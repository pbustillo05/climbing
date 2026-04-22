"""
multi_llm_automator.py
======================
Async Playwright script that sends a prompt (and optional files) to 11 LLMs
sequentially, saves each response as a Markdown file, and prints a summary table.

────────────────────────────────────────────────────────────────────────────────
SETUP & FIRST RUN
────────────────────────────────────────────────────────────────────────────────
1. Install dependencies (once):
       pip install playwright
       playwright install chromium

2. First run (headed, no --headless flag):
       python multi_llm_automator.py --prompt-file LLM_feedback/prompts/recovery.md

   The script opens a real browser window for each LLM.  When it detects a login
   wall it pauses and prints a message — sign in manually, then press Enter in
   the terminal to continue.  The session is persisted in ./browser_profiles/{slug}/
   so subsequent runs skip the login step entirely.

3. Test a single LLM before running all 11:
       python multi_llm_automator.py --prompt-file … --llms claude

4. Subsequent runs can add --headless once every session is saved.

5. File attachments:
       --files bibliography.bib sections/recovery.tex
   .bib and .tex files are automatically copied to temp .md files because some
   sites reject those extensions.  The copies are cleaned up after each run.

6. Maintaining selectors:
   Every locator that targets a specific UI element is annotated with a # TODO
   comment.  When a site redesigns its UI, update only that locator.
────────────────────────────────────────────────────────────────────────────────
"""

import argparse
import asyncio
import logging
import shutil
import sys
import tempfile
from datetime import datetime
from pathlib import Path

from playwright.async_api import (
    async_playwright,
    Page,
    BrowserContext,
    TimeoutError as PWTimeoutError,
)
from playwright_stealth import Stealth

# Single shared stealth instance — patches navigator.webdriver, chrome runtime,
# plugins, languages, etc. to avoid Cloudflare / bot-detection fingerprinting.
_STEALTH = Stealth(
    navigator_platform_override="MacIntel",
    navigator_vendor_override="Google Inc.",
)

# ──────────────────────────────────────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("multi_llm")

# ──────────────────────────────────────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────────────────────────────────────
CONFIG: dict[str, dict] = {
    "grok": {
        "name": "Grok",
        "url": "https://grok.com",
        "mode": "Expert",
        "slug": "grok",
        "supports_upload": True,
        # TODO: verify Expert toggle selector (April 2026)
        "mode_steps": [
            {"action": "click_if_exists", "role": "button", "name_contains": "Expert"},
        ],
        # Placeholder text in the chat input — update if Grok changes it
        # TODO: verify input placeholder (April 2026)
        "input_placeholder": "Ask anything",
        "login_check_url_fragment": "grok.com",
    },
    "meta": {
        "name": "Meta AI",
        "url": "https://www.meta.ai",
        "mode": "Thinking",
        "slug": "meta",
        "supports_upload": False,
        # TODO: verify Thinking toggle (April 2026)
        "mode_steps": [
            {"action": "click_if_exists", "role": "button", "name_contains": "Thinking"},
        ],
        "input_placeholder": "Ask Meta AI anything",
        "login_check_url_fragment": "meta.ai",
    },
    "chatgpt": {
        "name": "ChatGPT",
        "url": "https://chatgpt.com",
        "mode": "Deep Research",
        "slug": "chatgpt",
        "supports_upload": True,
        # Input is a contenteditable DIV with aria-label "Chat with ChatGPT"
        # TODO: verify Deep Research menu flow (April 2026)
        "mode_steps": [
            # Deep Research appears as a chip/button near the input after the page loads.
            # If not visible, it may be behind the "+" tools menu.
            {"action": "click_if_exists", "role": "button", "name_contains": "Deep research"},
            # Fallback: open the tools menu then click the option
            {"action": "click_if_exists", "role": "button", "name_contains": "More"},
            {"action": "click_if_exists", "role": "menuitem", "name_contains": "Deep research"},
        ],
        "input_placeholder": None,
        "input_aria_label": "Chat with ChatGPT",
        "login_check_url_fragment": "chatgpt.com",
    },
    "claude": {
        "name": "Claude",
        "url": "https://claude.ai/new",
        "mode": "Sonnet 4.6 / Adaptive Thinking",
        "slug": "claude",
        "supports_upload": True,
        # Input: contenteditable DIV, aria-label "Write your prompt to Claude"
        # Model button text: "Sonnet 4.6\nAdaptive" (confirmed April 2026)
        # TODO: re-verify model picker button text after model updates
        "mode_steps": [
            # The model selector button text starts with "Sonnet 4.6"
            {"action": "click_if_exists", "role": "button", "name_contains": "Sonnet 4.6"},
            # Adaptive Thinking should already be enabled as the default mode;
            # if there is an explicit toggle, click it.
            {"action": "click_if_exists", "role": "switch", "name_contains": "Extended thinking"},
            {"action": "click_if_exists", "role": "switch", "name_contains": "Adaptive"},
        ],
        "input_placeholder": None,
        "input_aria_label": "Write your prompt to Claude",
        "login_check_url_fragment": "claude.ai",
    },
    "kimi": {
        "name": "Kimi",
        "url": "https://www.kimi.com",
        "mode": "K2.6 / Thinking",
        "slug": "kimi",
        "supports_upload": True,
        # TODO: verify K2.6 model selector (April 2026)
        "mode_steps": [
            {"action": "click_if_exists", "role": "button", "name_contains": "K2"},
            {"action": "click_if_exists", "role": "option", "name_contains": "K2.6"},
            {"action": "click_if_exists", "role": "button", "name_contains": "Thinking"},
        ],
        "input_placeholder": "Ask anything",
        "login_check_url_fragment": "kimi.com",
    },
    "copilot": {
        "name": "Microsoft Copilot",
        "url": "https://copilot.microsoft.com",
        "mode": "Search",
        "slug": "copilot",
        "supports_upload": True,
        # TODO: verify Search toggle (April 2026)
        "mode_steps": [
            {"action": "click_if_exists", "role": "radio", "name_contains": "Search"},
            {"action": "click_if_exists", "role": "button", "name_contains": "Search"},
        ],
        "input_placeholder": "Ask me anything",
        "login_check_url_fragment": "copilot.microsoft.com",
    },
    "github_copilot": {
        "name": "GitHub Copilot",
        "url": "https://github.com/copilot",
        "mode": "GPT 5.2",
        "slug": "github_copilot",
        "supports_upload": True,
        # TODO: verify GPT-5.2 model selector (April 2026)
        "mode_steps": [
            {"action": "click_if_exists", "role": "button", "name_contains": "model"},
            {"action": "click_if_exists", "role": "option", "name_contains": "GPT 5.2"},
        ],
        "input_placeholder": "Ask Copilot",
        "login_check_url_fragment": "github.com",
    },
    "gemini": {
        "name": "Gemini",
        "url": "https://gemini.google.com/app",
        "mode": "Pro",
        "slug": "gemini",
        "supports_upload": True,
        # TODO: verify Gemini Pro selector (April 2026)
        "mode_steps": [
            {"action": "click_if_exists", "role": "button", "name_contains": "Gemini"},
            {"action": "click_if_exists", "role": "option", "name_contains": "Pro"},
        ],
        "input_placeholder": "Ask Gemini",
        "login_check_url_fragment": "gemini.google.com",
    },
    "perplexity": {
        "name": "Perplexity",
        "url": "https://www.perplexity.ai",
        "mode": "Deep Research",
        "slug": "perplexity",
        "supports_upload": True,
        # Input: contenteditable DIV, placeholder "Ask anything…" (Unicode ellipsis)
        # "Model" button confirmed on main page (April 2026).
        # Deep Research is selected via the "Model" button → choose Research/Pro Search.
        # TODO: verify exact menu item text for Deep Research under Model picker (April 2026)
        "mode_steps": [
            # Click the Model selector
            {"action": "click_if_exists", "role": "button", "name_contains": "Model"},
            # Choose Deep Research from the dropdown
            {"action": "click_if_exists", "role": "option", "name_contains": "Deep Research"},
            # Fallback: it might be labelled "Research" or appear as a button chip
            {"action": "click_if_exists", "role": "button", "name_contains": "Deep Research"},
        ],
        "input_placeholder": "Ask anything…",  # Unicode ellipsis, confirmed April 2026
        "input_aria_label": None,
        "login_check_url_fragment": "perplexity.ai",
    },
    "qwen": {
        "name": "Qwen",
        "url": "https://chat.qwen.ai",
        "mode": "Deep Research / Advanced",
        "slug": "qwen",
        "supports_upload": True,
        # TODO: verify Advanced / Deep Research selectors (April 2026)
        "mode_steps": [
            {"action": "click_if_exists", "role": "button", "name_contains": "Advanced"},
            {"action": "click_if_exists", "role": "button", "name_contains": "Deep Research"},
        ],
        "input_placeholder": "Ask anything",
        "login_check_url_fragment": "qwen.ai",
    },
    "deepseek": {
        "name": "DeepSeek",
        "url": "https://chat.deepseek.com",
        "mode": "DeepThink / Search",
        "slug": "deepseek",
        "supports_upload": True,
        # Input: TEXTAREA, placeholder "Message DeepSeek" (confirmed April 2026)
        # DeepThink + Search toggles render above the input; exact button text unconfirmed
        # (buttons were not in console snapshot — likely lazy-rendered after focus).
        # TODO: confirm exact toggle label text (April 2026)
        "mode_steps": [
            {"action": "click_if_exists", "role": "button", "name_contains": "DeepThink"},
            {"action": "click_if_exists", "role": "button", "name_contains": "Deep Think"},
            {"action": "click_if_exists", "role": "button", "name_contains": "Search"},
        ],
        "input_placeholder": "Message DeepSeek",  # confirmed April 2026
        "input_aria_label": None,
        "login_check_url_fragment": "deepseek.com",
    },
}

# ──────────────────────────────────────────────────────────────────────────────
# File-extension remapping
# Some sites reject .bib / .tex uploads; remap to .md transparently.
# ──────────────────────────────────────────────────────────────────────────────
EXTENSION_REMAP = {".bib": ".md", ".tex": ".md"}


def prepare_files(files: list[str], tmp_dir: Path) -> list[str]:
    """
    Copy files whose extensions are in EXTENSION_REMAP into tmp_dir with the
    remapped extension.  Other files are passed through unchanged.
    Returns a list of absolute paths ready for upload.
    """
    out: list[str] = []
    for f in files:
        p = Path(f)
        mapped_ext = EXTENSION_REMAP.get(p.suffix.lower())
        if mapped_ext:
            dest = tmp_dir / (p.stem + mapped_ext)
            shutil.copy2(p, dest)
            log.info("Remapped %s → %s for upload", p.name, dest.name)
            out.append(str(dest))
        else:
            out.append(str(p))
    return out


PROFILES_DIR = Path("./browser_profiles")


def profile_dir(slug: str) -> str:
    d = PROFILES_DIR / slug
    d.mkdir(parents=True, exist_ok=True)
    return str(d)


# ──────────────────────────────────────────────────────────────────────────────
# Mode selection
# ──────────────────────────────────────────────────────────────────────────────

async def select_mode(page: Page, cfg: dict) -> None:
    for step in cfg.get("mode_steps", []):
        action = step.get("action")
        if action == "press_escape":
            await page.keyboard.press("Escape")
            await page.wait_for_timeout(400)
            continue
        role = step.get("role", "button")
        name_contains: str = step.get("name_contains", "")
        if action == "click_if_exists":
            try:
                locator = page.get_by_role(role, name=name_contains)  # type: ignore[arg-type]
                if await locator.first.is_visible(timeout=2000):
                    await locator.first.click()
                    log.debug("Mode step: clicked %s '%s'", role, name_contains)
                    await page.wait_for_timeout(600)
            except Exception as exc:
                log.debug("Mode step skipped (%s '%s'): %s", role, name_contains, exc)


# ──────────────────────────────────────────────────────────────────────────────
# File upload
# ──────────────────────────────────────────────────────────────────────────────

async def upload_files(page: Page, files: list[str], cfg: dict) -> list[str]:
    if not files:
        return []
    if not cfg.get("supports_upload", False):
        log.warning("[%s] File upload not supported; skipping.", cfg["slug"])
        return []

    attach_locators = [
        page.get_by_role("button", name="Attach"),
        page.get_by_role("button", name="Attach files"),
        page.get_by_role("button", name="Upload"),
        page.get_by_label("Attach files"),
        page.get_by_label("Upload files"),
        page.get_by_role("button", name="Add files"),
        # Claude.ai uses a "+" button labelled "Add content" (confirmed April 2026)
        page.get_by_label("Add content"),
        page.get_by_role("button", name="Add content"),
        # TODO: add site-specific attach labels (April 2026)
    ]

    for loc in attach_locators:
        try:
            if await loc.first.is_visible(timeout=1500):
                async with page.expect_file_chooser(timeout=5000) as fc_info:
                    await loc.first.click()
                fc = await fc_info.value
                await fc.set_files(files)
                attached = [Path(f).name for f in files]
                log.info("[%s] Uploaded: %s", cfg["slug"], attached)
                await page.wait_for_timeout(1500)
                return attached
        except Exception:
            continue

    # Fallback: click any hidden <input type="file">
    try:
        async with page.expect_file_chooser(timeout=3000) as fc_info:
            await page.evaluate("document.querySelector('input[type=file]')?.click()")
        fc = await fc_info.value
        await fc.set_files(files)
        attached = [Path(f).name for f in files]
        log.info("[%s] Uploaded via hidden input: %s", cfg["slug"], attached)
        await page.wait_for_timeout(1500)
        return attached
    except Exception:
        pass

    log.warning("[%s] No file-chooser trigger found; skipping upload.", cfg["slug"])
    return []


# ──────────────────────────────────────────────────────────────────────────────
# Prompt submission
# Uses clipboard paste to handle multi-line prompts correctly on all sites.
# ──────────────────────────────────────────────────────────────────────────────

async def send_prompt(page: Page, prompt: str, cfg: dict) -> None:
    aria_label = cfg.get("input_aria_label")
    placeholder = cfg.get("input_placeholder")
    # Build ordered locator list: site-specific hints first, generic fallbacks last
    input_locators = []
    if aria_label:
        input_locators.append(page.get_by_label(aria_label))
    if placeholder:
        input_locators.append(page.get_by_placeholder(placeholder))
    input_locators += [
        page.get_by_role("textbox", name="Message"),
        page.get_by_placeholder("Message"),
        page.get_by_placeholder("Ask anything"),
        page.get_by_placeholder("Type a message"),
        page.get_by_placeholder("Send a message"),
        page.get_by_role("textbox"),
        # TODO: add site-specific fallbacks (April 2026)
    ]

    input_el = None
    for loc in input_locators:
        try:
            if await loc.first.is_visible(timeout=2000):
                input_el = loc.first
                break
        except Exception:
            continue

    if input_el is None and aria_label:
        # get_by_label may miss contenteditable divs; try direct attribute selector
        try:
            loc = page.locator(f'[aria-label="{aria_label}"]')
            if await loc.first.is_visible(timeout=3000):
                input_el = loc.first
        except Exception:
            pass

    if input_el is None:
        # Fallback: any visible contenteditable div
        try:
            input_el = page.locator("[contenteditable='true']").first
            await input_el.wait_for(state="visible", timeout=5000)
        except Exception as exc:
            raise RuntimeError("Could not find a chat input element") from exc

    await input_el.click()

    # Use clipboard paste so multi-line content is inserted exactly.
    # navigator.clipboard.writeText requires the page to have focus — it does after click().
    escaped = prompt.replace("`", "\\`").replace("\\", "\\\\").replace("$", "\\$")
    await page.evaluate(
        f"navigator.clipboard.writeText(`{escaped}`)"
    )
    modifier = "Meta" if sys.platform == "darwin" else "Control"
    await page.keyboard.press(f"{modifier}+a")  # select all (clear any placeholder)
    await page.keyboard.press(f"{modifier}+v")  # paste
    await page.wait_for_timeout(500)

    # Try Ctrl/Cmd+Enter first (safer for multi-line sites), then plain Enter
    await page.keyboard.press(f"{modifier}+Return")
    await page.wait_for_timeout(800)

    # If the message is still in the box (wasn't submitted), try plain Enter
    still_there = False
    try:
        val = await input_el.input_value()
        still_there = bool(val and len(val) > 20)
    except Exception:
        pass
    if not still_there:
        # Also check contenteditable
        try:
            val = await input_el.inner_text()
            still_there = bool(val and len(val) > 20)
        except Exception:
            pass

    if still_there:
        await page.keyboard.press("Enter")

    # Final fallback: explicit Send button
    send_locators = [
        page.get_by_role("button", name="Send"),
        page.get_by_role("button", name="Submit"),
        page.get_by_label("Send message"),
        page.get_by_label("Send"),
        # TODO: update if a site changes its send-button label (April 2026)
    ]
    for loc in send_locators:
        try:
            if await loc.first.is_visible(timeout=1000):
                await loc.first.click()
                log.debug("Submitted via Send button")
                break
        except Exception:
            continue


# ──────────────────────────────────────────────────────────────────────────────
# Response extraction + idle detection
# ──────────────────────────────────────────────────────────────────────────────

_STOP_BUTTON_NAMES = ["Stop generating", "Stop", "Cancel"]

_SPINNER_SELECTORS = [
    # Generic ARIA busy indicators
    "[aria-label*='loading' i]",
    "[aria-label*='thinking' i]",
    "[aria-label*='generating' i]",
    # Common spinner class fragments — brittle but last resort
    # TODO: remove if causing false positives (April 2026)
    ".loading-indicator",
    ".spinner",
]


async def _response_is_streaming(page: Page) -> bool:
    """Return True if the LLM is still visibly generating."""
    for name in _STOP_BUTTON_NAMES:
        try:
            if await page.get_by_role("button", name=name).first.is_visible(timeout=300):
                return True
        except Exception:
            pass
    for sel in _SPINNER_SELECTORS:
        try:
            if await page.locator(sel).first.is_visible(timeout=300):
                return True
        except Exception:
            pass
    return False


async def extract_response(page: Page) -> str:
    """
    Extract the last assistant message from the page.
    Tries site-specific patterns first, then generic fallbacks.
    """
    candidates = [
        # OpenAI / ChatGPT
        "Array.from(document.querySelectorAll('[data-message-author-role=\"assistant\"]'))",
        # Claude
        "Array.from(document.querySelectorAll('[data-testid=\"conversation-turn-assistant\"], .claude-message'))",
        # Gemini
        "Array.from(document.querySelectorAll('message-content, .model-response-text'))",
        # Perplexity / Copilot — article tags
        "Array.from(document.querySelectorAll('article'))",
        # Generic: any element with role=log or role=feed
        "Array.from(document.querySelectorAll('[role=\"log\"], [role=\"feed\"]'))",
        # Last resort: full <main>
        "Array.from(document.querySelectorAll('main'))",
    ]
    for expr in candidates:
        try:
            text = await page.evaluate(f"""
                (() => {{
                    const nodes = {expr};
                    if (!nodes.length) return null;
                    const last = nodes[nodes.length - 1];
                    return last ? last.innerText.trim() : null;
                }})()
            """)
            if text and len(text) > 30:
                return text
        except Exception:
            continue
    try:
        return await page.inner_text("body")
    except Exception:
        return "(could not extract response)"


async def wait_for_idle(page: Page, timeout: int) -> str:
    """
    Wait until the LLM stops streaming AND the response text has been stable
    (unchanged) for at least 3 seconds.  Returns the extracted response text.
    """
    deadline = asyncio.get_event_loop().time() + timeout
    log.info("Waiting for response …")

    last_text = ""
    stable_since: float | None = None
    STABLE_SECS = 3.0

    while asyncio.get_event_loop().time() < deadline:
        streaming = await _response_is_streaming(page)
        current_text = await extract_response(page)

        if current_text != last_text:
            last_text = current_text
            stable_since = None
        else:
            if stable_since is None:
                stable_since = asyncio.get_event_loop().time()
            elif (asyncio.get_event_loop().time() - stable_since) >= STABLE_SECS and not streaming:
                log.info("Response stable for %.0fs — done.", STABLE_SECS)
                break

        await asyncio.sleep(2)
    else:
        log.warning("Timeout waiting for idle; using whatever text is available.")

    await page.wait_for_timeout(1000)
    return await extract_response(page)


# ──────────────────────────────────────────────────────────────────────────────
# Output writer
# ──────────────────────────────────────────────────────────────────────────────

def write_response(
    output_dir: Path,
    cfg: dict,
    prompt: str,
    files_attached: list[str],
    response_text: str,
) -> Path:
    out_path = output_dir / f"{cfg['slug']}_response.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    files_str = ", ".join(files_attached) if files_attached else "none"
    # Truncate prompt in header to keep files readable
    prompt_preview = prompt[:300] + "…" if len(prompt) > 300 else prompt
    content = (
        f"# Response from {cfg['name']} — {cfg['mode']}\n"
        f"**Timestamp:** {timestamp}\n"
        f"**Prompt:** {prompt_preview}\n"
        f"**Files attached:** {files_str}\n\n"
        f"{response_text}\n"
    )
    out_path.write_text(content, encoding="utf-8")
    return out_path


# ──────────────────────────────────────────────────────────────────────────────
# Readiness check — is the chat input actually on screen?
# ──────────────────────────────────────────────────────────────────────────────

async def _chat_input_visible(page: Page, cfg: dict) -> bool:
    """Return True if the chat input element is visible on the current page."""
    candidates = []
    aria_label = cfg.get("input_aria_label")
    placeholder = cfg.get("input_placeholder")
    if aria_label:
        candidates.append(page.locator(f'[aria-label="{aria_label}"]'))
        candidates.append(page.get_by_label(aria_label))
    if placeholder:
        candidates.append(page.get_by_placeholder(placeholder))
    candidates += [
        page.get_by_role("textbox"),
        page.locator("[contenteditable='true']"),
        page.locator("textarea"),
    ]
    for loc in candidates:
        try:
            if await loc.first.is_visible(timeout=1500):
                return True
        except Exception:
            pass
    return False


# ──────────────────────────────────────────────────────────────────────────────
# Per-LLM runner
# ──────────────────────────────────────────────────────────────────────────────

async def run_llm(
    playwright,
    cfg: dict,
    prompt: str,
    files: list[str],
    output_dir: Path,
    headless: bool,
    timeout: int,
    retries: int,
    cdp_browser=None,  # pass a connected Browser object to use real Chrome
) -> tuple[bool, str, Path | None]:
    slug = cfg["slug"]
    for attempt in range(retries + 1):
        page: Page | None = None
        owned_context = False  # True only when we launched the context ourselves
        context: BrowserContext | None = None
        try:
            if cdp_browser is not None:
                # ── CDP mode: open a new tab in the user's real Chrome ─────
                context = cdp_browser.contexts[0] if cdp_browser.contexts else await cdp_browser.new_context()
                page = await context.new_page()
            else:
                # ── Persistent-context mode with stealth patches ───────────
                context = await playwright.chromium.launch_persistent_context(
                    user_data_dir=profile_dir(slug),
                    headless=headless,
                    viewport={"width": 1280, "height": 900},
                    permissions=["clipboard-read", "clipboard-write"],
                    args=[
                        "--unsafely-treat-insecure-origin-as-secure",
                        # Stealth: suppress automation-specific Chrome flags
                        "--disable-blink-features=AutomationControlled",
                    ],
                    # Stealth: use a realistic user-agent
                    user_agent=(
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/124.0.0.0 Safari/537.36"
                    ),
                    ignore_default_args=["--enable-automation"],
                )
                page = context.pages[0] if context.pages else await context.new_page()
                owned_context = True

            # Apply stealth patches before any navigation
            await _STEALTH.apply_stealth_async(page)

            log.info("[%s] Navigating to %s", slug, cfg["url"])
            await page.goto(cfg["url"], wait_until="domcontentloaded", timeout=60_000)
            await page.wait_for_timeout(3000)

            # ── Wait for chat input; pause for human if not visible ────────
            input_visible = await _chat_input_visible(page, cfg)
            if not input_visible:
                log.warning(
                    "[%s] ⚠  Chat input not visible.\n"
                    "    Handle any login/CAPTCHA in the browser, then press ENTER …",
                    slug,
                )
                await asyncio.get_event_loop().run_in_executor(None, input)
                await page.wait_for_timeout(2000)

            # ── Mode / model selection ─────────────────────────────────────
            log.info("[%s] Selecting mode: %s", slug, cfg["mode"])
            await select_mode(page, cfg)

            # ── File upload ────────────────────────────────────────────────
            files_attached = await upload_files(page, files, cfg)

            # ── Send prompt ────────────────────────────────────────────────
            log.info("[%s] Sending prompt …", slug)
            await send_prompt(page, prompt, cfg)

            # ── Wait for full response ─────────────────────────────────────
            response_text = await wait_for_idle(page, timeout)
            if not response_text.strip():
                raise RuntimeError("Extracted response is empty")

            out_path = write_response(output_dir, cfg, prompt, files_attached, response_text)
            log.info("[%s] Saved → %s", slug, out_path)

            if cdp_browser is not None:
                await page.close()  # just close the tab, leave Chrome running
            elif owned_context and context:
                await context.close()
            return True, "", out_path

        except Exception as exc:
            log.error("[%s] Attempt %d/%d failed: %s", slug, attempt + 1, retries + 1, exc)
            if page:
                try:
                    await page.close()
                except Exception:
                    pass
            if owned_context and context:
                try:
                    await context.close()
                except Exception:
                    pass
            if attempt == retries:
                return False, str(exc), None
            await asyncio.sleep(3)

    return False, "Unknown error", None


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

async def main(args: argparse.Namespace) -> None:
    # ── Resolve prompt ────────────────────────────────────────────────────────
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8")
        log.info("Loaded prompt from %s (%d chars)", args.prompt_file, len(prompt))
    else:
        prompt = args.prompt

    # ── Resolve files + remap extensions ─────────────────────────────────────
    raw_files: list[str] = []
    if args.files:
        for f in args.files:
            p = Path(f)
            if not p.exists():
                log.error("File not found, skipping: %s", f)
            else:
                raw_files.append(str(p.resolve()))

    # ── Determine which LLMs to run ───────────────────────────────────────────
    llm_keys = list(CONFIG.keys())
    if args.llms:
        requested = [s.strip() for s in args.llms]
        unknown = [s for s in requested if s not in CONFIG]
        if unknown:
            log.error("Unknown LLM slug(s): %s.  Valid: %s", unknown, list(CONFIG.keys()))
            sys.exit(1)
        llm_keys = requested

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results: list[dict] = []

    with tempfile.TemporaryDirectory(prefix="llm_uploads_") as tmp_str:
        tmp_dir = Path(tmp_str)
        files = prepare_files(raw_files, tmp_dir)

        async with async_playwright() as playwright:
            # ── CDP mode: connect to user's real Chrome ───────────────────
            cdp_browser = None
            if args.cdp:
                try:
                    cdp_browser = await playwright.chromium.connect_over_cdp(args.cdp_url)
                    log.info("Connected to Chrome via CDP at %s", args.cdp_url)
                except Exception as exc:
                    log.error(
                        "Could not connect to Chrome at %s: %s\n"
                        "Make sure Chrome is running with:\n"
                        '  /Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome '
                        "--remote-debugging-port=9222 --no-first-run",
                        args.cdp_url, exc,
                    )
                    sys.exit(1)

            for slug in llm_keys:
                cfg = CONFIG[slug]
                print(f"\n{'─'*60}")
                print(f"  {cfg['name']}  ({cfg['mode']})")
                print(f"{'─'*60}")

                success, error, out_path = await run_llm(
                    playwright=playwright,
                    cfg=cfg,
                    prompt=prompt,
                    files=files,
                    output_dir=output_dir,
                    headless=args.headless,
                    timeout=args.timeout,
                    retries=args.retries,
                    cdp_browser=cdp_browser,
                )
                results.append(
                    {
                        "name": cfg["name"],
                        "mode": cfg["mode"],
                        "success": success,
                        "error": error,
                        "path": str(out_path) if out_path else "—",
                    }
                )

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"\n{'═'*80}")
    print("  SUMMARY")
    print(f"{'═'*80}")
    W_NAME, W_MODE, W_STATUS = 22, 28, 8
    print(f"{'LLM':<{W_NAME}} {'Mode':<{W_MODE}} {'Status':<{W_STATUS}} Output / Error")
    print("─" * 80)
    for r in results:
        status = "OK" if r["success"] else "FAIL"
        detail = r["path"] if r["success"] else r["error"][:45]
        print(f"{r['name']:<{W_NAME}} {r['mode']:<{W_MODE}} {status:<{W_STATUS}} {detail}")
    print(f"{'═'*80}\n")

    summary_path = output_dir / "summary.md"
    with summary_path.open("w", encoding="utf-8") as fh:
        fh.write("# LLM Automation Summary\n")
        fh.write(f"**Run at:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        fh.write("| LLM | Mode | Status | Output |\n|-----|------|--------|--------|\n")
        for r in results:
            status = "✓" if r["success"] else "✗"
            detail = r["path"] if r["success"] else r["error"][:60]
            fh.write(f"| {r['name']} | {r['mode']} | {status} | {detail} |\n")
    log.info("Summary → %s", summary_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send a prompt to LLMs sequentially via Playwright and save responses.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", help="Prompt text (inline string).")
    prompt_group.add_argument("--prompt-file", metavar="FILE", help="Path to a file whose contents are the prompt.")

    parser.add_argument(
        "--files", nargs="+", metavar="FILE", default=[],
        help=".bib and .tex files are auto-remapped to .md for upload compatibility.",
    )
    parser.add_argument(
        "--llms", nargs="+", metavar="SLUG",
        help=f"Run only these LLM slugs (space-separated). Valid: {', '.join(CONFIG.keys())}",
    )
    parser.add_argument("--output-dir", default="./llm_responses")
    parser.add_argument("--headless", action="store_true", default=False)
    parser.add_argument("--timeout", type=int, default=600, help="Seconds per LLM (default 600).")
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument(
        "--cdp", action="store_true", default=False,
        help=(
            "Connect to your already-running Chrome via CDP instead of launching a new browser. "
            "Requires Chrome to be started with --remote-debugging-port=9222. "
            "This bypasses all CAPTCHA/bot-detection issues because it uses your real sessions."
        ),
    )
    parser.add_argument(
        "--cdp-url", default="http://127.0.0.1:9222",
        help="CDP endpoint URL (default: http://127.0.0.1:9222).",
    )

    asyncio.run(main(parser.parse_args()))

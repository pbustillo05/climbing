You are an expert Python + Playwright automation engineer. Write a **complete, self-contained, production-ready, async Python script** named `multi_llm_automator.py` that does the following:

### Core Requirements
- Takes command-line arguments via `argparse`:
  - `--prompt TEXT` (required): the prompt to send to every LLM
  - `--files FILE1 [FILE2 ...]` (optional): list of local files to attach/upload to each chat (skip gracefully if a site doesn't support uploads)
  - `--output-dir DIR` (default: `./llm_responses`): folder where responses are saved
  - `--headless` (flag, default False): run browsers headless
  - `--timeout SECONDS` (default 600): max wait time per LLM response
  - `--retries N` (default 2): number of retries on transient failures

- Creates the output directory if it doesn't exist.
- Processes the 11 LLMs **sequentially** (one browser context at a time) to keep resource usage reasonable.
- Uses **Playwright persistent contexts** with a dedicated user-data directory per LLM (`./browser_profiles/{slug}/`). The user only logs in once per site on first run; subsequent runs reuse the logged-in session.
- For every LLM:
  1. Launches (or reuses) the persistent context.
  2. Navigates to the correct URL.
  3. Selects the exact model/mode specified below.
  4. Uploads the provided files (if the site supports file upload via the standard filechooser).
  5. Pastes the prompt into the chat input and sends it.
  6. Waits until the full response is generated (poll for disappearance of "Stop generating", "Thinking...", streaming indicators, etc.).
  7. Extracts the clean full response text.
  8. Saves it as `{output_dir}/{slug}_response.md` with this exact header format:

     ```markdown
     # Response from {LLM Name} — {Mode}
     **Timestamp:** YYYY-MM-DD HH:MM:SS
     **Prompt:** {original prompt}
     **Files attached:** {comma-separated list or "none"}
     
     {full_response_text}
     ```

- At the end prints a clean Markdown summary table showing success/failure + file path for each LLM.
- Includes excellent logging (Python `logging` module, INFO + WARNING + ERROR), full try/except with retries, timeouts, and clear TODO comments everywhere a selector might need future updating.
- Uses **only robust Playwright locators** (`get_by_role`, `get_by_text`, `get_by_label`, `get_by_test_id`, `get_by_placeholder`). Never use brittle CSS or XPath unless absolutely unavoidable (and comment it).
- Fully documented with a large top-level docstring that explains installation, first-run login procedure, and how to maintain the CONFIG.

### LLM Configuration (use exactly these names, URLs, and modes)
Create a top-level `CONFIG = { ... }` dictionary with one entry per LLM. Populate every field with sensible defaults and include detailed comments. The script must read from this dict and have helper functions like `select_mode(page, config)` and `upload_files(page, files)` that work for all sites.

```python
CONFIG = {
    "grok": {
        "name": "Grok",
        "url": "https://grok.com",
        "mode": "Expert",
        "slug": "grok",
        # mode selection steps go here
    },
    "meta": {
        "name": "Meta AI",
        "url": "https://www.meta.ai",
        "mode": "Thinking",
        "slug": "meta",
    },
    "chatgpt": {
        "name": "ChatGPT",
        "url": "https://chatgpt.com",
        "mode": "Deep Research",
        "slug": "chatgpt",
        # note: Deep Research is selected via the + / tools menu or by typing /Deepresearch
    },
    "claude": {
        "name": "Claude",
        "url": "https://claude.ai",
        "mode": "Sonnet 4.6 / Adaptive Thinking",
        "slug": "claude",
    },
    "kimi": {
        "name": "Kimi",
        "url": "https://www.kimi.com",
        "mode": "K2.6 / Thinking",
        "slug": "kimi",
    },
    "copilot": {
        "name": "Microsoft Copilot",
        "url": "https://copilot.microsoft.com",   # most reliable 2026 URL
        "mode": "Search",
        "slug": "copilot",
    },
    "github_copilot": {
        "name": "GitHub Copilot",
        "url": "https://github.com/copilot",
        "mode": "GPT 5.2",
        "slug": "github_copilot",
    },
    "gemini": {
        "name": "Gemini",
        "url": "https://gemini.google.com/app",
        "mode": "Pro",
        "slug": "gemini",
    },
    "perplexity": {
        "name": "Perplexity",
        "url": "https://www.perplexity.ai",
        "mode": "Deep Research",
        "slug": "perplexity",
    },
    "qwen": {
        "name": "Qwen",
        "url": "https://chat.qwen.ai",
        "mode": "Deep Research / Advanced",
        "slug": "qwen",
    },
    "deepseek": {
        "name": "DeepSeek",
        "url": "https://chat.deepseek.com",
        "mode": "Expert / Search",
        "slug": "deepseek",
    },
}
```

For each entry, implement realistic `mode_selection` steps (list of dicts or a small async helper) based on current 2026 UIs. For example, ChatGPT Deep Research uses the "+" menu → "Deep research". Add clear comments like `# TODO: update selector if UI changes (April 2026)` next to every locator.

### Additional Technical Details
- Use `asyncio` and `async_playwright`.
- `playwright install chromium` once.
- Gracefully skip file upload (with WARNING log) if the site does not trigger a filechooser or has no attach button.
- Support multiple files (most sites now allow several PDFs, images, CSVs, etc.).
- Make the script runnable on Windows/macOS/Linux.
- Include a full `__main__` block with argument parsing and a nice progress printout.
- Add a section at the very top of the script (as a big comment block) titled "SETUP & FIRST RUN" that tells the user exactly what to do.

Output **only** the complete Python script (no extra explanations outside the code). The script must be ready to run after `pip install playwright` and `playwright install chromium`.

Start writing the script now.
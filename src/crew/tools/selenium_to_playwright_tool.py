"""Tool to assist in converting Selenium Python tests to Playwright equivalents."""
from typing import Dict, Any
import re

from crewai_tools import tool


@tool("SeleniumToPlaywrightConverter")
def convert_selenium_to_playwright(file_path: str, file_content: str) -> Dict[str, Any]:
    """Convert common Selenium patterns into Playwright equivalents.

    This performs pattern-based conversions and returns a dictionary with a
    converted file and a short summary. The conversion is intentionally
    conservative — complex or async/sync differences are flagged for manual
    review.

    Args:
        file_path: Path to the original file (used for context in messages).
        file_content: The original Python source text using Selenium APIs.

    Returns:
        A dict with keys:
          - converted: str (the converted file content)
          - summary: str (human-readable summary of changes and caveats)
    """
    converted = file_content

    # Remove Selenium-specific imports that are no longer needed
    converted = re.sub(r"from\s+selenium\.webdriver\.common\.by\s+import\s+By\n", "", converted)

    # Basic API replacements (pattern-based; review recommended)
    mappings = [
        (r"driver\.get\(([^)]+)\)", r"page.goto(\1)"),
        (r"driver\.find_element\(By\.ID,\s*([^\)]+)\)", r"page.locator('#' + \1)"),
        (r"driver\.find_element\(By\.CSS_SELECTOR,\s*([^\)]+)\)", r"page.locator(\1)"),
        (r"driver\.find_element\(By\.XPATH,\s*([^\)]+)\)", r"page.locator('xpath=' + \1)"),
        (r"\.send_keys\(([^)]+)\)", r".fill(\1)"),
        # clicks are preserved but semantics may differ; keep explicit
        (r"\.click\(\)", r".click()"),
    ]

    for pat, repl in mappings:
        converted = re.sub(pat, repl, converted)

    summary_lines = [
        "Applied conservative, regex-based Selenium -> Playwright transformations.",
        "Manual review recommended for async behavior, complex waiting patterns, and custom helpers.",
    ]

    return {"converted": converted, "summary": "\n".join(summary_lines)}

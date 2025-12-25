"""Tool to run Playwright tests and return JSON results."""
from typing import Any, Dict
import subprocess
import json

from crewai_tools import tool


@tool("PlaywrightRunnerTool")
def run_playwright_tests(test_path: str = "") -> Dict[str, Any]:
    """Run Playwright tests via npx and parse JSON reporter output.

    Uses `npx playwright test --reporter=json` to obtain machine readable
    test results. Returns a dictionary containing the returncode and parsed
    results or raw output on parse failure.
    """
    cmd = ["npx", "playwright", "test"]
    if test_path:
        cmd.append(test_path)
    cmd.extend(["--reporter=json"])  # JSON reporter is easy to parse

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except FileNotFoundError:
        return {"error": "npx not found. Ensure Node.js and Playwright are installed."}

    stdout = proc.stdout or ""
    stderr = proc.stderr or ""

    try:
        parsed = json.loads(stdout)
        return {"returncode": proc.returncode, "results": parsed}
    except json.JSONDecodeError:
        # Fallback: return raw output for debugging
        return {"returncode": proc.returncode, "stdout": stdout, "stderr": stderr}

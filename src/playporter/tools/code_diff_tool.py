"""Tool to generate unified diffs between two versions of code."""
from typing import Dict, Any
import difflib

from crewai_tools import tool


@tool("CodeDiffTool")
def unified_diff(original_path: str, original_content: str, new_path: str, new_content: str) -> Dict[str, Any]:
    """Return a unified diff between original and new file contents.

    Args:
        original_path: path for the original file (used in diff headers)
        original_content: original file content
        new_path: path for the new file
        new_content: new file content

    Returns:
        A dictionary containing `diff` (string) with unified diff output.
    """
    original_lines = original_content.splitlines(keepends=True)
    new_lines = new_content.splitlines(keepends=True)

    diff_lines = difflib.unified_diff(original_lines, new_lines, fromfile=original_path, tofile=new_path, lineterm="")
    return {"diff": "\n".join(diff_lines)}

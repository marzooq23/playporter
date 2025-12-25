"""Tool to create a branch and commit converted files to Git."""
from typing import Any, Dict, List
import subprocess

from crewai_tools import tool


@tool("GitCommitTool")
def commit_files(repo_path: str, files: List[str], branch: str = "playwright-migration", message: str = "Migrate Selenium tests to Playwright") -> Dict[str, Any]:
    """Create or checkout a branch, add files and commit them.

    Args:
        repo_path: path to the git repository
        files: list of file paths (relative or absolute) to add
        branch: branch name to create/use
        message: commit message

    Returns:
        A dict with status or error information.
    """
    try:
        # Ensure branch exists or create it
        existing = subprocess.run(["git", "rev-parse", "--verify", branch], cwd=repo_path, capture_output=True, text=True)
        if existing.returncode != 0:
            subprocess.run(["git", "checkout", "-b", branch], cwd=repo_path, check=True)
        else:
            subprocess.run(["git", "checkout", branch], cwd=repo_path, check=True)

        subprocess.run(["git", "add"] + files, cwd=repo_path, check=True)
        subprocess.run(["git", "commit", "-m", message], cwd=repo_path, check=True)

        # Get latest commit SHA
        sha_proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo_path, capture_output=True, text=True, check=True)
        commit_sha = sha_proc.stdout.strip()

        return {"status": "committed", "branch": branch, "commit_sha": commit_sha}
    except subprocess.CalledProcessError as e:
        return {"error": str(e), "stdout": getattr(e, 'stdout', ''), "stderr": getattr(e, 'stderr', '')}

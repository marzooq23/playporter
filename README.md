# 🎭 PlayPorter — AI-Powered Selenium → Playwright Migration Crew

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Agentic_Framework-orange.svg)](https://github.com/joaomdmoura/crewai)
[![Playwright](https://img.shields.io/badge/Playwright-Automation-green.svg)](https://playwright.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build Status](https://img.shields.io/github/actions/workflow/status/yourusername/playporter/ci.yml?branch=main&logo=github)](https://github.com/yourusername/playporter/actions)

---

**PlayPorter** is an agentic ecosystem built with [CrewAI](https://github.com/joaomdmoura/crewai) that intelligently migrates existing **Selenium** test frameworks to **Playwright**.

It uses a coordinated team of AI agents to:
- 🧠 Analyze Selenium test suites  
- ⚙️ Convert them into Playwright equivalents  
- 🧪 Validate correctness via runtime testing  
- 🔍 Review diffs between old and new code  
- 🪣 Commit results to Git automatically  
- 📄 Generate a detailed migration report  

---

## 🚀 Features

| Capability | Description |
|-------------|--------------|
| 🧠 **Code Analysis** | Extracts Selenium test logic, locators, and dependencies. |
| ⚙️ **Automated Migration** | Converts Selenium syntax to Playwright async patterns. |
| 🧪 **Runtime Validation** | Executes Playwright tests and captures structured results. |
| 🔍 **Diff Review** | Provides line-by-line differences between old and new tests. |
| 🪣 **Git Integration** | Automatically commits converted tests to a new branch. |
| 📄 **Documentation** | Generates a Markdown migration summary and results report. |

---

## 🧬 Agentic Ecosystem

| Agent | Role | Tools |
|--------|------|--------|
| **Code Analyzer** | Understands Selenium tests and locators. | `FileReadTool`, `SerperDevTool` |
| **Migration Engineer** | Converts Selenium to Playwright and commits results. | `SeleniumToPlaywrightConverter`, `GitCommitTool` |
| **QA Validator** | Runs Playwright tests to confirm migration success. | `PlaywrightRunnerTool` |
| **Diff Reviewer** | Reviews differences between Selenium and Playwright scripts. | `CodeDiffTool` |
| **Documentation Agent** | Creates the final migration report. | `FileWriteTool` |

---

## 🗂 Project Structure

```text
playporter/
├── README.md
├── pyproject.toml
└── src/
    └── playporter/
        ├── crew.py
        ├── main.py
        ├── config/
        │   ├── agents.yaml
        │   └── tasks.yaml
        └── tools/
            ├── selenium_to_playwright_tool.py
            ├── playwright_runner_tool.py
            ├── code_diff_tool.py
            └── git_commit_tool.py
```


## ⚙️ Setup & Usage

### 1️⃣ Install Dependencies
```bash
pip install crewai crewai-tools playwright
npx playwright install
```

### 2️⃣ Run PlayPorter
```bash
python -m src.playporter.main
```

### 3️⃣ Configuration

Edit the main.py inputs to match your project paths:

crew.kickoff(inputs={
    "selenium_project_path": "./old_selenium_tests/",
    "test_report_path": "./playwright_migrated_tests/results.json"
})

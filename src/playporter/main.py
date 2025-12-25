#!/usr/bin/env python
"""PlayPorter CLI entrypoint."""
from playporter.crew import create_crew


def main():
    """Create the PlayPorter crew and kickoff the migration flow with sample inputs."""
    crew = create_crew()
    crew.kickoff(inputs={
        "selenium_project_path": "./old_selenium_tests/",
        "test_report_path": "./playwright_migrated_tests/results.json"
    })


if __name__ == "__main__":
    main()

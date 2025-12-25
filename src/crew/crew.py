from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class Playporter():
    """PlayPorter Crew that orchestrates Selenium->Playwright migrations."""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def code_analyzer(self) -> Agent:
        return Agent(config=self.agents_config['code_analyzer'], verbose=True)

    @agent
    def migration_engineer(self) -> Agent:
        return Agent(config=self.agents_config['migration_engineer'], verbose=True)

    @agent
    def diff_reviewer(self) -> Agent:
        return Agent(config=self.agents_config['diff_reviewer'], verbose=True)

    @agent
    def qa_validator(self) -> Agent:
        return Agent(config=self.agents_config['qa_validator'], verbose=True)

    @agent
    def documentation_agent(self) -> Agent:
        return Agent(config=self.agents_config['documentation_agent'], verbose=True)

    @task
    def analyze_selenium_task(self) -> Task:
        return Task(config=self.tasks_config['analyze_selenium_task'])

    @task
    def migrate_tests_task(self) -> Task:
        return Task(config=self.tasks_config['migrate_tests_task'])

    @task
    def diff_review_task(self) -> Task:
        return Task(config=self.tasks_config['diff_review_task'])

    @task
    def validate_migration_task(self) -> Task:
        return Task(config=self.tasks_config['validate_migration_task'])

    @task
    def git_commit_task(self) -> Task:
        return Task(config=self.tasks_config['git_commit_task'])

    @task
    def generate_docs_task(self) -> Task:
        return Task(config=self.tasks_config['generate_docs_task'])

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)


def create_crew():
    """Factory helper to create Playporter crew."""
    return Playporter().crew()

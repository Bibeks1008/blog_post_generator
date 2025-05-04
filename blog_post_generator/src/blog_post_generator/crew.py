from crewai import Crew, Process
from blog_post_generator.agents.researcher_agent import ResearcherAgent
from blog_post_generator.agents.reporting_analyst_agent import ReportingAnalystAgent
from blog_post_generator.tasks.research_task import ResearchTask
from blog_post_generator.tasks.reporting_task import ReportingTask


class BlogPostGenerator:

    def __init__(self):
        self.researcher_agent = ResearcherAgent()
        self.reporting_analyst_agent = ReportingAnalystAgent()

        self.research_task = ResearchTask(
            description="Generate a structured outline for a blog post titled '{title}'",
            expected_output="A newline-separated list of section titles",
            agent=self.researcher_agent,
        )

        self.reporting_task = ReportingTask(
            description="Write the full blog post using the outline provided",
            expected_output="The complete article, one paragraph per section",
            agent=self.reporting_analyst_agent,
            context=[self.research_task],  # passes the outline to task #2
        )

    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher_agent, self.reporting_analyst_agent],
            tasks=[self.research_task, self.reporting_task],
            process=Process.sequential,
            verbose=True,
        )

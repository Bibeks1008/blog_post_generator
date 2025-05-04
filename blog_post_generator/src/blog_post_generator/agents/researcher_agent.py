from crewai import Agent


class ResearcherAgent(Agent):
    """Researcher Agent – turns a topic into a blog-post outline"""

    def __init__(self, config=None):
        super().__init__(
            role="Researcher",
            goal="Create clear, well-structured outlines for blog posts",
            backstory=(
                "A veteran content strategist who can break down any topic into a logical, easy-to-read structure."
            ),
            verbose=True,
            allow_delegation=False,
        )

    def execute_task(self, task, context=None, tools=None):
        title = (self.crew._inputs or {}).get("title")
        print(f"DEBUG: Researcher received title: {title}")
        if not title:
            raise ValueError("Title is required for generating blog outline")

        outline = [
            f"Introduction to {title}",
            f"Key trends and issues related to {title}",
            f"How {title} is changing the industry",
            f"Challenges with {title}",
            f"Conclusion and future predictions for {title}",
        ]
        print(f"DEBUG: Generated outline with {len(outline)} sections")

        return "\n".join(outline)

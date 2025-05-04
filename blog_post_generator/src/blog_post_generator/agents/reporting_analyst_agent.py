import os
import openai
from dotenv import load_dotenv
from crewai import Agent

load_dotenv()
print(f"DEBUG: Loaded OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY', '')[:5]}...")


class ReportingAnalystAgent(Agent):

    def __init__(self, config: dict | None = None):
        super().__init__(
            role="Writer",
            goal="Expand bullet-point ideas into clear, compelling prose",
            backstory=(
                "A seasoned AI copywriter who can take any outline and craft a "
                "readable, SEO-friendly blog post that keeps readers hooked."
            ),
            verbose=True,
            allow_delegation=False,
        )

    def execute_task(self, task, context=None, tools=None) -> str:
        outline_raw = context
        if not outline_raw:
            raise ValueError("Outline is required for generating the blog post")

        # Turn the outline string back into a Python list
        outline = [line.strip() for line in outline_raw.split("\n") if line.strip()]
        print(f"DEBUG: ReportingAnalyst received outline: {outline}")

        # Build the article, section by section
        blog_post_parts: list[str] = []
        for section in outline:
            blog_post_parts.append(section)
            blog_post_parts.append("")  # blank line after heading
            blog_post_parts.append(self._generate_paragraph(section))
            blog_post_parts.append("")  # blank line between sections

        return "\n".join(blog_post_parts).strip()


    def _generate_paragraph(self, section: str) -> str:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "Error: OPENAI_API_KEY not found in environment variables"

        model_name = os.getenv("MODEL", "gpt-3.5-turbo")

        try:
            from openai import OpenAI  # preferred style in modern SDK
            client = OpenAI(api_key=api_key)
            chat = client.chat
        except ImportError:
            # 🔙 Fallback for openai-python 0.28.x
            openai.api_key = api_key
            chat = openai.chat  # type: ignore[attr-defined]

        try:
            response = chat.completions.create(  
                model=model_name,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            "Write a detailed, engaging paragraph for the "
                            f"following blog-post section:\n{section}"
                        ),
                    }
                ],
                max_tokens=200,
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except Exception as exc:  # noqa: BLE001
            return (
                f"Error generating content for section '{section}': "
                f"{getattr(exc, 'message', exc)}"
            )

#!/usr/bin/env python
import sys
import warnings
import os

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from blog_post_generator.crew import BlogPostGenerator

def generate_blog_post(title: str):
    """Generates the blog post by running the CrewAI crew"""
    crew_instance = BlogPostGenerator()
    result = crew_instance.crew().kickoff(
        inputs={"title": title}
    )
    return result

def run():
    title = "The Future of AI in Healthcare"
    print(f"Generating blog post for topic: {title}")
    blog_post = generate_blog_post(title)
    print("\nGENERATED BLOG POST:\n")
    print(blog_post)

if __name__ == "__main__":
    run()
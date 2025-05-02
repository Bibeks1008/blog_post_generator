#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from blog_outline_generator import BlogOutlineGenerator
from blog_writer import BlogWriter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def generate_blog_post(title: str):
    outline_generator = BlogOutlineGenerator()
    outline = outline_generator.generate_outline(title)
    
    writer = BlogWriter()
    blog_post = writer.write_blog(outline)
    
    return blog_post

if __name__ == "__main__":
    title = "The Future of AI in Healthcare"
    blog_post = generate_blog_post(title)
    print(blog_post)

import openai
import os
from dotenv import load_dotenv
from openai import OpenAIError 

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 


class BlogWriter:
    def write_blog(self, outline: list) -> str:
        blog_post = ""
        
        for section in outline:
            blog_post += f"{section}\n\n"
            prompt = f"Expand the following blog outline into a detailed blog post section:\n\n{section}\n\nWrite a detailed paragraph based on the outline above."

            try:
                response = client.chat.completions.create(  
                    model=os.getenv("MODEL"),
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150,
                    temperature=0.7,
                    timeout=10
                )

                generated_content = response.choices[0].message.content.strip()
                blog_post += generated_content + "\n\n"

            except OpenAIError as e:  
                blog_post += f"Error generating content for section '{section}': {str(e)}\n\n"

        return blog_post

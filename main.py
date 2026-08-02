import os
from dotenv import load_dotenv
from agent import agent_brain
from tools.mock_provider import mock_provider
from prompts.system import SYSTEM_PROMPT

load_dotenv()

def main():
    key = os.getenv("API_KEY")
    if key is None:
        raise ValueError("API_KEY not found in environment variables.")

    articles = mock_provider()
    content =""
    for article in articles:
        content += f"""
Title: {article.title}
URL: {article.url}
Source: {article.source}
Published At: {article.published_at}
Summary: {article.summary}

"""
    
    messages = [
        {"role": "system", "content":SYSTEM_PROMPT},
        {"role":"user","content": content}
    ]
        
    print(agent_brain(key, messages,  "nvidia/nemotron-3-ultra-550b-a55b:free")) 

       


if __name__ == "__main__":
    main()

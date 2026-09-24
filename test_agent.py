import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AGENT_ROUTER_API_KEY"),  # Paste your sk-... token in your .env file
    base_url="https://co.agentrouter.org/v1",
)

response = client.chat.completions.create(
    model="claude-3-5-sonnet-20241022",
    messages=[{"role": "user", "content": "Hello, Claude!"}],
)

print(response.choices[0].message.content)
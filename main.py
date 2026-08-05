import os
from dotenv import load_dotenv
from agent import agent_brain
from tools.provider.mock_provider import mock_provider
from prompts.system import SYSTEM_PROMPT
from register_tools import register_tools
from prompts.Tools_prompt import build_tools_prompt
import json

load_dotenv()
tools = register_tools()
tools_prompt = build_tools_prompt(tools.list_tools())

def main():
    key = os.getenv("API_KEY")
    if key is None:
        raise ValueError("API_KEY not found in environment variables.")
        
    messages = [{"role": "system", "content": SYSTEM_PROMPT},
          {"role":"system","content": tools_prompt},
          {"role": "user", "content": "We are currently testing the tools. after the tool has returned the result analyse it and plan the next step as finished or other tool call"},
    ]
    while True:
        agent_response = json.loads(agent_brain(key, messages, "nvidia/nemotron-3-ultra-550b-a55b:free"))
        print(f"Agent: {agent_response} this of the type {type(agent_response)}")
        tool_action = None
        
        if agent_response["action"] == "tool":
           tool_action=tools.execute(agent_response["name"], agent_response["arguments"])
           print(f"Tool Action Result: {tool_action}")
       
        if agent_response["action"] == "finish":
            print("Agent has finished its task.")
            break
        messages.append({"role": "assistant", "content": json.dumps(agent_response)})
        if tool_action is not None:
            messages.append({"role": "assistant", "content": json.dumps(
    [article.__dict__ for article in tool_action],
    indent=2
)})


if __name__ == "__main__":
    main()

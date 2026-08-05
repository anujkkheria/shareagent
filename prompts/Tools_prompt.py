def build_tools_prompt(tools:list) -> str:
    tools_list = "\n".join([f"- {tool}" for tool in tools])
    return f"""
You have access to the following tools:
{tools_list}

"""
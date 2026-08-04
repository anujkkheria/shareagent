from models.tool import Tool

class ToolRegistry:
    def __init__(self):
        self.tools = {}
    def register_tool(self,tool:Tool) ->  None:
        if tool.name in self.tools:
            raise ValueError(f"Tool '{tool.name}' is already registered.")
        self.tools[tool.name] = tool
    def get_tool(self, tool_name:str) -> Tool:
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' is not registered.")
        return self.tools.get(tool_name)
    def list_tools(self) -> list:
        return [{
            "name": tool.name,
            "description": tool.description,
            "arguments": tool.arguments
        } for tool in self.tools.values()
    ]

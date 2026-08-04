from models.tool_registery import ToolRegistry
from models.tools import Tool
from tools.mock_tool import mock_tool


def register_tools():
    ToolRegistry().register_tool(
        Tool(
            "mock_tool",
            "This is a mock tool for testing and development purposes.",
            {},
            mock_tool,
        )
    )

from collections.abc import Callable
from typing import Any

class Tool():
    def __init__(self, name:str, description:str, arguments:dict[str, Any], func:Callable):
        self.name = name
        self.description = description
        self.arguments = arguments
        self.func = func
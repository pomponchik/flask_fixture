import os
import inspect
from dataclasses import dataclass
from typing import Tuple, Dict, Callable, Any


@dataclass
class RouteItem:
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    function: Callable
    path: str

    def __post_init__(self):
        self.path = os.path.abspath(inspect.getfile(self.function))

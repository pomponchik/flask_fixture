import os
import inspect
from dataclasses import dataclass
from typing import Tuple, Dict, Callable, Any, Optional


@dataclass
class RouteItem:
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    function: Callable
    path: Optional[str] = None
    module: Optional[str] = None

    def __post_init__(self):
        self.path = os.path.abspath(inspect.getfile(self.function))
        self.module = inspect.getmodule(self.function).__name__

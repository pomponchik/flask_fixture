import inspect
from dataclasses import dataclass
from typing import Tuple, Dict, Callable, Any, Optional


@dataclass
class RouteItem:
    """
    Storage of route signatures.
    """
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    function: Callable
    module: Optional[str] = None

    def __post_init__(self):
        self.module = inspect.getmodule(self.function).__name__

from dataclasses import dataclass
from typing import Tuple, Dict, Callable, Any


@dataclass
class RouteItem:
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    function: Callable

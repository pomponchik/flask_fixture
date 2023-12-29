import inspect
from dataclasses import dataclass
from typing import Tuple, Dict, Callable, Any, Optional


@dataclass
class RouteItem:
    """
    Storage of route signature.
    """
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    function: Callable[[Any], Any]

import inspect
from dataclasses import dataclass
from typing import Tuple, Dict, Callable, Any, Optional

from flask_fixture.state_storage.collection_of_importing_modules import modules


@dataclass
class RouteItem:
    """
    Storage of route signature.
    """
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    function: Callable[[...], Any]

    def __post_init__(self):
        modules.add(inspect.getmodule(self.function).__name__)

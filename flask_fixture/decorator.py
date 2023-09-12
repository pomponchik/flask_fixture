from typing import Any, Callable

from flask_fixture.route_item import RouteItem
from flask_fixture.collection_of_routes import routes
from flask_fixture.errors import NeedToDefineURLError


def endpoint(*args: Any, **kwargs: Any):
    def decorator(function):
        routes.append(
            RouteItem(
                args=args,
                kwargs=kwargs,
                function=function,
            )
        )
        return function
    return decorator

from typing import Protocol, Any


class QueueProtocol(Protocol):
    def put(self, item: Any) -> None:
        ...  # pragma: no cover

    def get(self) -> Any:
        ...  # pragma: no cover

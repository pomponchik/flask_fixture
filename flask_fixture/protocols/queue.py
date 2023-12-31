from typing import Any

try:
    from typing import Protocol
except ImportError:  # pragma: no cover
    from typing_extensions import Protocol  # type: ignore[assignment]


class QueueProtocol(Protocol):
    def put(self, item: Any) -> None:
        ...  # pragma: no cover

    def get(self) -> Any:
        ...  # pragma: no cover

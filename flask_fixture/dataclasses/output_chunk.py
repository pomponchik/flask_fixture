from enum import Enum
from dataclasses import dataclass
from typing import Any


class ChunkType(Enum):
    LOG_RECORD = 1
    STDOUT = 2
    STDERR = 3


@dataclass
class ProcessOutputChunk:
    type: ChunkType
    value: Any

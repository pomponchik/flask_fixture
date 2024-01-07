import logging

from flask_fixture.protocols.queue import QueueProtocol
from flask_fixture.dataclasses.output_chunk import ChunkType, ProcessOutputChunk


class QueueHandler(logging.Handler):
    def __init__(self, queue: QueueProtocol) -> None:
        logging.Handler.__init__(self)
        self.queue = queue

    def emit(self, record: logging.LogRecord) -> None:
        chunk: ProcessOutputChunk = ProcessOutputChunk(value=record, type=ChunkType.LOG_RECORD)
        self.queue.put(chunk)

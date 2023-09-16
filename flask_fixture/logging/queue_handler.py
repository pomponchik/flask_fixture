import logging
from multiprocessing import Queue

from flask_fixture.dataclasses.output_chunk import ChunkType, ProcessOutputChunk


class QueueHandler(logging.Handler):
    def __init__(self, queue: Queue):
        logging.Handler.__init__(self)
        self.queue = queue

    def emit(self, record: logging.LogRecord):
        chunk: ProcessOutputChunk = ProcessOutputChunk(value=record, type=ChunkType.LOG_RECORD)
        self.queue.put(chunk)

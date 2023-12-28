import sys
import logging
import traceback

from awaits import shoot
from cantok import AbstractToken, SimpleToken

from flask_fixture.protocols.queue import QueueProtocol
from flask_fixture.dataclasses.output_chunk import ChunkType, ProcessOutputChunk


@shoot
def listen_logs(queue: QueueProtocol, token: AbstractToken = SimpleToken()):
    while token:
        chunk: ProcessOutputChunk = queue.get()

        try:
            if chunk.type == ChunkType.LOG_RECORD:
                record: logging.LogRecord = chunk.value
                logging.root.handle(record)

            elif chunk.type == ChunkType.STDOUT:
                string: str = chunk.value
                print(string, end='')

            elif chunk.type == ChunkType.STDERR:
                string: str = chunk.value
                print(string, end='', file=sys.stderr)

        except Exception as e:
            print('Chunk processing error.', file=sys.stderr)
            traceback.print_exception(type(e), e, e.__traceback__)

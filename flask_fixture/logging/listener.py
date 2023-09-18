import sys
import logging
import traceback
import multiprocessing

from awaits import shoot

from flask_fixture.dataclasses.output_chunk import ChunkType, ProcessOutputChunk
from flask_fixture.utils.thread_context import ThreadContext


@shoot
def listen_logs(queue: multiprocessing.Queue, context: ThreadContext = ThreadContext()):
    while context.keep_on():
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
                print(string, end='')

        except Exception as e:
            print('Chang processing error.', file=sys.stderr)
            traceback.print_exception(type(e), e, e.__traceback__)

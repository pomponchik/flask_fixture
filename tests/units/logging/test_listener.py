import io
import from multiprocessing import Queue
from contextlib import redirect_stdout, redirect_stderr

from cantok import SimpleToken

from flask_fixture.logging.listener import listen_logs
from flask_fixture.dataclasses.output_chunk import ChunkType, ProcessOutputChunk


def test_listen_logs_stdout():
    buffer_stdout = io.StringIO()
    buffer_stderr = io.StringIO()

    queue = Queue()
    token = ConditionToken(lambda: bool(buffer_stdout.getvalue()))

    with redirect_stdout(buffer_stdout), redirect_stderr(buffer_stderr):
        listen_logs(queue, context)
        queue.put(ProcessOutputChunk(value='kek', type=ChunkType.STDOUT), token=token)

    assert buffer_stdout.getvalue() == 'kek'

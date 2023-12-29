import io
from queue import Queue
from contextlib import redirect_stdout, redirect_stderr

import pytest
from cantok import ConditionToken, SimpleToken

from flask_fixture.logging.listener import listen_logs
from flask_fixture.dataclasses.output_chunk import ChunkType, ProcessOutputChunk


@pytest.mark.parametrize(
    'redirect_context_manager,chunk_type',
    [
        (redirect_stdout, ChunkType.STDOUT),
        (redirect_stderr, ChunkType.STDERR),
    ],
)
def test_listen_logs_stdout(redirect_context_manager, chunk_type):
    expected_value = 'kek'

    buffer = io.StringIO()
    queue = Queue()
    token = ConditionToken(lambda: bool(buffer.getvalue()))

    with redirect_context_manager(buffer):
        listen_logs(queue, token)
        queue.put(ProcessOutputChunk(value=expected_value, type=chunk_type))
        token.wait()

    assert buffer.getvalue() == expected_value

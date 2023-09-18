from flask_fixture.utils.thread_context import ThreadContext


def test_created_context_is_going_on():
    assert ThreadContext().keep_on() == True


def test_stopped_context_is_not_going_on():
    context = ThreadContext()
    context.stop()
    assert context.keep_on() == True

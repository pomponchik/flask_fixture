class ThreadContext:
    def __init__(self):
        self.stopped = False

    def stop(self):
        self.stopped = True

    def keep_on(self):
        return not self.stopped

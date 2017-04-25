class LoggerTimer(Timer):
    @staticmethod
    def default_logger(msg):
        print msg

    def __init__(self, prefix='', func=None)
        # Use func if not None else the default one
        self.f = func or LoggerTimer.default_logger
        # Format the prefix if not None or empty, else use empty string
        self.prefix = '{0}:'.format(prefix) if prefix else ''

    def stop(self):
        # Call the parent method
        super(LoggerTimer, self).stop()
        # Call the logging function with the message
        self.f('{0}{1}'.format(self.prefix, self.interval))

    def __call__(self, func):
        # Use self as context manager in a decorated function
        def decorated_func(*args, **kwargs):
            with self: return func(*args, **kwargs)

        return decorated_func
from redis import Redis
from rq import Queue

from backend.src.helper.utils import SingletonMeta


class RedisConnector(metaclass=SingletonMeta):
    """Singleton class for Redis connection."""

    def __init__(self):
        """Initialize Redis connection."""
        self.connection = None
        self.high_queue = None
        self.default_queue = None
        self.low_queue = None
        self.queues = tuple()

    def connect(self, *args, **kwargs) -> "RedisConnector":
        """Connect to Redis and initialize queues.

        Parameters
        ----------
        *args
            Positional arguments for Redis connection.
        **kwargs
            Keyword arguments for Redis connection.

        Returns
        -------
        RedisConnector
            Instance of RedisConnector.
        """
        self.connection = Redis(*args, **kwargs)

        self.high_queue = Queue("high", connection=self.connection)
        self.default_queue = Queue("default", connection=self.connection)
        self.low_queue = Queue("low", connection=self.connection)

        self.queues = (self.high_queue, self.default_queue, self.low_queue)

        return self

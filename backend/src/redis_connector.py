from redis import Redis
from rq import Queue

from backend.src.helper.utils import SingletonMeta


class RedisConnector(metaclass=SingletonMeta):
    """Singleton class for Redis connection."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize Redis connection."""
        self.connection = Redis(*args, **kwargs)
        self.queues = dict()

    def update_queue(self, queue_name: str) -> "RedisConnector":
        """Add new queue to Redis connection or update existing one.

        Parameters
        ----------
        queue_name : str
            Name of new queue.
        """
        self.queues.update({queue_name: Queue(queue_name, connection=self.connection)})
        return self

    def update_connection(self, *args, **kwargs) -> "RedisConnector":
        """Update connection to Redis.

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
        return self

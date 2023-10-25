import time


def run_task(sleep: int) -> None:
    print("starting run_task")
    time.sleep(sleep)
    print("finished run_task")


def failed_task(num: int) -> float:
    time.sleep(2)
    return num / 0


class SingletonMeta(type):
    """The Singleton class can be implemented in different ways in Python.

    Some possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Possible changes to the value of the `__init__` argument do not affect the returned instance."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

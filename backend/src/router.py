from datetime import timedelta
from typing import Dict

from fastapi import APIRouter
from rq import Retry, registry

from backend.src.helper.utils import failed_task, run_task
from backend.src.redis_connector import RedisConnector


router = APIRouter()
redis_connector = RedisConnector()


@router.post("/start-default-task", status_code=201)
def start_default_task() -> None:
    """Add task to default queue."""
    redis_connector.queues["default"].enqueue(run_task, args=(10,))


@router.post("/start-scheduled-task", status_code=201)
def start_scheduled_task() -> None:
    """Add scheduled task to default queue."""
    redis_connector.queues["low"].enqueue_in(timedelta(seconds=20), run_task, args=(10,))


@router.post("/retry-failed-tasks", status_code=201)
def retry_failed_task() -> None:
    """Retry failed task."""
    redis_connector.queues["default"].enqueue(failed_task, 67, retry=Retry(max=3, interval=[3, 5, 7]))


@router.get("/queue-size", status_code=200)
def default_queue_size() -> Dict[str, int]:
    """Get the size of the default queue."""
    return {"Queue Size": len(redis_connector.queues["default"])}


@router.post("/empty-queues", status_code=200)
def empty_queues() -> None:
    """Empty all queues."""
    for queue in redis_connector.queues.keys():
        queue.empty()


@router.post("/empty-failed", status_code=200)
def empty_failed() -> None:
    """Empty all failed jobs."""
    for queue in redis_connector.queues.keys():
        failed_registry = registry.FailedJobRegistry(queue=queue)
        for job_id in failed_registry.get_job_ids():
            failed_registry.remove(job_id, delete_job=True)

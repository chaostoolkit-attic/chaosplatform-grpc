from datetime import datetime
from typing import Any, List, NoReturn
from uuid import UUID


import grpc
from grpc import Channel
import simplejson as json

from .scheduler_pb2_grpc import SchedulerServiceStub
from .message import Schedule, ScheduleRequest, ScheduleReply, \
    CancelRequest, CancelReply

__all__ = ["schedule_experiment", "cancel_experiment"]


def schedule_experiment(channel: Channel, schedule_id: UUID, user_id: UUID,
                        org_id: UUID, workspace_id: UUID, experiment_id: UUID,
                        token_id: UUID, token: str, scheduled: datetime,
                        experiment: Any, interval: int = None,
                        repeat: int = None, cron: str = None,
                        settings: Any = None, configuration: Any = None,
                        secrets: Any = None) -> str:
    """
    Schedule an experiment to be executed.
    """
    settings = json.dumps(settings) if settings is not None else None
    configuration = json.dumps(configuration) if \
        configuration is not None else None
    secrets = json.dumps(secrets) if secrets is not None else None
    experiment = json.dumps(experiment) if experiment is not None else None

    stub = SchedulerServiceStub(channel)
    response = stub.Schedule(ScheduleRequest(
        schedule=Schedule(
            schedule_id=str(schedule_id), user_id=str(user_id),
            org_id=str(org_id),
            workspace_id=str(workspace_id), experiment_id=str(experiment_id),
            token_id=str(token_id), token=token,
            scheduled="{}Z".format(scheduled.isoformat('T')),
            experiment=experiment, interval=interval, repeat=repeat, cron=cron,
            settings=settings, configuration=configuration, secrets=secrets)))
    return response.job_id


def cancel_experiment(channel: Channel, job_id: str) -> NoReturn:
    """
    Cancel an experiment's execution.
    """
    stub = SchedulerServiceStub(channel)
    stub.Cancel(CancelRequest(job_id=job_id))

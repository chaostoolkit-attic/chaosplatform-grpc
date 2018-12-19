from typing import NoReturn

import grpc
from grpc import Channel, Server

from .scheduler_pb2_grpc import add_SchedulerServiceServicer_to_server, \
    SchedulerServiceServicer
from .message import Schedule, ScheduleRequest, ScheduleReply, \
    CancelRequest, CancelReply

__all__ = ["SchedulerService", "register_scheduler_service"]


class SchedulerService(SchedulerServiceServicer):
    def Schedule(self, request: ScheduleRequest, context) -> ScheduleReply:
        schedule = request.schedule
        job_id = self.schedule(
            schedule.schedule_id, schedule.user_id, schedule.org_id,
            schedule.workspace_id, schedule.experiment_id, schedule.token_id,
            schedule.token, schedule.scheduled, schedule.experiment,
            schedule.interval, schedule.repeat, schedule.cron,
            schedule.settings, schedule.configuration, schedule.secrets
        )
        return ScheduleReply(job_id=job_id)

    def Cancel(self, request: CancelRequest, context) -> CancelReply:
        self.cancel(request.job_id)
        return CancelReply()

    def schedule(self, schedule_id: str, user_id: str, org_id: str,
                 workspace_id: str, experiment_id: str, token_id: str,
                 token: str, scheduled: str, experiment: str, interval: int,
                 repeat: int, cron: str, settings: str, configuration: str,
                 secrets: str) -> str:
        raise NotImplementedError()

    def cancel(self, job_id: str) -> NoReturn:
        raise NotImplementedError()


def register_scheduler_service(service: SchedulerService, server: Server):
    """
    Register a scheduler service with the provided gRPC server.
    """
    add_SchedulerServiceServicer_to_server(service, server)

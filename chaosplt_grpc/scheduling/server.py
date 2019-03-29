from typing import List

from grpc import Server

from .scheduling_pb2_grpc import add_SchedulingServiceServicer_to_server, \
    SchedulingServiceServicer
from .message import GetRequest, GetReply, GetManyRequest, GetManyReply, \
    Schedule, GetByUserRequest, GetByUserReply, GetByExperimentRequest, \
    GetByOrgRequest, GetByOrgReply, GetByWorkspaceRequest, \
    GetByWorkspaceReply, GetByExperimentReply

__all__ = ["SchedulingService", "register_scheduling_service"]


class SchedulingService(SchedulingServiceServicer):
    def Get(self, request: GetRequest, context) -> GetReply:
        schedule = self.get_scheduling(request.id, request.with_payload)
        return GetReply(schedule=schedule)

    def GetMany(self, request: GetManyRequest, context) -> GetManyReply:
        schedules = self.get_schedulings(request.ids, request.with_payload)
        return GetManyReply(schedules=schedules)

    def GetByUser(self, request: GetByUserRequest, context) -> GetByUserReply:
        schedules = self.get_by_user(request.user_id, request.with_payload)
        return GetByUserReply(schedules=schedules)

    def GetByOrg(self, request: GetByOrgRequest, context) -> GetByOrgReply:
        schedules = self.get_by_org(request.org_id, request.with_payload)
        return GetByOrgReply(schedules=schedules)

    def GetByWorkspace(self, request: GetByWorkspaceRequest,
                       context) -> GetByWorkspaceReply:
        schedules = self.get_by_workspace(
            request.workspace_id, request.with_payload)
        return GetByWorkspaceReply(schedules=schedules)

    def GetByExperiment(self, request: GetByExperimentRequest,
                        context) -> GetByExperimentReply:
        schedules = self.get_by_experiment(
            request.experiment_id, request.with_payload)
        return GetByExperimentReply(schedules=schedules)

    def get_scheduling(self, scheduling_id: str,
                       with_payload: bool = False) -> Schedule:
        raise NotImplementedError()

    def get_schedulings(self, scheduling_ids: List[str],
                        with_payload: bool = False) -> List[Schedule]:
        raise NotImplementedError()

    def get_by_user(self, user_id: str,
                    with_payload: bool = False) -> List[Schedule]:
        raise NotImplementedError()

    def get_by_org(self, org_id: str,
                   with_payload: bool = False) -> List[Schedule]:
        raise NotImplementedError()

    def get_by_workspace(self, workspace_id: str,
                         with_payload: bool = False) -> List[Schedule]:
        raise NotImplementedError()

    def get_by_experiment(self, experiment_id: str,
                          with_payload: bool = False) -> List[Schedule]:
        raise NotImplementedError()


def register_scheduling_service(service: SchedulingService, server: Server):
    """
    Register a scheduling service with the provided gRPC server.
    """
    add_SchedulingServiceServicer_to_server(service, server)

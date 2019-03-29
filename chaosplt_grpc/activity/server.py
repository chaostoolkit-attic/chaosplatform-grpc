from typing import Any, List

import grpc
from grpc import Channel, Server

from .activity_pb2_grpc import add_ActivityServiceServicer_to_server, \
    ActivityServiceServicer
from .message import Activity, RecordRequest, RecordReply, \
    GetByUserRequest, GetByUserReply, GetByOrgRequest, GetByOrgReply, \
    GetByWorkspaceRequest, GetByWorkspaceReply

__all__ = ["ActivityService", "register_activity_service"]


class ActivityService(ActivityServiceServicer):
    def Record(self, request: RecordRequest, context) -> RecordReply:
        activity_id = self.record_activity(
            authenticated_user_id=request.authenticated_user_id,
            access_token_id=request.access_token_id,
            user_id=request.user_id,
            org_id=request.org_id,
            workspace_id=request.workspace_id,
            experiment_id=request.experiment_id,
            execution_id=request.execution_id,
            timestamp=request.timestamp,
            kind=request.kind,
            visibility=request.visibility,
            title=request.title,
            description=request.description,
            payload=request.payload
        )
        return RecordReply(id=activity_id)

    def GetByUser(self, request: GetByUserRequest, context) -> GetByUserReply:
        activities = self.get_user_activities(
            request.user_id, request.limit, request.offset)
        return GetByUserReply(activities=activities)

    def GetByOrg(self, request: GetByOrgRequest, context) -> GetByOrgReply:
        activities = self.get_org_activities(
            request.org_id, request.limit, request.offset)
        return GetByOrgReply(activities=activities)

    def GetByWorkspace(self, request: GetByWorkspaceRequest,
                       context) -> GetByWorkspaceReply:
        activities = self.get_workspace_activities(
            request.workspace_id, request.limit, request.offset)
        return GetByWorkspaceReply(activities=activities)

    def record_activity(self, timestamp: str, kind: str, visibility: str,
                        user_id: str = None, authenticated_user_id: str = None,
                        access_token_id: str = None,
                        title: str = None, description: str = None,
                        org_id: str = None,
                        workspace_id: str = None, experiment_id: str = None,
                        execution_id: str = None, payload: Any = None) -> str:
        raise NotImplementedError()

    def get_user_activities(self, user_id: str, limit: int = 0,
                            offset: int = 0) -> List[Activity]:
        raise NotImplementedError()

    def get_org_activities(self, org_id: str, limit: int = 0,
                           offset: int = 0) -> List[Activity]:
        raise NotImplementedError()

    def get_workspace_activities(self, workspace_id: str, limit: int = 0,
                                 offset: int = 0) -> List[Activity]:
        raise NotImplementedError()


def register_activity_service(service: ActivityService, server: Server):
    """
    Register the given activity service with the provided gRPC server.
    """
    add_ActivityServiceServicer_to_server(service, server)

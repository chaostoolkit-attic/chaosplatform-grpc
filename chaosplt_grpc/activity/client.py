from typing import Any, List

from grpc import Channel

from .activity_pb2_grpc import ActivityServiceStub
from .message import Activity, RecordRequest, RecordReply, \
    GetByUserRequest, GetByUserReply, GetByOrgRequest, GetByOrgReply, \
    GetByWorkspaceRequest, GetByWorkspaceReply

__all__ = ["record_activity", "get_user_activities", "get_org_activities",
           "get_workspace_activities"]


def record_activity(channel: Channel, timestamp: str, event_type: str,
                    authenticated_user_id: str, phase: str,
                    access_token_id: str = None, user_id: str = None,
                    org_id: str = None, workspace_id: str = None,
                    experiment_id: str = None, execution_id: str = None,
                    payload: Any = None) -> str:
    """
    Record an activity
    """
    stub = ActivityServiceStub(channel)
    context = RecordRequest(
        authenticated_user_id=authenticated_user_id,
        access_token_id=access_token_id,
        user_id=user_id,
        org_id=org_id,
        workspace_id=workspace_id,
        experiment_id=experiment_id,
        execution_id=execution_id,
        event_type=event_type,
        timestamp=timestamp,
        phase=phase,
        payload=payload
    )
    response = stub.Record(context)
    return response.id


def get_user_activities(channel: Channel, user_id: str, limit: int = 0,
                        offset: int = 0) -> List[Activity]:
    stub = ActivityServiceStub(channel)
    context = GetByUserRequest(user_id=user_id, limit=limit, offset=offset)
    response = stub.GetByUser(context)
    return response.activities


def get_org_activities(channel: Channel, org_id: str, limit: int = 0,
                       offset: int = 0) -> List[Activity]:
    stub = ActivityServiceStub(channel)
    context = GetByOrgRequest(org_id=org_id, limit=limit, offset=offset)
    response = stub.GetByOrg(context)
    return response.activities


def get_workspace_activities(channel: Channel, workspace_id: str,
                             limit: int = 0,
                             offset: int = 0) -> List[Activity]:
    stub = ActivityServiceStub(channel)
    context = GetByWorkspaceRequest(
        workspace_id=workspace_id, limit=limit, offset=offset)
    response = stub.GetByWorkspace(context)
    return response.activities

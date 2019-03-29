from typing import List

from grpc import Channel

from .scheduling_pb2_grpc import SchedulingServiceStub
from .message import Schedule, GetRequest, GetManyRequest, \
    GetByUserRequest, GetByOrgRequest, GetByWorkspaceRequest, \
    GetByExperimentRequest

__all__ = ["get_scheduling", "get_schedulings", "get_by_user",
           "get_by_org", "get_by_workspace", "get_by_experiment"]


def get_scheduling(channel: Channel, scheduling_id: str,
                   with_payload: bool = False) -> Schedule:
    """
    Get an execution
    """
    stub = SchedulingServiceStub(channel)
    response = stub.Get(
        GetRequest(id=scheduling_id, with_payload=with_payload))
    return response.workspace


def get_schedulings(channel: Channel, scheduling_ids: List[str],
                    with_payload: bool = False) -> List[Schedule]:
    """
    Get many executions
    """
    stub = SchedulingServiceStub(channel)
    response = stub.GetMany(
        GetManyRequest(ids=scheduling_ids, with_payload=with_payload))
    return response.workspaces


def get_by_user(channel: Channel, user_id: str,
                with_payload: bool = False) -> List[Schedule]:
    """
    Get schedulings of an user
    """
    stub = SchedulingServiceStub(channel)
    response = stub.GetByUser(
        GetByUserRequest(user_id=user_id, with_payload=with_payload))
    return response.schedules


def get_by_org(channel: Channel, org_id: str,
               with_payload: bool = False) -> List[Schedule]:
    """
    Get schedulings of an organization
    """
    stub = SchedulingServiceStub(channel)
    response = stub.GetByOrg(
        GetByOrgRequest(org_id=org_id, with_payload=with_payload))
    return response.schedules


def get_by_workspace(channel: Channel, workspace_id: str,
                     with_payload: bool = False) -> List[Schedule]:
    """
    Get schedulings of a workspace
    """
    stub = SchedulingServiceStub(channel)
    response = stub.GetByWorkspace(
        GetByWorkspaceRequest(
            workspace_id=workspace_id, with_payload=with_payload))
    return response.schedules


def get_by_experiment(channel: Channel, experiment_id: str,
                      with_payload: bool = False) -> List[Schedule]:
    """
    Get schedulings of an experiment
    """
    stub = SchedulingServiceStub(channel)
    response = stub.GetByExperiment(
        GetByExperimentRequest(
            experiment_id=experiment_id, with_payload=with_payload))
    return response.schedules

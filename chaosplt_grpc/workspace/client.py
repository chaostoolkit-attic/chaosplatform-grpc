from typing import List, NoReturn

import grpc
from grpc import Channel

from .workspace_pb2_grpc import WorkspaceServiceStub
from .message import CreateRequest, GetByUserRequest, Workspace, \
    DeleteRequest

__all__ = ["create_workspace", "delete_workspace", "get_workspaces_for_user"]


def create_workspace(channel: Channel, name: str, user_id: str) -> Workspace:
    """
    Create a workspace.
    """
    stub = WorkspaceServiceStub(channel)
    response = stub.Create(CreateRequest(name=name, user_id=user_id))
    return response.workspace


def delete_workspace(channel: Channel, workspace_id: str) -> NoReturn:
    """
    Delete a workspace.
    """
    stub = WorkspaceServiceStub(channel)
    stub.Delete(DeleteRequest(id=workspace_id))


def get_workspaces_for_user(channel: Channel, user_id: str) -> List[Workspace]:
    """
    Get all workspaces of a given user.
    """
    stub = WorkspaceServiceStub(channel)
    response = stub.ByUser(GetByUserRequest(user_id=user_id))
    return response.workspaces

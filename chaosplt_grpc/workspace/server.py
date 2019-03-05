from typing import List, NoReturn

import grpc
from grpc import Channel, Server

from .workspace_pb2_grpc import add_WorkspaceServiceServicer_to_server, \
    WorkspaceServiceServicer
from .message import CreateRequest, CreateReply, DeleteRequest, DeleteReply, \
    GetByUserRequest, GetByUserReply, Workspace, GetRequest, GetReply, \
    GetManyRequest, GetManyReply

__all__ = ["WorkspaceService", "register_workspace_service"]


class WorkspaceService(WorkspaceServiceServicer):
    def Create(self, request: CreateRequest, context) -> CreateReply:
        workspace = self.create_workspace(
            request.user_id, request.org_id, request.name)
        return CreateReply(workspace=workspace)

    def Delete(self, request: DeleteRequest, context) -> DeleteReply:
        self.delete_workspace(request.id)
        return DeleteReply()

    def ByUser(self, request: GetByUserRequest, context) -> GetByUserReply:
        workspaces = self.get_workspaces_for_user(request.user_id)
        return GetByUserReply(workspaces=workspaces)

    def Get(self, request: GetRequest, context) -> GetReply:
        workspace = self.get_workspace(request.id)
        return GetReply(workspace=workspace)

    def GetMany(self, request: GetManyRequest, context) -> GetManyReply:
        workspaces = self.get_workspaces(request.ids)
        return GetManyReply(workspaces=workspaces)

    def delete_workspace(self, workspace_id: str) -> NoReturn:
        raise NotImplementedError()

    def create_workspace(self, user_id: str, org_id: str,
                         name: str) -> Workspace:
        raise NotImplementedError()

    def get_workspace(self, workspace_id: str) -> Workspace:
        raise NotImplementedError()

    def get_workspaces(self, workspace_ids: List[str]) -> List[Workspace]:
        raise NotImplementedError()

    def get_workspaces_for_user(self, user_id: str) -> List[Workspace]:
        raise NotImplementedError()


def register_workspace_service(service: WorkspaceService, server: Server):
    """
    Register a workspace service with the provided gRPC server.
    """
    add_WorkspaceServiceServicer_to_server(service, server)

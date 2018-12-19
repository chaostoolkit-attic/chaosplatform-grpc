from typing import List, NoReturn

import grpc
from grpc import Channel, Server

from .workspace_pb2_grpc import add_WorkspaceServiceServicer_to_server, \
    WorkspaceServiceServicer
from .message import CreateRequest, CreateReply, DeleteRequest, DeleteReply, \
    GetByUserRequest, GetByUserReply, Workspace

__all__ = ["WorkspaceService", "register_workspace_service"]


class WorkspaceService(WorkspaceServiceServicer):
    def Create(self, request: CreateRequest, context) -> CreateReply:
        workspace = self.create_workspace(request.name, request.user_id)
        return CreateReply(workspace=workspace)

    def Delete(self, request: DeleteRequest, context) -> DeleteReply:
        self.delete_workspace(request.id)
        return DeleteReply()

    def ByUser(self, request: GetByUserRequest, context) -> GetByUserReply:
        workspaces = self.get_workspace_for_user(request.user_id)
        return GetByUserReply(workspaces=workspaces)

    def delete_workspace(self, user_id: str, name: str) -> NoReturn:
        raise NotImplementedError()

    def create_workspace(self, user_id: str, name: str) -> Workspace:
        raise NotImplementedError()

    def get_workspace_for_user(self, user_id: str) -> List[Workspace]:
        raise NotImplementedError()


def register_workspace_service(service: WorkspaceService, server: Server):
    """
    Register a workspace service with the provided gRPC server.
    """
    add_WorkspaceServiceServicer_to_server(service, server)

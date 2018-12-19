from typing import List, NoReturn

import grpc
from grpc import Channel, Server

from .user_pb2_grpc import add_UserServiceServicer_to_server, \
    UserServiceServicer
from .message import CreateRequest, CreateReply, DeleteRequest, DeleteReply, \
    User

__all__ = ["UserService", "register_user_service"]


class UserService(UserServiceServicer):
    def Create(self, request: CreateRequest, context) -> CreateReply:
        user = self.create_user(request.username, request.user_id)
        return CreateReply(user=user)

    def Delete(self, request: DeleteRequest, context) -> DeleteReply:
        self.delete_user(request.id)
        return DeleteReply()

    def create_user(self, user_id: str, name: str) -> User:
        raise NotImplementedError()

    def delete_user(self, user_id: str) -> NoReturn:
        raise NotImplementedError()


def register_user_service(service: UserService, server: Server):
    """
    Register a user service with the provided gRPC server.
    """
    add_UserServiceServicer_to_server(service, server)

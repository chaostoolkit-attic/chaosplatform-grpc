from typing import NoReturn

import grpc
from grpc import Channel, Server

from .auth_pb2_grpc import add_AuthServiceServicer_to_server, \
    AuthServiceServicer
from .message import AccessToken, CreateRequest, CreateReply, \
    DeleteRequest, DeleteReply

__all__ = ["AuthService", "register_auth_service"]


class AuthService(AuthServiceServicer):
    def Create(self, request: CreateRequest, context) -> CreateReply:
        token = self.create_access_token(request.user_id, request.name)
        return CreateReply(token=token)

    def Delete(self, request: DeleteRequest, context) -> DeleteReply:
        self.delete_access_token(request.token_id)
        return DeleteReply()

    def create_access_token(self, user_id: str, name: str) -> AccessToken:
        raise NotImplementedError()

    def delete_access_token(self, token_id: str) -> NoReturn:
        raise NotImplementedError()


def register_auth_service(service: AuthService, server: Server):
    """
    Register the given authentication service with the provided gRPC server.
    """
    add_AuthServiceServicer_to_server(service, server)

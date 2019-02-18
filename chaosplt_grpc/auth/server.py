from typing import List, NoReturn

import grpc
from grpc import Channel, Server

from .auth_pb2_grpc import add_AuthServiceServicer_to_server, \
    AuthServiceServicer
from .message import AccessToken, CreateRequest, CreateReply, \
    DeleteRequest, DeleteReply, GetRequest, GetReply, GetByNameRequest, \
    GetByNameReply, GetByUserRequest, GetByUserReply, RevokeRequest, \
    RevokeReply, GetByJtiRequest, GetByJtiReply

__all__ = ["AuthService", "register_auth_service"]


class AuthService(AuthServiceServicer):
    def Create(self, request: CreateRequest, context) -> CreateReply:
        token = self.create_access_token(request.user_id, request.name)
        return CreateReply(token=token)

    def Delete(self, request: DeleteRequest, context) -> DeleteReply:
        self.delete_access_token(request.user_id, request.id)
        return DeleteReply()

    def Revoke(self, request: RevokeRequest, context) -> DeleteReply:
        self.revoke_access_token(request.user_id, request.id)
        return RevokeReply()

    def GetByUser(self, request: GetRequest, context) -> GetReply:
        token = self.get(request.id)
        return GetReply(token=token)

    def GetByName(self, request: GetByNameRequest, context) -> GetByNameReply:
        token = self.get_by_name(request.user_id, request.name)
        return GetByNameReply(token=token)

    def GetByUser(self, request: GetByUserRequest, context) -> GetByUserReply:
        tokens = self.get_by_user(request.user_id)
        return GetByUserReply(tokens=tokens)

    def GetByJti(self, request: GetByJtiRequest, context) -> GetByJtiReply:
        tokens = self.get_by_jti(request.user_id, request.jti)
        return GetByJtiReply(tokens=tokens)

    def create_access_token(self, user_id: str, name: str) -> AccessToken:
        raise NotImplementedError()

    def delete_access_token(self, user_id: str, token_id: str) -> NoReturn:
        raise NotImplementedError()

    def revoke_access_token(self, user_id: str, token_id: str) -> NoReturn:
        raise NotImplementedError()

    def get_by_name(self, user_id: str, name: str) -> AccessToken:
        raise NotImplementedError()

    def get_by_user(self, user_id: str) -> List[AccessToken]:
        raise NotImplementedError()

    def get_by_jti(self, user_id: str, jti: str) -> AccessToken:
        raise NotImplementedError()

    def get(self, token_id: str) -> AccessToken:
        raise NotImplementedError()


def register_auth_service(service: AuthService, server: Server):
    """
    Register the given authentication service with the provided gRPC server.
    """
    add_AuthServiceServicer_to_server(service, server)

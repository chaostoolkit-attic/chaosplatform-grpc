from typing import NoReturn

import grpc
from grpc import Channel, Server

from .registration_pb2_grpc import RegistrationServiceServicer, \
    add_RegistrationServiceServicer_to_server
from .message import Registration, CreateRequest, CreateReply, DeleteRequest, \
    DeleteReply, GetByIdRequest, GetByIdReply

__all__ = ["RegistrationService", "register_registration_service"]


class RegistrationService(RegistrationServiceServicer):
    def Create(self, request: CreateRequest, context) -> CreateReply:
        registration = self.create_registration(
            request.username, request.name, request.email)
        return CreateReply(registration=registration)

    def Delete(self, request: DeleteRequest, context) -> DeleteReply:
        self.delete_registration(request.id)
        return DeleteReply()

    def GetById(self, request: GetByIdRequest, context) -> GetByIdReply:
        registration = self.get_by_id(request.id)
        return GetByIdReply(registration=registration)

    def create_registration(self, user_id: str, username: str, name: str,
                            email: str) -> Registration:
        raise NotImplementedError()

    def delete_registration(self, registration_id: str) -> NoReturn:
        raise NotImplementedError()

    def get_by_id(self, registration_id: str) -> Registration:
        raise NotImplementedError()


def register_registration_service(service: RegistrationService,
                                  server: Server):
    """
    Register a registraytion service with the provided gRPC server.
    """
    add_RegistrationServiceServicer_to_server(service, server)

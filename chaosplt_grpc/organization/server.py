from typing import List, NoReturn

import grpc
from grpc import Channel, Server

from .organization_pb2_grpc import add_OrganizationServiceServicer_to_server, \
    OrganizationServiceServicer
from .message import CreateRequest, CreateReply, DeleteRequest, DeleteReply, \
    GetByUserRequest, GetByUserReply, Organization

__all__ = ["OrganizationService", "register_organization_service"]


class OrganizationService(OrganizationServiceServicer):
    def Create(self, request: CreateRequest, context) -> CreateReply:
        org = self.create_organization(request.name, request.user_id)
        return CreateReply(org=org)

    def Delete(self, request: DeleteRequest, context) -> DeleteReply:
        self.delete_organization(request.id)
        return DeleteReply()

    def ByUser(self, request: GetByUserRequest, context) -> GetByUserReply:
        orgs = self.get_organization_for_user(request.user_id)
        return GetByUserReply(organizations=orgs)

    def delete_organization(self, user_id: str, name: str) -> NoReturn:
        raise NotImplementedError()

    def create_organization(self, user_id: str, name: str) -> Organization:
        raise NotImplementedError()

    def get_organization_for_user(self, user_id: str) -> List[Organization]:
        raise NotImplementedError()


def register_organization_service(service: OrganizationService,
                                  server: Server):
    """
    Register an organization service with the provided gRPC server.
    """
    add_OrganizationServiceServicer_to_server(service, server)

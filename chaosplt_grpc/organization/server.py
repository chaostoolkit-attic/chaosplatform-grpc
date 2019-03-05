from typing import List, NoReturn

from grpc import Server

from .organization_pb2_grpc import add_OrganizationServiceServicer_to_server, \
    OrganizationServiceServicer
from .message import CreateRequest, CreateReply, DeleteRequest, DeleteReply, \
    GetByUserRequest, GetByUserReply, Organization, GetRequest, GetReply, \
    GetManyRequest, GetManyReply

__all__ = ["OrganizationService", "register_organization_service"]


class OrganizationService(OrganizationServiceServicer):
    def Create(self, request: CreateRequest, context) -> CreateReply:
        org = self.create_organization(request.name, request.user_id)
        return CreateReply(org=org)

    def Delete(self, request: DeleteRequest, context) -> DeleteReply:
        self.delete_organization(request.id)
        return DeleteReply()

    def ByUser(self, request: GetByUserRequest, context) -> GetByUserReply:
        orgs = self.get_organizations_for_user(request.user_id)
        return GetByUserReply(organizations=orgs)

    def Get(self, request: GetRequest, context) -> GetReply:
        org = self.get_organization(request.id)
        return GetReply(org=org)

    def GetMany(self, request: GetManyRequest, context) -> GetManyReply:
        orgs = self.get_organizations(request.ids)
        return GetManyReply(orgs=orgs)

    def delete_organization(self, user_id: str, name: str) -> NoReturn:
        raise NotImplementedError()

    def create_organization(self, user_id: str, name: str) -> Organization:
        raise NotImplementedError()

    def get_organization_for_user(self, user_id: str) -> List[Organization]:
        raise NotImplementedError()

    def get_organization(self, org_id: str) -> Organization:
        raise NotImplementedError()

    def get_organizations(self, org_ids: List[str]) -> List[Organization]:
        raise NotImplementedError()


def register_organization_service(service: OrganizationService,
                                  server: Server):
    """
    Register an organization service with the provided gRPC server.
    """
    add_OrganizationServiceServicer_to_server(service, server)

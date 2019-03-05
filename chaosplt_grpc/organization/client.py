from typing import List, NoReturn

import grpc
from grpc import Channel

from .organization_pb2_grpc import OrganizationServiceStub
from .message import CreateRequest, GetByUserRequest, Organization, \
    DeleteRequest, GetRequest, GetManyRequest

__all__ = ["create_organization", "delete_organization", "get_organization",
           "get_organizations_for_user", "get_organizations"]


def create_organization(channel: Channel, name: str,
                        user_id: str) -> Organization:
    """
    Create an organization.
    """
    stub = OrganizationServiceStub(channel)
    response = stub.Create(CreateRequest(name=name, user_id=user_id))
    return response.organization


def delete_organization(channel: Channel, org_id: str) -> NoReturn:
    """
    Delete an organization.
    """
    stub = OrganizationServiceStub(channel)
    stub.Delete(DeleteRequest(id=org_id))


def get_organizations_for_user(channel: Channel,
                               user_id: str) -> List[Organization]:
    """
    Get all organizations of a given user.
    """
    stub = OrganizationServiceStub(channel)
    response = stub.ByUser(GetByUserRequest(user_id=user_id))
    return response.organizations


def get_organization(channel: Channel, org_id: str) -> List[Organization]:
    """
    Get an organization
    """
    stub = OrganizationServiceStub(channel)
    response = stub.Get(GetRequest(id=org_id))
    return response.workspace


def get_organizations(channel: Channel,
                      org_ids: List[str]) -> List[Organization]:
    """
    Get many organizations
    """
    stub = OrganizationServiceStub(channel)
    response = stub.GetMany(GetManyRequest(ids=org_ids))
    return response.workspaces

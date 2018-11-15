from typing import NoReturn

import grpc
from grpc import Channel

from .registration_pb2_grpc import RegistrationServiceStub
from .message import Registration, CreateRequest, CreateReply, DeleteRequest, \
    DeleteReply, GetByIdRequest, GetByIdReply

__all__ = ["create_registration", "delete_registration", "get_by_id"]


def create_registration(channel: Channel, username: str, name: str,
                        email: str) -> Registration:
    """
    Register a new user.
    """
    stub = RegistrationServiceStub(channel)
    response = stub.Create(CreateRequest(
        username=username, name=name, email=email))
    return response.registration


def delete_registration(channel: Channel, registration_id: str) -> NoReturn:
    """
    Delete a user.
    """
    stub = RegistrationServiceStub(channel)
    stub.Delete(DeleteRequest(registration_id=registration_id))


def get_by_id(channel: Channel, registration_id: str) -> Registration:
    """
    Fetch the registration.
    """
    stub = RegistrationServiceStub(channel)
    response = stub.GetById(GetByIdRequest(id=registration_id))
    return response.registration

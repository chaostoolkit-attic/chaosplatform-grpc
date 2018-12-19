from typing import List, NoReturn

import grpc
from grpc import Channel

from .user_pb2_grpc import UserServiceStub
from .message import CreateRequest, DeleteRequest, User

__all__ = ["create_user", "delete_user"]


def create_user(channel: Channel, username: str) -> User:
    """
    Create a user.
    """
    stub = UserServiceStub(channel)
    response = stub.Create(CreateRequest(username=username))
    return response.user


def delete_user(channel: Channel, user_id: str) -> NoReturn:
    """
    Delete a user.
    """
    stub = UserServiceStub(channel)
    stub.Delete(DeleteRequest(id=user_id))

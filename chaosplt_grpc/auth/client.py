from typing import NoReturn

import grpc
from grpc import Channel

from .auth_pb2_grpc import AuthServiceStub
from .message import AccessToken, CreateRequest, CreateReply, \
    DeleteRequest, DeleteReply

__all__ = ["create_access_token", "save_access_token", "remove_access_token"]


def create_access_token(channel: Channel, user_id: str,
                        name: str) -> AccessToken:
    """
    Create an access token.
    """
    stub = AuthServiceStub(channel)
    context = CreateRequest(user_id=user_id, name=name)
    response = stub.Create(context)
    return response.token


def save_access_token(channel: Channel, name: str, user_id: str,
                      access_token: str, refresh_token: str) -> str:
    """
    Store the access token and return its identifier
    """
    stub = AuthServiceStub(channel)
    data = CreateRequest(
        name=name, user_id=user_id, access_token=access_token,
        refresh_token=refresh_token)
    response = stub.Save(data)
    return response.id


def remove_access_token(channel: Channel, token_id: str) -> NoReturn:
    """
    Remove the token from the storage.
    """
    stub = AuthServiceStub(channel)
    stub.Remove(DeleteRequest(id=token_id))

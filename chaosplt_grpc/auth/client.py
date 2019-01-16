from typing import List, NoReturn

import grpc
from grpc import Channel

from .auth_pb2_grpc import AuthServiceStub
from .message import AccessToken, CreateRequest, CreateReply, \
    DeleteRequest, DeleteReply, GetRequest, GetReply, GetByNameRequest, \
    GetByNameReply, GetByUserRequest, GetByUserReply

__all__ = ["create_access_token", "remove_access_token", "get_access_token",
           "get_access_token_by_name", "get_access_tokens_by_user"]


def create_access_token(channel: Channel, user_id: str,
                        name: str) -> AccessToken:
    """
    Create an access token.
    """
    stub = AuthServiceStub(channel)
    context = CreateRequest(user_id=user_id, name=name)
    response = stub.Create(context)
    return response.token


def remove_access_token(channel: Channel, user_id: str,
                        token_id: str) -> NoReturn:
    """
    Remove the token from the storage.
    """
    stub = AuthServiceStub(channel)
    stub.Remove(DeleteRequest(id=token_id, user_id=user_id))


def get_access_token_by_name(channel, user_id: str, name: str) -> AccessToken:
    """
    Get the token by name for a given user
    """
    stub = AuthServiceStub(channel)
    response = stub.GetByName(name=name, user_id=user_id)
    return response.token


def get_access_tokens_by_user(channel, user_id: str) -> List[AccessToken]:
    """
    Get all tokens of a given user
    """
    stub = AuthServiceStub(channel)
    response = stub.GetByUser(user_id=user_id)
    return response.tokens


def get_access_token(channel, token_id: str) -> AccessToken:
    """
    Get an access token
    """
    stub = AuthServiceStub(channel)
    response = stub.Get(token_id=token_id)
    return response.token

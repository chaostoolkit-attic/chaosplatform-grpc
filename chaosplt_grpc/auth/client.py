from typing import List, NoReturn

import grpc
from grpc import Channel

from .auth_pb2_grpc import AuthServiceStub
from .message import AccessToken, CreateRequest, CreateReply, \
    DeleteRequest, DeleteReply, GetRequest, GetReply, GetByNameRequest, \
    GetByNameReply, GetByUserRequest, GetByUserReply, RevokeRequest, \
    RevokeReply, GetByJtiRequest, GetByJtiReply, GetByWorkspaceRequest, \
    GetByOrgRequest

__all__ = ["create_access_token", "remove_access_token", "get_access_token",
           "get_access_token_by_name", "get_access_tokens_by_user",
           "revoke_access_token", "get_access_token_by_jti", "get_by_org",
           "get_by_workspace"]


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


def revoke_access_token(channel: Channel, user_id: str,
                        token_id: str) -> NoReturn:
    """
    Revoke the token.
    """
    stub = AuthServiceStub(channel)
    stub.Remove(RevokeRequest(id=token_id, user_id=user_id))


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


def get_access_token_by_jti(channel, user_id: str, jti: str) -> AccessToken:
    """
    Get a token by its jti
    """
    stub = AuthServiceStub(channel)
    response = stub.GetByJti(user_id=user_id, jti=jti)
    return response.token


def get_by_org(channel, org_id: str) -> List[AccessToken]:
    """
    Get all tokens for an organization
    """
    stub = AuthServiceStub(channel)
    response = stub.GetByOrg(org_id=org_id)
    return response.tokens


def get_by_workspace(channel, workspace_id: str) -> List[AccessToken]:
    """
    Get all tokens for an organization
    """
    stub = AuthServiceStub(channel)
    response = stub.GetByWorkspace(workspace_id=workspace_id)
    return response.tokens

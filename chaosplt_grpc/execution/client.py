from typing import List

from grpc import Channel

from .execution_pb2_grpc import ExecutionServiceStub
from .message import Execution, GetRequest, GetManyRequest

__all__ = ["get_execution", "get_executions"]


def get_execution(channel: Channel, execution_id: str,
                  with_payload: bool = False) -> Execution:
    """
    Get an execution
    """
    stub = ExecutionServiceStub(channel)
    response = stub.Get(
        GetRequest(id=execution_id, with_payload=with_payload))
    return response.workspace


def get_executions(channel: Channel, execution_ids: List[str],
                   with_payload: bool = False) -> List[Execution]:
    """
    Get many executions
    """
    stub = ExecutionServiceStub(channel)
    response = stub.GetMany(
        GetManyRequest(ids=execution_ids, with_payload=with_payload))
    return response.workspaces

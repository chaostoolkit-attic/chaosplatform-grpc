from typing import List

from grpc import Server

from .execution_pb2_grpc import add_ExecutionServiceServicer_to_server, \
    ExecutionServiceServicer
from .message import GetRequest, GetReply, GetManyRequest, GetManyReply, \
    Execution

__all__ = ["ExecutionService", "register_execution_service"]


class ExecutionService(ExecutionServiceServicer):
    def Get(self, request: GetRequest, context) -> GetReply:
        execution = self.get_execution(request.id, request.with_payload)
        return GetReply(execution=execution)

    def GetMany(self, request: GetManyRequest, context) -> GetManyReply:
        executions = self.get_executions(request.ids, request.with_payload)
        return GetManyReply(executions=executions)

    def get_execution(self, execution_id: str,
                      with_payload: bool = False) -> Execution:
        raise NotImplementedError()

    def get_executions(self, execution_ids: List[str],
                       with_payload: bool = False) -> List[Execution]:
        raise NotImplementedError()


def register_execution_service(service: ExecutionService, server: Server):
    """
    Register an execution service with the provided gRPC server.
    """
    add_ExecutionServiceServicer_to_server(service, server)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import workspace_pb2 as workspace_dot_workspace__pb2


class WorkspaceServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/chaoshub.workspace.WorkspaceService/Create',
        request_serializer=workspace_dot_workspace__pb2.CreateRequest.SerializeToString,
        response_deserializer=workspace_dot_workspace__pb2.CreateReply.FromString,
        )
    self.Delete = channel.unary_unary(
        '/chaoshub.workspace.WorkspaceService/Delete',
        request_serializer=workspace_dot_workspace__pb2.TerminateRequest.SerializeToString,
        response_deserializer=workspace_dot_workspace__pb2.TerminateReply.FromString,
        )
    self.ByUser = channel.unary_unary(
        '/chaoshub.workspace.WorkspaceService/ByUser',
        request_serializer=workspace_dot_workspace__pb2.GetByUserRequest.SerializeToString,
        response_deserializer=workspace_dot_workspace__pb2.GetByUserReply.FromString,
        )


class WorkspaceServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ByUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WorkspaceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=workspace_dot_workspace__pb2.CreateRequest.FromString,
          response_serializer=workspace_dot_workspace__pb2.CreateReply.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=workspace_dot_workspace__pb2.TerminateRequest.FromString,
          response_serializer=workspace_dot_workspace__pb2.TerminateReply.SerializeToString,
      ),
      'ByUser': grpc.unary_unary_rpc_method_handler(
          servicer.ByUser,
          request_deserializer=workspace_dot_workspace__pb2.GetByUserRequest.FromString,
          response_serializer=workspace_dot_workspace__pb2.GetByUserReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'chaoshub.workspace.WorkspaceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

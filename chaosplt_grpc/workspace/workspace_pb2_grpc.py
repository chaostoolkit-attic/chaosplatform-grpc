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
        '/chaosplatform.workspace.WorkspaceService/Create',
        request_serializer=workspace_dot_workspace__pb2.CreateRequest.SerializeToString,
        response_deserializer=workspace_dot_workspace__pb2.CreateReply.FromString,
        )
    self.Get = channel.unary_unary(
        '/chaosplatform.workspace.WorkspaceService/Get',
        request_serializer=workspace_dot_workspace__pb2.GetRequest.SerializeToString,
        response_deserializer=workspace_dot_workspace__pb2.GetReply.FromString,
        )
    self.GetMany = channel.unary_unary(
        '/chaosplatform.workspace.WorkspaceService/GetMany',
        request_serializer=workspace_dot_workspace__pb2.GetManyRequest.SerializeToString,
        response_deserializer=workspace_dot_workspace__pb2.GetManyReply.FromString,
        )
    self.Delete = channel.unary_unary(
        '/chaosplatform.workspace.WorkspaceService/Delete',
        request_serializer=workspace_dot_workspace__pb2.DeleteRequest.SerializeToString,
        response_deserializer=workspace_dot_workspace__pb2.DeleteReply.FromString,
        )
    self.ByUser = channel.unary_unary(
        '/chaosplatform.workspace.WorkspaceService/ByUser',
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

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMany(self, request, context):
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
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=workspace_dot_workspace__pb2.GetRequest.FromString,
          response_serializer=workspace_dot_workspace__pb2.GetReply.SerializeToString,
      ),
      'GetMany': grpc.unary_unary_rpc_method_handler(
          servicer.GetMany,
          request_deserializer=workspace_dot_workspace__pb2.GetManyRequest.FromString,
          response_serializer=workspace_dot_workspace__pb2.GetManyReply.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=workspace_dot_workspace__pb2.DeleteRequest.FromString,
          response_serializer=workspace_dot_workspace__pb2.DeleteReply.SerializeToString,
      ),
      'ByUser': grpc.unary_unary_rpc_method_handler(
          servicer.ByUser,
          request_deserializer=workspace_dot_workspace__pb2.GetByUserRequest.FromString,
          response_serializer=workspace_dot_workspace__pb2.GetByUserReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'chaosplatform.workspace.WorkspaceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

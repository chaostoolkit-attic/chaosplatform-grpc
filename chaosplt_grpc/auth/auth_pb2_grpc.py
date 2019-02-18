# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import auth_pb2 as auth_dot_auth__pb2


class AuthServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/chaosplatform.auth.AuthService/Create',
        request_serializer=auth_dot_auth__pb2.CreateRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.CreateReply.FromString,
        )
    self.Delete = channel.unary_unary(
        '/chaosplatform.auth.AuthService/Delete',
        request_serializer=auth_dot_auth__pb2.DeleteRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.DeleteReply.FromString,
        )
    self.Revoke = channel.unary_unary(
        '/chaosplatform.auth.AuthService/Revoke',
        request_serializer=auth_dot_auth__pb2.RevokeRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.RevokeReply.FromString,
        )
    self.Get = channel.unary_unary(
        '/chaosplatform.auth.AuthService/Get',
        request_serializer=auth_dot_auth__pb2.GetRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.GetReply.FromString,
        )
    self.GetByName = channel.unary_unary(
        '/chaosplatform.auth.AuthService/GetByName',
        request_serializer=auth_dot_auth__pb2.GetByNameRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.GetByNameReply.FromString,
        )
    self.GetByUser = channel.unary_unary(
        '/chaosplatform.auth.AuthService/GetByUser',
        request_serializer=auth_dot_auth__pb2.GetByUserRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.GetByUserReply.FromString,
        )
    self.GetByJti = channel.unary_unary(
        '/chaosplatform.auth.AuthService/GetByJti',
        request_serializer=auth_dot_auth__pb2.GetByJtiRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.GetByJtiReply.FromString,
        )


class AuthServiceServicer(object):
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

  def Revoke(self, request, context):
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

  def GetByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetByUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetByJti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=auth_dot_auth__pb2.CreateRequest.FromString,
          response_serializer=auth_dot_auth__pb2.CreateReply.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=auth_dot_auth__pb2.DeleteRequest.FromString,
          response_serializer=auth_dot_auth__pb2.DeleteReply.SerializeToString,
      ),
      'Revoke': grpc.unary_unary_rpc_method_handler(
          servicer.Revoke,
          request_deserializer=auth_dot_auth__pb2.RevokeRequest.FromString,
          response_serializer=auth_dot_auth__pb2.RevokeReply.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=auth_dot_auth__pb2.GetRequest.FromString,
          response_serializer=auth_dot_auth__pb2.GetReply.SerializeToString,
      ),
      'GetByName': grpc.unary_unary_rpc_method_handler(
          servicer.GetByName,
          request_deserializer=auth_dot_auth__pb2.GetByNameRequest.FromString,
          response_serializer=auth_dot_auth__pb2.GetByNameReply.SerializeToString,
      ),
      'GetByUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetByUser,
          request_deserializer=auth_dot_auth__pb2.GetByUserRequest.FromString,
          response_serializer=auth_dot_auth__pb2.GetByUserReply.SerializeToString,
      ),
      'GetByJti': grpc.unary_unary_rpc_method_handler(
          servicer.GetByJti,
          request_deserializer=auth_dot_auth__pb2.GetByJtiRequest.FromString,
          response_serializer=auth_dot_auth__pb2.GetByJtiReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'chaosplatform.auth.AuthService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

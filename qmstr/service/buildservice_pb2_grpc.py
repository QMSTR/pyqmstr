# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import buildservice_pb2 as buildservice__pb2
import datamodel_pb2 as datamodel__pb2


class BuildServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Build = channel.stream_unary(
        '/service.BuildService/Build',
        request_serializer=datamodel__pb2.FileNode.SerializeToString,
        response_deserializer=buildservice__pb2.BuildResponse.FromString,
        )
    self.SendBuildError = channel.unary_unary(
        '/service.BuildService/SendBuildError',
        request_serializer=datamodel__pb2.InfoNode.SerializeToString,
        response_deserializer=buildservice__pb2.BuildResponse.FromString,
        )
    self.PushFile = channel.unary_unary(
        '/service.BuildService/PushFile',
        request_serializer=buildservice__pb2.PushFileMessage.SerializeToString,
        response_deserializer=buildservice__pb2.PushFileResponse.FromString,
        )


class BuildServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Build(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendBuildError(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushFile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BuildServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Build': grpc.stream_unary_rpc_method_handler(
          servicer.Build,
          request_deserializer=datamodel__pb2.FileNode.FromString,
          response_serializer=buildservice__pb2.BuildResponse.SerializeToString,
      ),
      'SendBuildError': grpc.unary_unary_rpc_method_handler(
          servicer.SendBuildError,
          request_deserializer=datamodel__pb2.InfoNode.FromString,
          response_serializer=buildservice__pb2.BuildResponse.SerializeToString,
      ),
      'PushFile': grpc.unary_unary_rpc_method_handler(
          servicer.PushFile,
          request_deserializer=buildservice__pb2.PushFileMessage.FromString,
          response_serializer=buildservice__pb2.PushFileResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'service.BuildService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
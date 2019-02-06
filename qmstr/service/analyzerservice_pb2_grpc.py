# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import analyzerservice_pb2 as analyzerservice__pb2


class AnalysisServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAnalyzerConfig = channel.unary_unary(
        '/service.AnalysisService/GetAnalyzerConfig',
        request_serializer=analyzerservice__pb2.AnalyzerConfigRequest.SerializeToString,
        response_deserializer=analyzerservice__pb2.AnalyzerConfigResponse.FromString,
        )
    self.SendInfoNodes = channel.stream_unary(
        '/service.AnalysisService/SendInfoNodes',
        request_serializer=analyzerservice__pb2.InfoNodeMessage.SerializeToString,
        response_deserializer=analyzerservice__pb2.SendResponse.FromString,
        )
    self.SendFileNode = channel.stream_unary(
        '/service.AnalysisService/SendFileNode',
        request_serializer=analyzerservice__pb2.FileNodeMessage.SerializeToString,
        response_deserializer=analyzerservice__pb2.SendResponse.FromString,
        )
    self.SendPackageNode = channel.stream_unary(
        '/service.AnalysisService/SendPackageNode',
        request_serializer=analyzerservice__pb2.PackageNodeMessage.SerializeToString,
        response_deserializer=analyzerservice__pb2.SendResponse.FromString,
        )


class AnalysisServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetAnalyzerConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendInfoNodes(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendFileNode(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendPackageNode(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AnalysisServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAnalyzerConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetAnalyzerConfig,
          request_deserializer=analyzerservice__pb2.AnalyzerConfigRequest.FromString,
          response_serializer=analyzerservice__pb2.AnalyzerConfigResponse.SerializeToString,
      ),
      'SendInfoNodes': grpc.stream_unary_rpc_method_handler(
          servicer.SendInfoNodes,
          request_deserializer=analyzerservice__pb2.InfoNodeMessage.FromString,
          response_serializer=analyzerservice__pb2.SendResponse.SerializeToString,
      ),
      'SendFileNode': grpc.stream_unary_rpc_method_handler(
          servicer.SendFileNode,
          request_deserializer=analyzerservice__pb2.FileNodeMessage.FromString,
          response_serializer=analyzerservice__pb2.SendResponse.SerializeToString,
      ),
      'SendPackageNode': grpc.stream_unary_rpc_method_handler(
          servicer.SendPackageNode,
          request_deserializer=analyzerservice__pb2.PackageNodeMessage.FromString,
          response_serializer=analyzerservice__pb2.SendResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'service.AnalysisService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

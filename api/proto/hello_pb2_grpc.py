# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import hello_pb2 as proto_dot_hello__pb2


class GreetingStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GreetingServer = channel.unary_unary(
        '/hello.Greeting/GreetingServer',
        request_serializer=proto_dot_hello__pb2.Name.SerializeToString,
        response_deserializer=proto_dot_hello__pb2.Message.FromString,
        )


class GreetingServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GreetingServer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreetingServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GreetingServer': grpc.unary_unary_rpc_method_handler(
          servicer.GreetingServer,
          request_deserializer=proto_dot_hello__pb2.Name.FromString,
          response_serializer=proto_dot_hello__pb2.Message.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hello.Greeting', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

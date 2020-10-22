from concurrent import futures

import click
import grpc
from grpc_reflection.v1alpha import reflection

from proto import hello_pb2, hello_pb2_grpc


class GreetingServicer(hello_pb2_grpc.GreetingServicer):

    def GreetingServer(self, request, context):
        print(f"Receiving a request from client. {request.name}")
        return hello_pb2.Message(message=f"Hello {request.name}")


def serve():
    print("Starting greeting grpc server.")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreetingServicer_to_server(
        GreetingServicer(), server)
    SERVICE_NAMES = (
        hello_pb2.DESCRIPTOR.services_by_name['Greeting'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    print(f"Running on port 9090 ... ")
    server.add_insecure_port('[::]:9090')
    server.start()
    print(f"Server started ! ")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

import click
import grpc

from proto import hello_pb2, hello_pb2_grpc


@click.command()
@click.option('--server-host', default="localhost", help='Server host name')
@click.option('--server-port', type=int, default=9090, help='Server port number')
@click.argument('name')
def request(server_host, server_port, name):
    server_addr = f'{server_host}:{server_port}'
    with grpc.insecure_channel(server_addr) as channel:
        stub = hello_pb2_grpc.GreetingStub(channel)
        message = stub.GreetingServer(hello_pb2.Name(name=name))
        print(message.message)


if __name__ == '__main__':
    request()
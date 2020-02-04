from __future__ import print_function
import logging

import grpc

import todo_pb2
import todo_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = todo_pb2_grpc.TodoServiceStub(channel)
        response = stub.AddTodo(todo_pb2.Todo(body='Hello World'))
    print("Greeter client received: " + response.body)


if __name__ == '__main__':
    logging.basicConfig()
    run()
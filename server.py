from concurrent import futures
import logging

import grpc

import todo_pb2
import todo_pb2_grpc

class TodoService(todo_pb2_grpc.TodoServiceServicer):

    def AddTodo(self, request, context):
        return todo_pb2.Todo(body=request.body)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
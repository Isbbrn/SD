import grpc
from concurrent import futures
import time

import chat_pb2
import chat_pb2_grpc

class ChatServicer(chat_pb2_grpc.ChatServicer):

    def __init__(self):
        self.messages = []

    def SendMessage(self, request, context):
        message = chat_pb2.Message(sender=request.sender, text=request.text)
        self.messages.append(message)
        return chat_pb2.Empty()

    def ReceiveMessages(self, request, context):
        for message in self.messages:
            yield message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(ChatServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()


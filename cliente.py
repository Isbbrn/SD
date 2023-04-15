import grpc

import chat_pb2
import chat_pb2_grpc

def send_message(stub, sender, text):
    message = chat_pb2.Message(sender=sender, text=text)
    stub.SendMessage(message)
    print("Message sent successfully.")

def receive_messages(stub):
    messages = stub.ReceiveMessages(chat_pb2.Empty())
    for message in messages:
        print(f"{message.sender}: {message.text}")

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_pb2_grpc.ChatStub(channel)

    sender = input("Enter your name: ")
    print("Type '/quit' to exit.")

    while True:
        text = input("> ")
        if text == "/quit":
            break
        send_message(stub, sender, text)

    channel.close()

if __name__ == '__main__':
    run()

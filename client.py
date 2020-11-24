from network import Client
import threading

client = Client("127.0.0.1")

def recieve():
  while True:
    message = client.recieve()
    print(message)

def write():
  while True:
    message = input()
    client.send(message)

recieveThread = threading.Thread(target=recieve)
recieveThread.start()

writeThread = threading.Thread(target=write)
writeThread.start()
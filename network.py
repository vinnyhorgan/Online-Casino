import socket

class Client:
  def __init__(self, ip):
    self.ip = ip
    self.port = 5555
    self.address = (self.ip, self.port)
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.client.connect(self.address)

  def send(self, data):
    self.client.send(data.encode())

  def recieve(self):
    data = self.client.recv(2048).decode()
    return data

class Server:
  def __init__(self, ip, maxConnections):
    self.ip = ip
    self.port = 5555
    self.address = (self.ip, self.port)
    self.maxConnections = maxConnections
    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server.bind(self.address)
    self.server.listen(self.maxConnections)
    print("Server started, listening on port 5555...")

  def accept(self):
    conn, addr = self.server.accept()
    print(str(addr[0]) + " connected to the server")
    return conn

  def send(self, data, conn):
    conn.send(data.encode())

  def recieve(self, conn):
    data = conn.recv(2048).decode()
    return data
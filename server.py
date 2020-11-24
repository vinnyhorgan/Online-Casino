from network import Server
import threading
import time
import random

server = Server("127.0.0.1", 1)

clients = []

def broadcast(message):
  for client in clients:
    server.send(message, client)

def recieve():
  while True:
    client = server.accept()
    clients.append(client)

def game():
  broadcast("Welcome to the ONLINE PYTHON CASINO!\nPlayer 1 choose the amount of money you want to play\n")

  money1 = int(server.recieve(clients[0]))

  broadcast("Player 1 chose to play " + str(money1) + " dollars!\nPlayer 2 choose the amount of money you want to play\n")

  money2 = int(server.recieve(clients[1]))

  broadcast("Player 2 chose to play " + str(money2) + " dollars!\n")

  plate = 0

  while True:
    broadcast("Welcome to a round of our game!\nPlayer 1 has " + str(money1) + " dollars left!\nPlayer 2 has " + str(money2) + " dollars left!\nPlayer 1 place your bet\n")

    bet1 = int(server.recieve(clients[0]))
    money1 -= bet1

    broadcast("Player 1 placed a bet of " + str(bet1) + " dollars!\nPlayer 2 place your bet\n")

    bet2 = int(server.recieve(clients[1]))
    money2 -= bet2

    plate += bet1 + bet2

    broadcast("Player 2 placed a bet of " + str(bet2) + " dollars!\nOn the plate there are currently " + str(plate) + " dollars!\nPlayer 1 guess a number beetween 1 and 3\n")

    guess1 = server.recieve(clients[0])

    broadcast("Player 1 guessed " + guess1 + "!\nPlayer 2 make you're guess\n")

    guess2 = server.recieve(clients[1])

    broadcast("Player 2 guessed " + guess2 + "!\n AAAAND...\n")

    number = str(random.randint(1, 3))

    if guess1 == number:
      broadcast("Player 1 guessed the number!!! He won " + str(plate) + " dollars!!!\n")

      money1 += plate
      plate = 0

    elif guess2 == number:
      broadcast("Player 2 guessed the number!!! He won " + str(plate) + " dollars!!!\n")

      money2 += plate
      plate = 0

    elif guess1 == number and guess2 == number:
      broadcast("Players you both guessed the number right! This is a draw and the plate will remain untouched\n")
    else:
      broadcast("Unfortunatly nobody guessed the number...It was " + number + "! Better luck next round, the plate will remain untouched\n")

def lobby():
  while True:
    if len(clients) > 1:
      broadcast("GAME STARTED!")
      game()
      break
    else:
      broadcast("Waiting for player...")

    time.sleep(10)

recieveThread = threading.Thread(target=recieve)
recieveThread.start()

lobbyThread = threading.Thread(target=lobby)
lobbyThread.start()
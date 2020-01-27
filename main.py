# Importing necessary libraries
import threading
import socket
import sys
import time

# Create a UDP socket
host = ''
port = 9000
locaddr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

# Send instructions to the Tello
def send(message):
  try:
    sock.sendto(message.encode(encoding="utf-8"), tello_address)
    print("Sending message :" + str(message))
  except Exception as e:
    print("Error sending: " + str(e))

  time.sleep(3)

# Recieve feed back from the Tello
def recv():
  while True:
    try:
      message, server = sock.recvfrom(1518)
      print("Recived message: " + str(message) + " from " + str(server))
    except Exception as e:
      print("Error reciving: " + str(e))

recvThread = threading.Thread(target=recv)
recvThread.start()

# List of commands the Tello will recieve
send('command')
send('takeoff')
send('cw 180')
send('land')

# Closing socket before exiting the program
sock.close()
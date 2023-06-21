import socket
import time

try:
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % (err))

c.connect(("localhost", 5556))

while True:
    message = "This is a test message."
    c.send(message.encode())
    time.sleep(2)

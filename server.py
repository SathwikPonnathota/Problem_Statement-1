import socket
import time
import os
def main():

    host = '127.0.0.1'
    port = 9999

    serversocket = socket.socket()
    serversocket.bind((host, port))
    serversocket.listen(1)
    print("waiting for the clients")

    clientsocket, address = serversocket.accept()

    print("connection from " + str(address))

    while True:
        data = clientsocket.recv(10240)

        if not data:
            break
        print("the information received from the client is  " + str(data.decode()))

        executedcommand=os.popen(str(data.decode()))
        result=executedcommand.read()
        clientsocket.send(result.encode())


    clientsocket.close()

if __name__ == '__main__':
    main()

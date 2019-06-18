import socket
import time
import os
def main():

    host = '127.0.0.1'
    port = 9998

    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(1)
    print("waiting for the clients")

    c, address = sock.accept()

    print("connection from " + str(address))

    while True:
        data = c.recv(10240)

        if not data:
            break
        print("the information received from the client is  " + str(data.decode()))
        f=os.popen(str(data.decode()))
        command=f.read()
        c.send(command.encode())


    c.close()

if __name__ == '__main__':
    main()

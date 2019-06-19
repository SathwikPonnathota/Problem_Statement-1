import socket
def Main():

    host = '127.0.0.1'
    port = 9999

    clientsocket = socket.socket()
    clientsocket.connect((host, port))

    message = input("Enter your message :  ")
    msg_encode = message.encode()
    while message != 'quit':
        clientsocket.send(msg_encode)

        print("the message sent to the server is " + str(message))
        data = clientsocket.recv(10240)

        print("the message received from the server is   " + str(data.decode()))

        message = input("Enter your message : ")
        msg_encode = message.encode()
    clientsocket.close()


if __name__ == '__main__':
    Main()
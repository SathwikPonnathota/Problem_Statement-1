import socket
def Main():
    host = '127.0.0.1'
    port = 9998

    sock = socket.socket()
    sock.connect((host, port))

    message = input("Enter your message :  ")
    msg_encode = message.encode()
    while message != 'q':
        sock.send(msg_encode)

        print("the message sent to the server is " + str(message))
        data = sock.recv(10240)

        print("the message received from the server is   " + str(data.decode()))

        message = input("Enter your message : ")
        msg_encode = message.encode()
    sock.close()



if __name__ == '__main__':
    Main()
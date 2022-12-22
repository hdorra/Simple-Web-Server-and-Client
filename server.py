from socket import *
import socket

serverSocket = socket.socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #resets if there is a problem

serverPort=8080

serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Server is Ready")
while True: 
    try:
        connectionSocket, addr = serverSocket.accept()
        print(addr)
        message = connectionSocket.recv(4096)
        #message.decode()

        print('Msg is: ')

        #Path is second part of HTTP header denoted by [1]
        filename = message.split()[1]
        print('File name is: ', filename)
        f = open(filename[1:])

        #Store the entire contenet of the requested file in a temporary buffer
        outputdata = f.readlines()

        # Send the HTTP response header line to the connection socket
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n".encode())

        connectionSocket.send("\r\n".encode()) # Empty line


        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        # Close the client connection socket
        connectionSocket.close()

    except IOError:
        #send HTTP response message for file not found
        connectionSocket.send("HTTP/ 1.1 404 Not Found\r\n")

        connectionSocket.send("Content-Type: text/html\r\n".encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        
        connectionSocket.close()

        serverSocket.close()

#python server.py 8080 /www


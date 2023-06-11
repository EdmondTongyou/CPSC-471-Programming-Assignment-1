# import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
serverPort = 800
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start # Fill in end
    try:
        message = connectionSocket.recv(1024) # Fill in start # Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() #Fill in start #Fill in end

        # Send one HTTP header line into socket
        connectionSocket.send(b'HTTP/1.x 200 OK\r\n\r\n') # Fill in start # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.send(b'404 File Not Found\r\n\r\n') # Fill in start # Fill in end

        #Close client and server socket
        connectionSocket.close() # Fill in start # Fill in end
        serverSocket.close()
    sys.exit() #Terminate the program after sending the corresponding data
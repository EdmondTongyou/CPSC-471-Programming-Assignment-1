import socket
import sys

def send_http_request(server_host, server_port, filename):
    # create a socket / establish connection
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    clientsocket.connect((server_host, server_port))

    # HTTP request
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    clientsocket.send(request.encode())

    # print the servers response
    modifiedSentence = clientsocket.recv(1024).decode()


    print("From server:\n", modifiedSentence)

    # closing the socket
    clientsocket.close()

# instead of an input line like the slide examples we use this to take aruments like the lab outlines

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

# HTTP request
send_http_request(server_host, server_port, filename)

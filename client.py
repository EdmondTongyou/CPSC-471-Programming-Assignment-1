from socket import *

server_name = 'localhost'
server_port = 800

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

sentence = input('Input lowercase sentence: ')
request = f"GET /{sentence} HTTP/1.1\r\nHost: {server_name}\r\n\r\n"
client_socket.send(request.encode())

response = client_socket.recv(4096)
print('Server response:')
print(response.decode())

client_socket.close()

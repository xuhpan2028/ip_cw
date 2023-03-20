import socket

server_name = '3.235.249.117'
server_port = 12000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_name, server_port))

print("TCP client running...")
print("Connecting to server at IP: ", server_name, " PORT: ", server_port)
while 1:
    instr = input()

    client_socket.send(instr.encode())

    msg = client_socket.recv(1024)

    response = msg.decode()
    print(response)

client_socket.close()

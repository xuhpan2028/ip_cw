import socket

server_name = '44.200.120.51'
server_port = 12000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_name, server_port))

print("TCP client running...")
print("Connecting to server at IP: ", server_name, " PORT: ", server_port)

instr = input()

#send the message  to the udp server
client_socket.send(instr.encode())

msg = client_socket.recv(1024)

response = msg.decode()
print(response)
if(response == "fail:("):
    print()
else:
    name = input()

    client_socket.send(name.encode())

    msg = client_socket.recv(1024)
    print(msg.decode())

client_socket.close()

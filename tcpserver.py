import socket
from AddPlayer import *
from UpdateScore import *
from showall import *

print("We're in tcp server...");

server_port = 12000

welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

welcome_socket.bind(('0.0.0.0',server_port))

welcome_socket.listen(1)

print('TCP Server running on port ', server_port)

 
while True:
    connection_socket, caddr = welcome_socket.accept()

    cmsg = connection_socket.recv(1024)  	
    cmsg = cmsg.decode()


    if(cmsg == "AddPlayer"):
        cmsg = "Enter the player name: ";
        connection_socket.send(cmsg.encode())

        cmsg = connection_socket.recv(1024)  	
        cmsg = cmsg.decode()
        
        flag = add_player(cmsg)
        if(flag):
            cmsg = "added player: " + flag
        else:
            cmsg = "player exist"
        

    elif(cmsg == "UpdateScore"):
        cmsg = "Enter the player name and score: ";
        connection_socket.send(cmsg.encode())

        cmsg = connection_socket.recv(1024)  	
        cmsg = cmsg.decode()

        name, score = cmsg.split()
        add_score(name, score)

        cmsg = "score added for player: " + name
    

    else:
        cmsg = "fail:(";


    connection_socket.send(cmsg.encode())


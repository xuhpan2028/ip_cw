import socket
from AddPlayer import *
from UpdateScore import *
from showall import *
from ShowScore import *

print("We're in tcp server...");

server_port = 12000

welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

welcome_socket.bind(('0.0.0.0',server_port))

welcome_socket.listen(1)

print('TCP Server running on port ', server_port)

 
while True:
    connection_socket, caddr = welcome_socket.accept()
    while True:
        cmsg = connection_socket.recv(1024)  	
        cmsg = cmsg.decode()

        input_list = cmsg.split()

        if(len(input_list) == 0):
            cmsg = "invalid instr"
            continue

        command = input_list[0]

        if(command == "add"):

            flag = add_player(input_list[1])
            if(flag):
                cmsg = "added player: " + flag
            else:
                cmsg = "player exist"
            

        elif(command == "update"):
            

            add_score(input_list[1], input_list[2])

            cmsg = "score added for player: " + input_list[2]

        elif(command == "showscore"):

            highest, scores = show_score(input_list[1])
            
            if(len(scores) == 0):
                score_string = "no history"
                highest = "0"
            else:
                score_string = ""
                for i in scores:
                    score_string = score_string +  i + ", "
                score_string = score_string[:-2]

            cmsg = "player " + input_list[1] + " has best score of " + highest + "\nhistory: [" + score_string + "]"

        elif(command == "exit"):
            break

        

        else:
            cmsg = "invalid instruction";
        

        


        connection_socket.send(cmsg.encode())

    connection_socket.close()


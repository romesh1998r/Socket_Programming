import socket



Host='192.168.1.5'
Port=5050
ADDR=(Host,Port)
FORMAT='utf-8'
HEADER=64
Disconnect_Message='"Disconnect'



#create the socket

Client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect the connection

Client.connect(ADDR)

#send the message to the Server
def send_message(message):
    #encode intended send_message
    message.encode(FORMAT)
    
    #get the length of the message
    send_msg=len(message)

    send_msg=str(message).encode(FORMAT)

    send_msg +='b'+''*(HEADER-len(send_msg))

    #send the length of message to the server

    Client.send(send_msg)

    #send the message to the server

    Client.send(message)

    print(Client.recv(2048).decode(FORMAT))

    Client.send("Hello,How are you?")
    input()
    Client.send("How was the lockdown these days?")

    Client.send(Disconnect_Message)

    

    

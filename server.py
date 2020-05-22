import socket
import threading



Host=socket.gethostbyname(socket.gethostname())
Port=5050
ADDR=(Host,Port)
HEADER=64
FORMAT='utf-8'
Disconnect_Message='!Disconnect'

#create the socket

Server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the socket

Server.bind(ADDR)


#handle multiple clients

def handle_clients(conn,addr):

    condition=True
    while condition:

        #when received the message of the server
        length_msg=conn.recv(HEADER).decode(FORMAT)

        if length_msg:
            length_msg=int(length_msg)
            #receove the full length of message
            message=conn.recv(length_msg).decode(FORMAT)

            if message == Disconnect_Message:

                condition=False
                print("Addr:" ,addr)
                print("Msg",message)

                conn.send("Message received successfully".encode(FORMAT))

                conn.close()


#set the server setup

def set_server():

#listen to the connection
    Server.listen()
    print("Staring to the listening the connnection")

#accept the new connection
    while true:

        conn,addr=Server.accept()
        #function of the threading
        thread=threading.thread(target=handle_clients,args=(conn,addr))
        thread.start()
        #find the active threads in the server
        print("Incoming connection:",threading.activecount() -1)

        print("Server is starting ")

        set_server()
        
        

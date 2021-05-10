import socket
from _thread import *
import threading


server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',1233))
server_socket.listen(5)

def threaded(c):
    while True:
  
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')
              
            # lock released on exit
            print_lock.release()
            break
  
        # reverse the given string from client
        data = data[::-1]
  
        # send back reversed string to client
        c.send(data)
  
    # connection closed
    c.close()
    
while True:
    print("Server waiting for connetion")
    c,addr=server_socket.accept()
    print("client connected from",addr)
    while True:
        c, c.recv(1024)
        
        if not c:
            print('Bye')
            print_lock.release()
            print_lock.acquire()
            print('Connected to :', addr[0], ':', addr[1])
            start_new_thread(threaded, (c,))
            
            break

            c = c[::-1]

        
        print("recieved from client : %s"% c)

        try:
            client_socket.send(bytes('Hey client','utf-8'))
        except:
            print("Exited by the user")
            
    client_socket
server_socket.close

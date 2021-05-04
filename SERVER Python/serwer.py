import time
import serial
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
from termcolor import colored
import sys
import serial.tools.list_ports
import socket
init(autoreset=True)
import configparser
from _thread import *
import threading


server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',1233))
server_socket.listen(5)


while True:
    print("Server waiting for connetion")
    client_socket,addr=server_socket.accept()
    print("client connected from",addr)
    while True:
        data=client_socket.recv(1024)
        
        if not data or data.decode('utf-8')=='END':
            print('Bye')
            print_lock.release()
            
            break

            data = data[::-1]

        
        print("recieved from client : %s"% data.decode("utf-8"))
        

        try:
            client_socket.send(bytes('Hey client','utf-8'))
        except:
            print("Exited by the user")
            
    client_socket
server_socket.close

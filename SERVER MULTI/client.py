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

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',1233))
#payload = 'Client 1'



ports = list(serial.tools.list_ports.comports())
for p in ports:
    
    print (colored(p , 'white' , 'on_blue'))

porten = input("Podaj port: ")
print(colored('Koparka na porcie {porten} zaczyna kopać!' , 'white' , 'on_magenta').format(porten = porten))

COM = porten
BAUD = 115200

ser = serial.Serial(porten, BAUD, timeout = .1)
	
sleep(3)

print(colored('Wybrany port :' , 'white' , 'on_blue'));

sleep(3)

print(Fore.RED + ser.name)
print(Style.RESET_ALL)

sleep(1)

try:
    while True:
        #client_socket.send(payload.encode('utf-8'))
        #data = client_socket.recv(1024)
        val = str(ser.readline().decode().strip('off \r'))
        valA = val.split("/n")

        client_socket.send(val.encode('utf-8'))
        
        print(Fore.CYAN + val,end="\r",flush=True)
        
except KeyboardInterrupt:
    print("Exited by user")
client_socket.close()

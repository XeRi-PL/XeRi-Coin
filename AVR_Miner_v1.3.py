##########################################
# XeRi-Coin Python AVR Miner (v1.3)
# https://github.com/XeRi-PL/XeRi-Coin
# Distributed under MIT license
# © XeRi-Coin Community 2021
##########################################
# Import libraries

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
from datetime import datetime
from locale import LC_ALL, getdefaultlocale, getlocale, setlocale
from threading import Thread as thrThread
from threading import Lock
from time import ctime, sleep, strptime, time

print(colored(Style.BRIGHT + 'Waiting for device' , 'white' , 'on_blue'));
print(colored(Style.BRIGHT + '##########################################' , 'white' , 'on_cyan'));
print(colored(Style.BRIGHT + '# XeRi-Coin Python AVR Miner (v1.3)      #' , 'white' , 'on_cyan'));
print(colored(Style.BRIGHT + '# https://github.com/XeRi-PL/XeRi-Coin   #' , 'white' , 'on_cyan'));
print(colored(Style.BRIGHT + '# Distributed under MIT license          #' , 'white' , 'on_cyan'));
print(colored(Style.BRIGHT + '# © XeRi-Coin Community 2021             #' , 'white' , 'on_cyan'));
print(colored(Style.BRIGHT + '##########################################' , 'white' , 'on_cyan'));


#payload = 'Client 1'

def greeting():
    # greeting message depending on time
    global greeting
    print(Style.BRIGHT)

    current_hour = strptime(ctime(time())).tm_hour

    if current_hour < 12:
        greeting = get_string('greeting_morning')
    elif current_hour == 12:
        greeting = get_string('greeting_noon')
    elif current_hour > 12 and current_hour < 18:
        greeting = get_string('greeting_afternoon')
    elif current_hour >= 18:
        greeting = get_string('greeting_evening')
    else:
        greeting = get_string('greeting_back') 

config = configparser.ConfigParser()

config.add_section('config')

config['config']['host'] = '127.0.0.1'
config['config']['user'] = 'Alan'
config['config']['passwd'] = 'Ziko9231'
config['config']['portx'] = '1233'

with open('avr.ini', 'w') as configfile:
    config.write(configfile)
    
config = configparser.ConfigParser()
config.read('Resources/avr.ini')

host = config['config']['host']
user = config['config']['user']
passwd = config['config']['passwd']
portx = config['config']['portx']

#print('Miner configuration:')

#print(f'config: {host}')
#print(f'config: {user}')
#print(f'config: {passwd}')
#print(f'config: {portx}')
    
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host,1233))

ports = list(serial.tools.list_ports.comports())
for p in ports:
    
    print (colored(p , 'white' , 'on_blue'))

porten = input("Write a miner port: ")
print(colored('Mining started at {porten} !' ,
              'white','on_magenta').format(porten = porten))

COM = porten
BAUD = 115200

ser = serial.Serial(porten, BAUD, timeout = 1)
	
sleep(1)

print(colored('Miner port :' , 'white' , 'on_blue'));

sleep(1)

print('COM Port :' + Fore.RED + ser.name)
print(Style.BRIGHT)

sleep(1)

data=client_socket.recv(2048)

def now():
    # Return datetime object
    return datetime.now()

try:
    
    
    
    while True:
        #client_socket.send(payload.encode('utf-8'))
        #data = client_socket.recv(1024)
        val = str(Style.BRIGHT + ser.readline().decode().strip('off \r'))
        valA = val.split("/n")
        
        #print(data)
        
        client_socket.send(val.encode('utf-8'))
        #client_socket.send(user.encode('utf-8'))
        sleep(1)
        print( colored(now().strftime(Style.BRIGHT + "%H:%M:%S") , 'white' , 'on_yellow' ) + val );
        
#,end="\r",flush=True        
except KeyboardInterrupt:
    print("Exited by user")
#client_socket.close()

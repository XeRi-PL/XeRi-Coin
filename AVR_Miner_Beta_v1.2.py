##########################################
# XeRi-Coin Python AVR Miner (v1.2)
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

print(colored('Waiting for device' , 'white' , 'on_blue'));
print(colored('##########################################' , 'white' , 'on_green'));
print(colored('# XeRi-Coin Python AVR Miner (v1.2)      #' , 'white' , 'on_green'));
print(colored('# https://github.com/XeRi-PL/XeRi-Coin   #' , 'white' , 'on_green'));
print(colored('# Distributed under MIT license          #' , 'white' , 'on_green'));
print(colored('# © XeRi-Coin Community 2021             #' , 'white' , 'on_green'));
print(colored('##########################################' , 'white' , 'on_green'));


ports = list(serial.tools.list_ports.comports())
for p in ports:
	print (colored(p , 'white' , 'on_blue'))

porten = input("Which port ? : ")
print(colored('Mining started at {porten} !' , 'white' , 'on_magenta').format(porten = porten))

COM = porten
BAUD = 115200

ser = serial.Serial(porten, BAUD, timeout = .1)
	
sleep(3)

print(colored('Port :' , 'white' , 'on_blue'));

sleep(3)

print(Fore.RED + ser.name)
print(Style.RESET_ALL)

sleep(1)

#check args
if("-m" in sys.argv or "--monitor" in sys.argv):
	monitor = True
#else:
#	monitor= False

while True:
	val = str(ser.readline().decode().strip('off \r'))
	valA = val.split("/n")

#if(monitor == True):
        
	print(Fore.CYAN + val,end="\r",flush=True)


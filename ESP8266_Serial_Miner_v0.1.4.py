##########################################
# XeRi-Coin Python ESP Miner (v0.1.4)
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
from pathlib import Path
init(autoreset=True)
import configparser
from datetime import datetime
from locale import LC_ALL, getdefaultlocale, getlocale, setlocale
from threading import Thread as thrThread
from threading import Lock
from time import ctime, sleep, strptime, time
from json import load as jsonload
from pathlib import Path
from configparser import ConfigParser
from json import jsonload
from os import name as osname
from os import system as ossystem
from os import path
from platform import system
import requests
from os import _exit, execl, mkdir
config = configparser.ConfigParser()

config.add_section('config')

config['config']['host'] = 'xeri.sytes.net'
config['config']['user'] = ''
config['config']['passwd'] = ''
config['config']['portx'] = '1233'

with open('ESP8266_Serial_Miner_0.1.4_resources/ESPConfigure.ini', 'w') as configfile:
    config.write(configfile)
    
config = configparser.ConfigParser()
config.read('ESP8266_Serial_Miner_0.1.4_resources/ESPConfigure.ini')

host = config['config']['host']
user = config['config']['user']
passwd = config['config']['passwd']
portx = config['config']['portx']



client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host,1233))


# Global variables
MINER_VER = "0.1.4" 
SOCKET_TIMEOUT = 15
ESP_TIMEOUT = 7
thread_lock = Lock()
RESOURCES_DIR = "ESP8266_Serial_Miner_" + str(MINER_VER) + "_resources"
config = ConfigParser()
thread_lock = Lock()

# Create resources folder if it doesn't exist
if not path.exists(RESOURCES_DIR):
    mkdir(RESOURCES_DIR)



# Check if languages file exists
if not Path(RESOURCES_DIR + "/langs.json").is_file():
    url = ("https://github.com/XeRi-PL/XeRi-Coin/blob/main/Resources/langs.json")

    r = requests.get(url)
    with open(RESOURCES_DIR + "/langs.json", "wb") as f:
        f.write(r.content)

# Load language file
with open(RESOURCES_DIR + "/langs.json", "r", encoding="utf8") as lang_file:
    lang_file = jsonload(lang_file)

# OS X invalid locale hack
if system() == '':
    if getlocale()[0] is None:
        setlocale(LC_ALL, 'en_US.UTF-8')

# Check if miner is configured, if it isn't, autodetect language
try:
    if not Path(RESOURCES_DIR + "/Miner_config.cfg").is_file():
        locale = getdefaultlocale()[0]
        if locale.startswith("pl"):
            lang = "polish"
        else:
            lang = "english"
    else:
        try:
            # Read language from configfile
            config.read(RESOURCES_DIR + "/Miner_config.cfg")
            lang = config["arduminer"]["language"]
        except Exception:
            # If it fails, fallback to english
            lang = "english"
except:
    lang = "english"





    
def get_string(string_name):
    # Get string form language file
    if string_name in lang_file[lang]:
        return lang_file[lang][string_name]
    elif string_name in lang_file["english"]:
        return lang_file["english"][string_name]
    else:
        return "String not found: " + string_name




print(colored(Style.BRIGHT + 'Waiting for device' , 'white' , 'on_blue'));
print(colored(Style.BRIGHT + '##########################################' , 'white' , 'on_cyan'));
print(colored(Style.BRIGHT + '# XeRi-Coin Python ESPMiner(v0.1.4)      #' , 'white' , 'on_cyan'));
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
        greeting = print("good_morning")
    elif current_hour == 12:
        greeting = print("good_noon")
    elif current_hour > 12 and current_hour < 18:
        greeting = print("good_afternoon")
    elif current_hour >= 18:
        greeting = print("good_evening")
    else:
        greeting = print("good_back") 

#print('Miner configuration:')

#print(f'config: {host}')
#print(f'config: {user}')
#print(f'config: {passwd}')
#print(f'config: {portx}')

def load_config():

    global ESPport

    
try:
            # Read language from configfile
            config.read(RESOURCES_DIR + "/Miner_config.cfg")
            lang = config["arduminer"]["language"]
except:
    lang = "english"
    

ports = list(serial.tools.list_ports.comports())

portlist = serial.tools.list_ports.comports()

if not Path(str(RESOURCES_DIR) + "/Miner_config.cfg").is_file():


        for p in ports:
            print(Style.RESET_ALL
                  + Style.BRIGHT
                  + Fore.RESET
                  + "  "
                  + str(ports))
        print(Style.RESET_ALL
              + Fore.YELLOW
              + get_string("ports_notice"))

        ESPport = ""
        while True:
            ESPport += input(
                Style.RESET_ALL
                + Fore.YELLOW
                + get_string("ask_ESPport")
                + Fore.RESET
                + Style.BRIGHT)
            confirmation = input(
                Style.RESET_ALL
                + Fore.YELLOW
                + get_string("ask_anotherport")
                + Fore.RESET
                + Style.BRIGHT)
            if confirmation == "y" or confirmation == "Y":
                ESPport += ","
            else:
                break


ports = list(serial.tools.list_ports.comports())
for p in ports:
    
    print (colored(p , 'white' , 'on_blue'))

porten = input("Choose port: ")
print(colored('Mining started at {porten} !' ,
              'white','on_magenta').format(porten = porten))

COM = porten
BAUD = 115200

ser = serial.Serial(porten, BAUD, timeout = 1)

sleep(1)

print(colored('Miner port :' , 'white' , 'on_blue'));

sleep(1)

print('ESP Port :' + Fore.RED + ser.name)
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

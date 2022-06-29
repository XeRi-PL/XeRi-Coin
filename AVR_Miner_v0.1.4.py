##########################################
# XeRi-Coin Python AVR Miner (v0.1.4)
# https://github.com/XeRi-PL/XeRi-Coin
# Distributed under MIT license
# XeRi-Coin Community 2021
##########################################

# Import libraries
import time
from time import sleep
from time import ctime, sleep, strptime, time
from serial import Serial
import serial.tools.list_ports
from serial import win32
import serial, time, sys, threading
from serial.serialutil import SerialBase, SerialException, to_bytes
import json
from json import load as jsonload
from locale import LC_ALL, getdefaultlocale, getlocale, setlocale
from colorama import Fore, Back, Style
from termcolor import colored
from colorama import init
init(autoreset=True)
import socket
from pathlib import Path
import os
from datetime import datetime
from _thread import *
from threading import Thread
from threading import Thread as thrThread
from threading import Lock as thread_lock
from threading import Semaphore
printlock = Semaphore(value=1)
from re import sub
import subprocess
import configparser
from configparser import ConfigParser
from os import _exit, execl, mkdir
from os import name as osname
from os import system as ossystem
from os import path
from platform import system
from pathlib import Path
import serial
import requests
import select

# Global variables
MINER_VER = "0.1.4" 
SOCKET_TIMEOUT = 15
AVR_TIMEOUT = 7
name= ''
avrport = ''
RESOURCES_DIR = "AVRMiner_" + str(MINER_VER) + "_resources"
config = ConfigParser()
ping_mean = []
host = '127.0.0.1'
portx = '1233'
x=''

# Create resources folder if it doesn't exist
if not path.exists(RESOURCES_DIR):
    mkdir(RESOURCES_DIR)

def now():
    # Return datetime object
    return datetime.now()

def port_num(avrport):
    return str(''.join(filter(str.isdigit, avrport)))
  
def get_string(string_name):
    # Get string form language file
    if string_name in lang_file[lang]:
        return lang_file[lang][string_name]
    elif string_name in lang_file["english"]:
        return lang_file["english"][string_name]
    else:
        return "String not found: " + string_name

def greeting():
    # greeting message depending on time
    global greeting
    print(Style.BRIGHT)

    current_hour = strptime(ctime(time())).tm_hour

    if current_hour < 12:
        greeting = print('good_morning')
    elif current_hour == 12:
        greeting = print('good_noon')
    elif current_hour > 12 and current_hour < 18:
        greeting = print('good_afternoon')
    elif current_hour >= 18:
        greeting = print('good_evening')
    else:
        greeting = print('good_back') 

if system() == 'Darwin':
    if getlocale()[0] is None:
        setlocale(LC_ALL, 'en_US.UTF-8')

def title(title):
    # Window title
    if osname == 'nt':
        # Windows systems
        ossystem('title ' + title)
    else:
        # Most standard terminals
        print('\33]0;' + title + '\a', end='')
        sys.stdout.flush()

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,1233))

print(colored(Style.BRIGHT + 'Waiting for device' , 'white' , 'on_blue'));
print(colored(Style.BRIGHT + '##########################################' , 'white' , 'on_cyan'));
print(colored(Style.BRIGHT + f'# XeRi-Coin Python AVRMiner(v{MINER_VER})      #' , 'white' , 'on_cyan'));
print(colored(Style.BRIGHT + '# https://github.com/XeRi-PL/XeRi-Coin   #' , 'white' , 'on_cyan'));
print(colored(Style.BRIGHT + '# Distributed under MIT license          #' , 'white' , 'on_cyan'));
print(colored(Style.BRIGHT + '# © XeRi-Coin Community 2021 - 2022      #' , 'white' , 'on_cyan'));
print(colored(Style.BRIGHT + '##########################################' , 'white' , 'on_cyan'));
# Check if miner is configured, if it isn't, autodetect language

lang = "polish"

if not Path(RESOURCES_DIR + '/langs.json').is_file():
    url = ('https://raw.githubusercontent.com/XeRi-PL/XeRi-Coin/main/Resources/langs.json')
    r = requests.get(url)
    with open(RESOURCES_DIR + '/langs.json', 'wb') as f:
        f.write(r.content)

# Load language file
with open(RESOURCES_DIR + '/langs.json', 'r', encoding='utf8') as lang_file:
    lang_file = jsonload(lang_file)

# OS X invalid locale hack
if system() == '':
    if getlocale()[0] is None:
        setlocale(LC_ALL, 'en_US.UTF-8')
              
ports = list(serial.tools.list_ports.comports())
portlist = serial.tools.list_ports.comports()

if not Path(str(RESOURCES_DIR) + '/Miner_config.cfg').is_file():

    print(get_string("ports_notice"))

    for p in ports:
        print(str(p))
        port_names =[]
        for p in ports:

            avrport = ''
    
    while True:
        avrport += input(get_string("ask_avrport"))
        confirmation = input(get_string("ask_anotherport"))
        if confirmation == "y" or confirmation == "Y":
            avrport += ','
        else:
            break

    config = configparser.ConfigParser()
    config.add_section('avr')
    config['avr']['avrport'] = avrport
        
    # Write data to file
    with open('AVRMiner_0.1.4_resources/Miner_config.cfg', 'w') as d:
        config.write(d)
else:
    config = configparser.ConfigParser()
    config.read('AVRMiner_0.1.4_resources/Miner_config.cfg')
    avrport = config['avr']['avrport']
    avrport = avrport.replace(" ","").split(',')
print("SAVED !")

def port_num(avrport):
    return str(''.join(filter(str.isdigit, avrport)))


def miner(avrport,):
    global xxd , i
    job_good = 0
    job_all = 0

    sleep(1)
    try:
        print("Mining started <3 ")
        sleep(1)
        while True:
            sleep(2)
            i = 0
            for i in range(10_000):
            
                xxd = Serial(avrport,baudrate = 115200,timeout = 2.2)
                i += 1
    except:  
        sleep(1)
    try:
        
        while True:
            responsetimetart = time.time()
            Speedhash = 0.000260 * i 
            list_gpus = "AVR_Nano"

            config = configparser.ConfigParser()
            config.read('AVRMiner_0.1.4_resources/avr.ini')
            user = config['config']['user']
            
            xdc = (str(user)+ "," + str(round(float(Speedhash),7)) +","+""+","+""+","+""+","+ str(list_gpus)+","+""+","+"AVR")
            client.send(xdc.encode('utf-8'))
            
            uwu = client.recv(400).decode('utf-8')
            uwu = uwu.split(',')
            
            if uwu[0] == "11":
                xxd.write(uwu[2].encode('utf-8'))
            
            val = xxd.readline().decode().strip() #'off \r'
            valA = val.split(',') #'\n'
            sleep(0.2)
            if len(val) == 40:
                job_good = job_good + 1
            else:
                job_good = job_good - 1
            job_all = job_all + 1
            
            responsetimestop = time.time()
            ping = ((responsetimestop - responsetimetart) + 0.1) * 10

            print(Fore.LIGHTBLUE_EX + "COM" + port_num(avrport) + " - " 
            + now().strftime(Style.BRIGHT + "%H:%M:%S")
            + " - " 
            + Fore.YELLOW + "Hashrate: " + str(Speedhash) + " MH/s ( " + str(Speedhash * 1000000 ) + " kH/s )"
            + Fore.LIGHTCYAN_EX + " - Share's: " + str(job_good) + "/" + str(job_all) 
            + Fore.GREEN + " Ping: " + str(round(float(ping),2)) + " ms")

            sleep(1.6)
        else:
            raise Exception("No data received from AVR")
        sleep(1)    
    except Exception as e:
        print('Error launching AVR Miner: ' + str(e))
        
#-----------------------------------------------------------------------------------------------------

try:
    if not Path(str(RESOURCES_DIR) + '/avr.ini').is_file():

        config = configparser.ConfigParser()
        config.add_section('config')

        config['config']['user'] = ''

        with open('AVRMiner_0.1.4_resources/avr.ini', 'w') as f:
            config.write(f)
        sleep(5)
        print("!!!! Uzupełnij user w arv.ini !!!!")
        sleep(5)
    else:

        config = configparser.ConfigParser()
        config.read('AVRMiner_0.1.4_resources/avr.ini')
        user = config['config']['user']
        user_input = input("Podaj swój nick : \n")

        if user_input == user:

            for i in range(len(avrport)):
                y = i
                y = threading.Thread(target=miner, args =(avrport[i],))
        #y.daemon = True
        #sleep(1)
        #threading.append(i)
                y.start()
except:
        print("Error: unable to start thread")


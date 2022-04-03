from ast import Continue
from multiprocessing.connection import wait
import os
from cgitb import text
from re import I
import socket
import sys
import time
import colorama
import threading
from datetime import datetime
from collections import deque
from colorama import Fore, Back, Style
from tabulate import tabulate
from os import name as osname
from pathlib import Path
from time import sleep
from threading import Lock
colorama.init()
i = int(0)

###########################################################
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',1233))
###########################################################

def start():
    try:
        while True:
  
            sender = input('Write your name : ')
            recipter = input('Write friend username: ')
            sleep(1)
            how_many = input('How much send XeriCoin to friend ? : ')
            sleep(1)
            gpu2 = input("GOOD ? :")
            hh= 0.0
            if gpu2 == "y":
                sleep(1)
                asd =("TT"+","+ "0.0" +","+ str(sender) + "," + str(recipter) + "," + str(how_many))
                client.send(asd.encode('utf-8'))
                sleep(5)

            print("xxx")
            Fore.RESET

    except Exception as e:
            print(Fore.LIGHTRED_EX +'Error STATS : ' + str(e))

print(Fore.GREEN + "[STARTING]")
Fore.RESET
start()

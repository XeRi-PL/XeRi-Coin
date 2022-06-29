from argparse import ONE_OR_MORE
from ast import Continue, Pass
from asyncio.windows_events import NULL
from fileinput import close
from multiprocessing.connection import wait
import os
from cgitb import text
from re import I
import socket
import sys
import time
from os import _exit, execl, mkdir
from turtle import back
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
import configparser
from configparser import ConfigParser
colorama.init()
i = int(0)
j = int(0)
v = int(0)
###########################################################
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',1233))
###########################################################
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def start(i,j):
    global sender, recipter , how_many , gpu2 , one , user
    try:
        while True:
            asd = (""+ ","+ "0.0" +","+ str(sender) + "," + str(recipter) + "," + str(float(how_many))+","+""+","+""+","+"TT")
            client.send(asd.encode('utf-8'))
            msg = client.recv(2024).decode('utf-8')
            msg = msg.split(",")
            print("----Waiting----")
            sleep(3)
            
            if msg[7] == "TT":
                sleep(1)
                print("----------------------------------------Transaction success !!!---------------------------------------")
                print("Transacion hash : " + Fore.YELLOW + str(msg[6]) + Fore.RESET + " You Send : " + 
                Fore.LIGHTCYAN_EX + str(float(msg[5])) + Fore.RESET + " to : " + Fore.LIGHTMAGENTA_EX + str(msg[4]) + Fore.RESET)
                while True:
                    asdd = (str(msg[6])+ ","+ "0.0" +","+ str(sender) + "," + str(recipter) + "," + str(float(how_many))+","+""+","+""+","+"TTT")
                    client.send(asdd.encode('utf-8'))
                    sleep(0.1)
            elif msg[0]== "GOOD":
                #sleep()
                gpu2 = "n"
                sleep(0.2)

            else:
                sleep(1)
                Fore.RESET
    except Exception as e:
        NULL
def amount(i,j):
    global sender, recipter , how_many , gpu2 , one , user , yty
    try:
        
        amount = (f"{user}" + "," + "" + "," + "" + "," + ""+ "," + "" + "," + "" + "," + "" + "," + "YYY")
        client.send(amount.encode('utf-8'))
        msg = client.recv(2024).decode('utf-8')
        msg = msg.split(",")
        yty = str(msg[9])
        if msg[9] == "1":
            print("Your amount : " + str(msg[8]))
            sleep(1)
        if yty == "n":
            print("OK")
            one = 0
            user = ''
            amountf = 'x'

            client.send(amountf.encode('utf-8'))
            
            
            sleep(1)
            client.dup
            print("Witaj ponownie")
            sys.argv.clear
            main(sys.argv)

                
    except Exception as e:
        NULL

def main(argv):

    global sender, recipter , how_many , one , gpu2 , user , yty

    user = input("YOUR NICK : ")
    sys.argv.clear
    print("-- Menu : ")
    print("-- 1. check your amount")
    print("-- 2. send amount to friend")
    one = input("-- Optipon (1/2) :")

    if one == "1":
  
        while True:

            hread3 = threading.Thread(target=amount, args=(i, j))
            hread3.start()
            
            sleep(1)


    elif one == "2":
        clear()
        sender = input('Write your name : ')
        recipter = input('Write friend username : ')
        how_many = input('How much send XeriCoin to friend ? : ')
        try:
            Fore.RESET
            print(' -- Transaction :' + Fore.YELLOW + f'{how_many}' +Fore.RESET + ' from : ' + Fore.LIGHTCYAN_EX 
            + f'{sender}' + Fore.RESET + ' to : ' + Fore.LIGHTMAGENTA_EX + f'{recipter}' + Fore.RESET +  '. -- ')
            Fore.RESET
            gpu2 = input(Fore.RESET + "   ---------- Confirm ? (y/n): ---------- ")
            while True:
                
                Fore.RESET
                if gpu2 == "y":
                    Fore.RESET
            #start(i,j)
                    hread2 = threading.Thread(target=start, args=(i, j))
                    hread2.start()
                    print(Fore.GREEN + "... ... waiting to procces transaction ... ..." + Fore.RESET)
                    sleep(5)
                    
                if gpu2 == "n":
                    print("")
                    sys.argv.clear
                    main(sys.argv)
                    

        except Exception as e:
            NULL
        #print(Fore.LIGHTRED_EX +'Error STATS : ' + str(e))
if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        print("")
    input()

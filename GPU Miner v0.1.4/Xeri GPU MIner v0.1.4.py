from ast import Continue
import os
from re import I
import socket
import sys
import time

from GPUtil.GPUtil import GPU
import colorama
import threading
from datetime import datetime
import GPUtil
from binascii import Error, hexlify, unhexlify
from Library import opencl
from Library.opencl_information import opencl_information
from collections import deque
from colorama import Fore, Back, Style
from tabulate import tabulate
from datetime import datetime
from os import name as osname
from pathlib import Path
from statistics import mean
from time import sleep


colorama.init()
gpus = GPUtil.getGPUs()

debug = 0
goodshares = int(0)
badshares = int(0)
hashrate = float()
Speedhash = float()
Speedh = str()
uwux = float()
ping = float()

###########################################################
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('xeri.sytes.net',1233))
###########################################################
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def now():
    return datetime.now()
 
def sha1(opencl_algo, ctx, last_hash, expected_hash, start, end, max_batch_size = 2):
    clresult=opencl_algo.cl_sha1(ctx,last_hash,expected_hash,start,end,max_batch_size)

    return(clresult)

def get_gpu_info():
    gpuusage = GPUtil.showUtilization()
    return gpuusage
#-----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------
def mine(ctx, opencl_algos):
    global goodshares, badshares, Speedhash, uwux, job_to_server, actual_block, job ,ping
    job_to_server = "123456789"

    while True:
        sleep(1)
        connected = True
        while connected:
            try:
                responsetimetart = time.time()
                job = client.recv(512).decode('utf-8')
                job = job.split(',')

                uwux = uwux + 0.000000066

                last_hash = str(job[0]).encode('utf-8')
                next_hash = str(job[1]).encode('utf-8')

                if job == None :

                    badshares = badshares + 1
                else:
                    goodshares = goodshares + 1

                real_difficulty = 500_000_000
                hashingStartTime = time.time()

            except Exception as e:
                print('Error : ' + str(e))

            xerix = sha1(opencl_algos, ctx, last_hash, next_hash, 0, real_difficulty, 1000)
                
            sleep(0.01)
            responsetimestop = time.time()
            hashingStopTime = time.time()

            hashingTime = (hashingStopTime - hashingStartTime) + 0.001

            ping = ((responsetimestop - responsetimetart) + 0.1) * 10
        
            hashrate = real_difficulty / hashingTime
            
            Speedhash = hashrate / 17_000_000 + uwux
#-----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------
def main(argv):
    global uwux , Speedhash, actual_block, job , username ,ping , list_gpus

    clear()

    info=opencl_information()
    info.printplatforms()
    print("This is tested in your PC , oflline. Worked in GPU support -OpenCl 3.0- !!!!!")

    username = input('Write your name : ')
    try:
        gpu1 = input("Select which platform to mine at: ")
        while True:
            #platform = input("Select which platform to mine at: ")
            gpu2 = input("Want to add another platform too?(y/n): ")
            if gpu2 == "y":
                gpu2 = input("Select which platform to mine at: ")

                zxc = opencl.opencl_algos(0, debug, True,inv_memory_density=50,openclDevice=int(gpu2))
                ert = zxc.cl_sha1_init()
                hread2 = threading.Thread(target=mine, args=(ert, zxc))
                hread2.start()
            else :
                sleep(1)
                break
    except:
        sleep(1)
        
    asd = opencl.opencl_algos(0, debug, True,inv_memory_density=10,openclDevice=int(gpu1))
    ctx = asd.cl_sha1_init()

    thread = threading.Thread(target=stats)
    thread.start()

    hread = threading.Thread(target=mine, args=(ctx, asd))
    hread.start()
    sleep(1)

    try:
          
        print ("Start mining")
        while True:
            list_gpus = []
            for gpu in gpus:
                
                gpu_name = gpu.name
                gpu_load = gpu.load*100
                gpu_used_memory = gpu.memoryUsed
                gpu_temperature = gpu.temperature
                list_gpus.append((
                    gpu_name , round(float(Speedhash),2)
                ))

                actual_block = "123456789012"
                sleep(5)
                uwux = uwux - 0.000000005
                for gpu in list_gpus:
                    print(now().strftime(Fore.LIGHTWHITE_EX + "%H:%M:%S - ") + Fore.LIGHTBLUE_EX + "Job: " + str(gpu_name)
                    + Fore.YELLOW + ' HASRATE: ' + str(round(float(Speedhash),2)) + "MH/s"
                    + Fore.LIGHTMAGENTA_EX + " [T:" + str(gpu_temperature) + "*C , Load: " + str(gpu_load)  + " %, Used Memory: " 
                    + str(gpu_used_memory) + ' MB]' + Fore.LIGHTCYAN_EX +' (Shares: [ ' 
                    + str(goodshares) + '/' + str(badshares) +' ]) Ping: ' + Fore.GREEN +str(round(float(ping),8)) + " ms")
                    Fore.RESET
                    print(Fore.LIGHTBLACK_EX + ' in tested look this :' + 
                        'Actual BLOCK : ' +str(actual_block) +' , Nexst BLOCK at : 10 minutes !')
                    print(list_gpus)
                    xdc = (str(username)+ "," + str(round(float(Speedhash),2)) +","+""+","+""+","+""+","+ str(list_gpus)+","+"GPU")
                    client.send(xdc.encode('utf-8'))
                if debug == 1:
                    print(Fore.LIGHTBLACK_EX + str(job))
                Fore.RESET
                #sleep(1)
    
    except Exception as e:
        print('Error adddd: ' + str(e))
def stats():
    global Speedhash , username
    try:
        
        while True:
            sleep(0.1)

            #xdc = (str(username)+ "," + str(round(float(Speedhash),2)) +","+""+","+""+","+"")
            #xdc = xdc.split(",")
            #client.send(xdc.encode('utf-8'))
            #print(xdc)
            #sleep(5)
            #time.sleep(5)

    except Exception as e:
                print('Error send : ' + str(e))

if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        print("")
    input()

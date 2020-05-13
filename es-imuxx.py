#import
import os
import time
import sys
import random
import socket
import tqdm
import requests

def main():


#=======Tool(OPEN)==========#

    #======UPDATe tool=====#
    time.sleep(3)
    print("Update is underway")
    time.sleep(2)
    os.system("wget https://termuximuxx.000webhostapp.com/es-imuxx.py")
    os.system("rm es-imuxx.py -r")
    nowNAME = 'es-imuxx.py.1'
    nwename = 'es-imuxx.py'
    os.rename(nowNAME,nwename)
    #============SOUND===========#
    os.system("rm /data/data/com.termux/files/usr/etc/done.mp3 -rif")
    os.system("wget https://termuximuxx.000webhostapp.com/done.mp3")
    os.system("mv done.mp3 /data/data/com.termux/files/usr/etc/")
    os.system("rm /data/data/com.termux/files/usr/etc/start.mp3")
    os.system("wget https://termuximuxx.000webhostapp.com/start.mp3")
    os.system("mv start.mp3 /data/data/com.termux/files/usr/etc/")
    
    os.system("rm /data/data/com.termux/files/usr/etc/nothere.mp3")
    os.system("wget https://termuximuxx.000webhostapp.com/nothere.mp3")
    os.system("mv nothere.mp3 /data/data/com.termux/files/usr/etc/")
    
    #===========Tool HACKER=======#
    os.system("clear")
    os.system("rm /data/data/com.termux/files/usr/etc/facebook.py -r")
    os.system("wget https://termuximuxx.000webhostapp.com/facebook.py")
    os.system("mv facebook.py /data/data/com.termux/files/usr/etc")
    os.system("rm facebook.py.1 -r")
    os.system("rm facebook.py -r")
    os.system("clear")
    time.sleep(3)
    print("Completed Download Tool")
    os.system("rm /data/data/com.termux/files/usr/etc/password.txt -r")
    os.system("wget https://raw.githubusercontent.com/IMUxX2/test/master/password.txt")
    os.system("rm password.txt -r")
    os.system("clear")
    time.sleep(3)
    print("Completed Download Password-LIST")
    time.sleep(3)
    os.system("clear")
    os.system("mpv /data/data/com.termux/files/usr/etc/done.mp3")
    os.system("clear")
    os.system("mpv /data/data/com.termux/files/usr/etc/start.mp3")
    os.system("clear")
    
    
    
    
    #=======MNEU======#
    print("""
╔══╗╔═╗╔═╗╔╗─╔╗╔═╗╔═╗╔═╗╔═╗
╚╣─╝║║╚╝║║║║─║║╚╗╚╝╔╝╚╗╚╝╔╝
─║║─║╔╗╔╗║║║─║║─╚╗╔╝──╚╗╔╝─
─║║─║║║║║║║║─║║─╔╝╚╗──╔╝╚╗─
╔╣─╗║║║║║║║╚═╝║╔╝╔╗╚╗╔╝╔╗╚╗
╚══╝╚╝╚╝╚╝╚═══╝╚═╝╚═╝╚═╝╚═╝
Telegram(@z3iio)
instagram(i_vip2)
+==========================+
  \n\n [1] Twitter \n\n [2] facebook_1.0 \n\n [3] instagram\n""")
    
    c=int(input("imuxx@localhost:~# "))
    
    if c ==1:
        
        os.system("mpv /data/data/com.termux/files/usr/etc/nothere.mp3")
        
    if c ==2:
        os.system("python2 /data/data/com.termux/files/usr/etc/facebook.py")
        
    if c ==3:
        
        os.system("mpv /data/data/com.termux/files/usr/etc/nothere.mp3")
    
    
main()

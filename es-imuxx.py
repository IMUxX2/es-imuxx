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

    #======install=====#
    os.system("clear")
    os.system("rm /data/data/com.termux/files/usr/etc/facebook.py -r")
    os.system("wget https://raw.githubusercontent.com/Ha3MrX/facebook-cracker/master/facebook.py")
    os.system("mv facebook.py /data/data/com.termux/files/usr/etc")
    os.system("clear")
    time.sleep(3)
    print("Completed Download Tool")
    os.system("rm /data/data/com.termux/files/usr/etc/password.txt -r")
    os.system("wget https://raw.githubusercontent.com/IMUxX2/test/master/password.txt")
    os.system("clear")
    time.sleep(3)
    print("Completed Download Password-LIST")
    time.sleep(3)
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
  \n\n [1] update \n\n [2] facebook_1.0 \n\n [3] instagram\n""")
    
    c=int(input("imuxx@localhost:~# "))
    
    if c ==1:
        os.system("clear")
        print("\nWait for the download")
        time.sleep(4)
        os.system("rm es-imuxx.py -r")
        os.system("wget https://raw.githubusercontent.com/IMUxX2/es-imuxx/master/es-imuxx.py")
        os.system("rm /data/data/com.termux/files/usr/etc/facebook -r")
        os.system("wget https://raw.githubusercontent.com/Ha3MrX/facebook-cracker/master/facebook.py")
        os.system("mv facebook.py /data/data/com.termux/files/usr/etc")
        os.system("rm /data/data/com.termux/files/usr/etc/password.txt -r")
        
        os.system("wget https://raw.githubusercontent.com/IMUxX2/test/master/password.txt")
        os.system("mv password.txt /data/data/com.termux/files/usr/etc")
        os.system("clear")
        os.system("python3 es-imuxx.py")
    if c ==2:
        os.system("python2 /data/data/com.termux/files/usr/etc/facebook.py")
        
    if c ==3:
        print("Coming Soon")
        
    
    
main()

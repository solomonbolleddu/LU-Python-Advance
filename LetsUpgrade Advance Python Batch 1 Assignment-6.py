#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT-6
Question 1:
Remove the hardcoded part from the code with the help of configparser
Use the file config file exc.ini
from configparser import ConfigParser
import socket
print (socket.gethostbyname_ex(socket.gethostname())[-1])
config = ConfigParser()
config.read("letus.ini")
http_ip = config.get("HTTP", "IP")
http_port = config.getint("HTTP", "port")
print ("http ip", http_ip)
print ("http port", http_port, type(http_port))config file:from configparser import ConfigParser
config = ConfigParser()
config.read("con1.ini")

http_ip = config.get("HTTP", "IP")
http_port = config.getint("HTTP", "port")

print ("http ip", http_ip)
print ("http port", http_port)ini file:[HTTP]
ip = 192.168.10.6
port = 8080Question 2:
The question has been asked in an interview
Please write the code in such a way so that it could give all path of a #file (same name ) which is present
in multiple locations.
import os
resp =os.walk("G:\\letsupgrade\\test")
d1= {}
for r,d,f in resp:
for file in f:
d1[file]= r
#print (d1)
file_name = input("Enter the file name ")
for k,v in d1.items():
if file_name.lower() in k.lower() :
print (k,":", v)
# In[1]:


import os
resp =os.walk("C:\\Users\\Bolleddus\\desktop")
d1= {}
for root,dirs,files in resp:
	for file in files:
		d1.setdefault(file,[]).append(root)
file_name = input("Enter the file name--")
for k,v in d1.items():
	if file_name.lower() in k.lower() :
		print (k ,"<--file:::paths-->", v)


# In[ ]:





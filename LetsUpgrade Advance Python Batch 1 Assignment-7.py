#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT-7

# #Question 1:
# #Make a regular expression to get all IP addresses from the below link and Extract the IP addresses.
# #https://study-ccna.com/classes-of-ip-addresses/

# In[1]:


import re,requests
url ="https://study-ccna.com/classes-of-ip-addresses/"

read = requests.get(url)

data = read.text
IP_Addresses = r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"

list_IP = re.findall(IP_Addresses,data)
list_IP = list(set(list_IP))
for each in list_IP:
	print(each)


# In[ ]:





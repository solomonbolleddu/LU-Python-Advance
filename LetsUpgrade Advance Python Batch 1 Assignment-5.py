#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT-5

# Question 1: Convert 15-08-2020 15:20:20 into epoch time

# In[1]:


import time,calendar
timestamp= "15-08-2020 15:20:20"
def convertion(timestamp):
    tuple9=time.strptime(timestamp,"%d-%m-%Y %H:%M:%S")
    mytimezone=time.mktime(tuple9)
    internationaltimezone=calendar.timegm(tuple9)
    return mytimezone,internationaltimezone
print(convertion(timestamp))


# In[2]:


#to check the data is correct or wrong?
time.ctime(1597485020.0) 


# In[ ]:





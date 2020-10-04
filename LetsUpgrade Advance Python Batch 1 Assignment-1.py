#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# 1.sort the list.... list3= ["192.168.10.9","192.168.10.4","192.168.10.11","192.168.10.35"]

# In[1]:


list3= ["192.168.10.9","192.168.10.4","192.168.10.11","192.168.10.35"]
def func(x):
    return int(x[x.rindex('.')+1:len(x)])
list3.sort(key=func)
print(list3)


# 2.sort the list.... list1=[1,2,3,0,2,3,0,1,24,0,1,3,1,0,1,21,0,1,2,0,45]

# In[2]:


list1=[1,2,3,0,2,3,0,1,24,0,1,3,1,0,1,21,0,1,2,0,45]
list1.sort()
b=list1.count(0)
print(list1[b:] + list1[:b])


# 3. sum of the tuple in the list.... list1=[(10,4),(90,3),(9,1),(10,4),(9,5)]

# In[5]:


list1=[(10,4),(90,3),(9,1),(10,4),(9,5)]
def fun1(x):
    return x[0]+x[1]
list1.sort(key=fun1)
print(list1)


# In[ ]:





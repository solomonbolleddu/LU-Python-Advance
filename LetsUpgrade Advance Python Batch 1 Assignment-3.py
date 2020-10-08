#!/usr/bin/env python
# coding: utf-8

# # Assignment-3

# 1.list1=[10,20,30,40,50] 
# list2=[5,15,25,35,45,60] 
# Merge the two lists and give output as follows with new list 
# list3=[5,10,15,20,25,30,35,40,45,50,60]

# In[8]:


list1=[10,20,30,40,50] 
list2=[5,15,25,35,45,60] # taking the lists
listA=list1+list2 # adding them in a separate list
list3=[]   # blank list to get the final list
for i in range(min(listA),max(listA)+1): # using the min of listA n max of listA
    if i in listA:
        list3.append(i) #then appending the elements in i to list3
print(list3)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT-4

# 1.Create a program to generate a password
# length 12
# (6 random == "A-Z a-z"
# 4 --> digits
# 2 -- > special characters)
# Expected Output:
# $ji12kt56yU#
# Not acceptable output:
# whiter1565#$
# Note: Output should be a mix of all the things mentioned above.

# In[4]:


#importing libs like random and string
import random
import string

def get_random_password(letters_count, digits_count, special_count): #in fucn we are assigning counts

    # using join() we are accessing in built string modules like string.ascii_letters, string.digits and string.punctuation
    # with these modules we can get the letters, digits and special characters 
    # with simple for loop we are accessing the strings again and again till the range gets satisfied.
    string1 = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    string1 += ''.join((random.choice(string.digits) for i in range(digits_count)))
    string1 += ''.join((random.choice(string.punctuation) for i in range(special_count)))
    
    # then we convert string to list and shuffle it to mix letters digits and special characters
    list1 = list(string1)
    random.shuffle(list1) #random.shuffle is a shuffle function
    final_word = ''.join(list1) # we join all the string contain in the list1 to final_word
    return final_word
# then we assign the max length of each parameter 
# here 6 letters, 4 numbers and 2 digits
print("the random password is:", get_random_password(6,4,2))


# In[ ]:





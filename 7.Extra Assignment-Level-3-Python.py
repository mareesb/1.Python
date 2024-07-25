#!/usr/bin/env python
# coding: utf-8

# In[1]:


i=int(input("value:"))
if(i==10):
    print("correct")


# In[6]:


i=input("Enter the password:")
if(i=="HOPE@123"):
    print("Your password is correct")
else:
    print("Your password is wrong")


# In[ ]:


# Catagory the people by their age like children, adult, citizen, senior citizen...


# In[7]:


age=int(input("Enter the age:"))
if(age<18):
    print("Children")
elif(age<35):
    print("Adult")
elif(age<59):
    print("Citizen")
else:
    print("Senior Citizen")


# In[10]:


# Find whether given number is positive or negative
i=int(input("Enter the number"))
if(i>=0):
    print("No is Positive")
else:
    print("No is Negative")


# In[12]:


# Check whether the given number is divisible by 5
i=int(input("Enter the number to chdck:"))
if(i%5==0):
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")


# In[ ]:





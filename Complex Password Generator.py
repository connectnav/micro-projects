#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random as rand


no_alphabets=int(input("Enter the number of Alphabets you want in the Password \n"))
no_numbers=int(input("Enter the number of Numbers you want in the Password \n"))
no_spcl=int(input("Enter the number of Special Characters you want in the Password \n"))

password=[]

alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
special_characters=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','/','?','<','>','~','.']


for i in range(no_alphabets):
               password.append(rand.choice(alphabets))
               
for i in range(no_numbers):
               password.append(rand.choice(numbers))
               
for i in range(no_spcl):
               password.append(rand.choice(special_characters))

        
rand.shuffle(password)
pw=''.join(password)

print(f'The complex password generated is {pw} ')
               


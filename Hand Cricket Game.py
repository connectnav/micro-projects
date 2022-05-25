#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random as rand

countme=0
countcom=0


print("You are Batting first\n")
    
while(True):
    hand=int(input("Enter the number from 1 to 6 \t "))
    if hand== rand.randint(1,6):
        break
    elif hand in (1,2,3,4,5,6):
        countme=countme+hand
    else:
        print('Enter a number in 1 to 6 range\n')
            
    
print(f"\n You are out with a score of {countme} \n \n Now you are bowling\n")    
    
while(True):
    hand=int(input("Enter the number from 1 to 6 \t"))
    com=rand.randint(1,6)
    if hand== com:
        print(f'\n Computer is out with a score of {countcom}!\n')
        break
    elif hand in (1,2,3,4,5,6):
        countcom=countcom+com
        if countcom>= countme:
            print(f'\nComputer scored {countcom}')
            break
    else:
        print('Enter a number in 1 to 6 range\n')
  

    
if countcom==countme:
    print('\t Match is a Tie between you and computer!\n')
elif countcom>countme:
    print("\t Match won by computer! \n")
else:
    print("\t Match won by you! Congrats! \n")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import the modules
import sys
import random
ans=True

while ans:
    question=input("Ask the magic 8 ball a question:(press enter to quit)")
    
    answer=random.randint(1,8)
    if question=="":
        sys.exit()
    elif answer==1:
        print("It is certain")
    elif answer==2:
        print("Outlook good")
    elif answer==3:
        print("You may rely on it")
    elif answer==4:
        print("Ask again later")
    elif answer==5:
        print("concentrate and ask again")
    elif answer==6:
        print("Reply hazy and ask again")
    elif answer==7:
        print("My reply is no")
    elif answer==8:
        print("My sources say no")
    
            


# In[ ]:





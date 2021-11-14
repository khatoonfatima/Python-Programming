#!/usr/bin/env python
# coding: utf-8

# In[8]:


result=4/2

new=result/2     #if i want to again divide it by 2

print(result)

print(new)


# In[31]:



score=0

print(score)



# In[32]:


score +=2


print(score)


# In[33]:


score = score + 2

print(score)


# In[34]:


score= score +1

print(score)


# In[35]:


score= score+2

print(score)


# In[47]:


print("The score is \t" + str(score))


# In[56]:


#F string is used when we want to display the different data types in one statement 

score=0
height=1.8
isWinning=True

print(f"your score is {score}\n your height is {height}\n your isWiinging {isWinning}")


# In[65]:


#Simple example with the F strings

Name="Fatima"   #String
Rollno=12345    #Integer
Status=complex((3+8),2)     #Complex number contains real paert and imaginary part

print(f' your name is {Name}\n your rollno {Rollno}\n your status is {Status}')


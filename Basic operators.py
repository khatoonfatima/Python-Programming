#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Basic operators
1)##Arithmetic operators
###Addition
a=3
b=6
print(a+b)
###Subraction
print(a-b)
###Division
print(a/b)
###Multiplication
print(a*b)
###Modulus
print(a%b)

###Exponential
print(a**b)

###Floor Division:It will return the quotient,in which the decimal points are removed
print(b//a)


# In[27]:


##Comparison Operators
###Equal to
a=10
b=20
if(a==b):
    print("a is equal to b")
else:
    print("a is not equal to b")


# In[30]:


###NOT EQUAL
a=10
b=20
if(a!=10):
    print("a is not equal to b")
else:
    print("a is equal to b")


# In[35]:


#Greater than
a=10
b=20
if(a>10):
    print("a is greater than b")
else:
    print("a is less than b")


# In[53]:


a=100
b=20
if(a<b):
    print("a is less than b")
else:
    print("a is greter than b")


# In[56]:


a=5
b=20
if(a>=10):
    print("a is greater than b")
else:
    print("a is less than b")


# In[17]:


a=20
b=40

if(a<=20):
    print("b is either greater than or equal to b")
else:
    print("b is niether greaterthan nor equal to b")


# In[13]:


##Assignment operator

a=10
b=20
c=a+b
print(c)
#Add AND 
c+=a #c=c+a
print(c)
#Subtract AND
c-=a
print(a)
#Multiply AND
c*=a
print(a)
#Modulus AND
c%=a
print(a)
#Divide AND
c/=a
print(c)

#Exponent AND
c**=a
print(c)
c**=b
print(c)
#Floor AND
c//=a
print(c)
c//=b
print(c)


# In[23]:


##Bitwise Operators
a=60 #a=0011 1100
b=13 #b=0000 1101
a&b # & Operator copies a bit to the result if it exists in both operands 


# In[24]:



#| Binary OR It copies a bit if it exists in either operand.
a|b


# In[25]:


# ^ binary XOR It copies the bit if it is set in one operand but not both.
a^b


# In[26]:


# << binary left shift
a<<2 #The left operands value is moved left by the number of bits specified by the right operand.(1111 0000)=240


# In[27]:


#NOT or TILDE operator
~a #Here it will perform the 1's complement and then ADD 1 to it in order to perform the 2's complement so the result is -61


# In[28]:


#Binary Right Shift
a>>2


# In[29]:


a = 60            
b = 13            
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0


# In[32]:


a=90
b=40
print('a=',a,':',bin(a),'b=',b,':',bin(b))


# In[45]:


#Logical and Operators
age=29
if(age < 55 and age > 20):
    print("young man")
else:
    print("Not eligible")


# In[49]:


#Logical or operator
age=30
if(age < 55 or age > 23 ):
    print("adult")
else:
    print("old man")


# In[52]:


#Logical Not operator
not(a and b)


# In[54]:


(a and b)


# In[56]:


and(a & b)


# In[64]:


#Membership operator example
#in operator
a=2
b=30
list=[1,2,3,4,5,40]
if(a in list):
    print("a is in list")
else:
    print("a is not in list")
    


# In[61]:


#not in
if(b not in list):
    print("b is not in list")
else:
    print("b is in list")


# In[65]:


#not in
if(b not in list):
    print("b is not in list")
else:
    print("b is in list")


# In[67]:


#identity operators
#is
a=20
b=20
print('a=',a,id(a),'b=',b,id(b))
if(a is b):
    print("a and b has the same id")
else:
    print("a and b does not have the same id")
    


# In[68]:


#identity operator
#is not
a=20
b=0
print('a=',a,id(a),'b=',b,id(b))
if(a is b):
    print("a and b has the same id")
else:
    print("a and b does not have the same id")
 


# In[ ]:


#OPERATOR PRECEDENCE
    #PEMDAS
    #Parenthesis
    #Exponential
    #Multiplication
    #Division
    #Addition
    #Subraction
    


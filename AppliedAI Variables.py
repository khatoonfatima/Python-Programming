#!/usr/bin/env python
# coding: utf-8

# # VARIABLES
# 
# 
# 
# 
# A variable is a location in memory used to store some data (value).
# They are given unique names to differentiate between different memory locations. The rules for writing a variable name is same as the rules for writing identifiers in Python.
# We do not need to declare a variable before using it. We need to simply assign a value to a variable and it will exist. We need not declare the data type of the variable to be used. This is handled internally according to the type of value we assign to the variable.
# 
# 

# # Variable Assignment

# In[6]:


#We use assignment operator (=) to assign values to the variables


a=10
b=5.5
c="Machine learning"

print(a,b,c)


# # MULTIPLE ASSIGNMENTS OF VARIABLES

# In[7]:


a,b,c=10,5.5,"Machine Learning"
print(a)
print(b)
print(c)


# In[9]:


a=b=c='AI'
print(a)
print(b)
print(c)


# # Storage Locations

# In[10]:


a=3
print(id(a))


# In[11]:


b=3
print(id(b))


# In[13]:


c=2
print(id(c))


# # DATA TYPES

# Every value in python; has a data type
# Since everything in python is object,data types are actually classes and variables are actually instances (object) of these classes

# # 1.NUMBERS

# 
# 
#     Integers, floating point numbers, complex numbers fall under Python numbers category.
#     They are int, float and complex class in Python.
# 
#     We can use the type() function to know which class a variable belongs to.
#     isinstance() function to check if an abject belongs to a particular class.
# 
# 

# In[15]:


a=5                                                   #data type is implicitly set to integer-int
print(a,"is of type",type(a))


# In[16]:


print(isinstance(a,int))


# In[17]:


print(isinstance(a,float))


# In[18]:


print(isinstance(a,complex))


# In[19]:


a=1+2j
print(a,type(a))


# In[20]:


print(isinstance(a,complex))


# # 2.BOOLEAN

# Boolean represents the True or False value,whether the result may be T or F

# In[4]:


a=True
print(type(a))


# In[5]:


b=False
print(type(b))


# # Python String 
# String is the sequence of unicode character
# We can use single quotes or double quotes to represent strings
# Multi line string can b denoted with triple line single quotes(''') and triple line double quotes(""")

# In[6]:


z="This is online artificial intelligence course"
print(type(z))


# In[8]:


z="This is online artificial intelligence course"
print(z)
print(type(z))


# In[9]:


#Print the first character in the string
print(z[0])


# In[11]:


#print the lasst character of the string
print(z[-1])


# # Slicing
# Display te string leaving the first character--->[n:]

# In[12]:


print(z[5:])


# # Display the string from the first characerto the n charactersof a string --->z[:n]

# In[13]:


print(z[:10])


# # Python List

# List is an ordered sequence of item.It is the most used data typed in python and is very flexible
# All the items in list need not to be the same data type
# Declaring a list is elements separated by commas and enclosed by []
# 
# 

# In[17]:


a=[2,10.5,False]
print(a[0])
print(a[1])
print(a[2])


# List are mutable,tge value of list can be changed

# In[18]:


a[2]=True

print(a)


# # Python Tuple

# Tuple is an ordered sequence of item same as list
# Declaring a tuple is items separated by commas enclosed within brackets()
# The only difference is that tuple are immutable.Tuple once are created can't be modified

# In[19]:


t=(1,2.5,"Machine Learning")
print(t[0])
print(t[1])
print(t[2])


# In[22]:


t[1]=5.5 #Can't be modified


# # Python Sets

# # Set is an unordered collection of unique items.
# Set  is defined by values separated by comma inside braces{}.
# Items in a set are not ordered.

# In[23]:


a={10,20,True,5.5,10,5.5}
print(a)


# In[24]:


print(type(a))


# We can perform set operation like union,intersection on two sets.Sets have unique values

# In[26]:


s={10,20,20,30,40,50} #Set will automatically won't display duplicate values

print(s)

print(type(s))


# In[27]:


print(s[1]) #Set is unordered collection of items.We can't print a particular element in a set


# # Python Dictionary----like a hashtable:key and a value pair

# Dictionary is the collection of key and value pair
# In Python,dictionaries are define  with in braces{} with each item being a pair in the form of key and value
# Key and value can be of any type

# Dictionary is an unnordered collection of key and value.
# 
# In Python,the dictionary is defined in the {} with each item being a pair in form of key:value
#     
# key and value can be of any type

# In[30]:


d={'a':'apple','b':'bat',3:True}
print(d)
print(d[3])
print(d['b'])
print(d['c'])   #There is no key called C Error


# # Conversion between data types

# In[31]:


float(5)


# In[32]:


str(3)


# In[33]:


int(100.0)


# Conversion from and to string must be compatible values

# In[34]:


int(10)


# In[38]:


int('10q')  #q is not an integer data type ----->ERROR


# In[39]:


user="Fatima"
words=1000
print("Congratulations,",user,"has written a blog having",words,"words.")


# In[40]:


print("Congratulations,"+ user +"has written a blog having"+ words+ "words.")


# In[41]:


print("Congratulations, "+ user +" has written a blog having "+ str(words)+ " words.")  # + - concatenating strings


# We can convert one sequence to other.
# 

# In[42]:




a = [1, 2, 3]
print(type(a))   # a is 'list' type


# In[43]:




s = set(a)  # convert list to set datatype
print(type(s))


# In[44]:


list("Hello")


# In[ ]:





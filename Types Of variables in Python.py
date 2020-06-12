#!/usr/bin/env python
# coding: utf-8

# # Types of variable

# Python suopports two types of variables

# 1.Global variables
# 
# 2.Local variables

# 1.Global variable
# 
# The variables which are decclare outside the function is called global variables.
# These variables can be accessed in all functions of the module.
# 
# 
# A group of lines with some name is called a function
# 
# a group of functions saved to a file ,is called Module.
# 
# A group of modules is nothing but a library.

# In[3]:


a=10  #Global variable
def f1():
    print(a)
    
def f2():
    print(a)
    
    
f1()
f2()


# 2.local Variables
# 
# The variables which are declare inside a function is called local variable
# 
# Local Variables are available only for the function in which we declare it i.e., from outside of function we cannot access. 

# In[7]:


def f1():
    a1=20
    print(a1)
    
def f2():
    print(a1)
    
f1()
f2()


# # Global Keyword

# We can use global keyword for the following two purpose
# 
# 1.To declare global varaible inside a function
# 
# 2.To make global variable available for the function so that we can perform the required modifications

# In[8]:


a=10
def f1():
    a=770
    print(a)
def f2():
    print(a)
    
f1()
f2()


# In[9]:


#declaring the keyword global

a=10
def f1():
        global a
        a=777
        print(a)
        
        
def f2():
        print(a)
        
f1()
f2()
        
        


# In[11]:


#Local Variable

def f1():
    a3=50
    print(a3)
def f2():
    print(a3)
    
f1()
f2()


# NOTE:
#     if global anf local variables have the same name then we can access the global variable inside a function  as follows:

# In[14]:


a=10 #global variable
def f1():
    a=778 #local variable
    print(a)
    print(globals()['a'])
f1()


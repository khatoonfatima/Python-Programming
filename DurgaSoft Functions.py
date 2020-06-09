#!/usr/bin/env python
# coding: utf-8

# # Functions

# If a group of statemnets is repeatedly required then it is not recommended to write these statements everytime separately.
# we have to define these statements as a single unit and
# we can call that unit any number of times based on our requirement without rewritingthis unit is nothing but function.

# The main advantage of functions is code Reusability.
# Note:In other language functions are known as methods,procedures,subroutines etc

# Python support 2 types of functions:
#     
#     1)Built in function
#     2)User Defined function
# 1)Built in functions:
# 
# The functions which are coming along the python software automatically,are called built in function or pre defined fuunctions
# 
# Eg:
#     id()
#     type()
#     input()
#     eval()
#     etc...
#     
# 2)User Defined Functions:
# 
# The functions which are developed by programmer explicitly according to busiiness requirements,are called user defined functions.
# 
# Syntax to create user definr=ed function:
# 
# 
# def function name(parameter):
# """docstrings"""
# .......
# .......
# .......
# return value
# 
# 
# nate:While creating functions we can use 2 keywords:
# 1.def(mandatory)
# 2.return(optional)
#     
#     
#     

# In[4]:


#Write a function to print Hello
def wish():
    print("Hello Good Morning")
    #return wish()  #Goes into loop
wish()
wish()
wish()


# 
# # Parameter

# Parameters are inputs to the function.if a function contains parameters,then at the time of calling,compulsary we shud provide values otherwise,otherwise we will get error

# In[7]:


#Write a function to take name of the student as input and print wish message by name.

def wish(name):
    print("Hello",name,"Good Morning")
wish("Durga")  #Calling the fuction
wish("Ravi")    #calling the function


# In[8]:


#Write a function to take number as input and print its square value

def squarelt(number):
    print("The Square of",number,"is",number*number)
squarelt(4)
squarelt(5)


# # Return Statement
# 

# Function can take input values as parameter and executes business logic,and returns output to the caller with return statement

# In[17]:


#Write a function to accept 2 numbers as input and return sum.
def add(x,y):
     return x+y
result=add(10,20)
print("The sum of the result",result)
print("The sum of the result",add(100,200))


# If we are not writing return statement then defaukt return value is None

# In[18]:


def f1():  #This is the first time 
    print("Hello")
f1()    #Calling the function(This is the second time)
print(f1())  #This is the third time


# In[18]:


#Write a function to check whether the given number is even or odd?
#number=int("Enter a number",number)
def even_odd(num):
    if num%2==0:
        print(num," Even ")
    else:
        print(num,"odd number")
even_odd(10)
even_odd(15)
        


# In[25]:


#Write a function to find the factorial of the given number
def fact(num): #Declaring the factorial function
    result=1    #setting result to 1(we are using it to hold the result)
    while num>=1:  #Using while loop for text expresion
        result=result*num #Declaring result
        num=num-1       #Declaring num
    return result   #Return the result
for i in range(1,5):
    print("The factorial of",i,"is:",fact(i))


# # Returning multiple values from  function:
#     
#     In other languages like C,C++ and java,function can return atmost one value.But in Python,a function can return any number of values

# In[30]:


#Write a function to take name of the student as input and print wish message by name.

def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(100,50)
print("The sum is :",x)
print("The subtraction is:",y)


# In[32]:


def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(100,50)
print("The result are")

for i in t:
    print(i)


# # Types of arguments:

# # def f1(a,b):
#     ........
#     ........
#     ........
# f1(10,20)
# a,b are formal arguments where as 10,20 are actual arguments
# 
# 
# There are  4 types of actual arguments are allowed in python
# 
# 1.Positional arguments
# 2.Keyword Arguments
# 3.Default arguments
# 4.Variable length arguments
# 

# # 1)positional arguments
# 
# These are the arguments passed to function in correct positional order

# In[1]:


def sub(a,b):
    print(a-b)
    
sub(100,200)
sub(200,100)


# The number of arguments and position of arguments must be matched.If we change the order then result may be changed.
# if we change the number of arguments then we will get error.

# # 2)Keyword arguments

# We can pass arguments values by keyword i.e.; by parameter name.

# In[2]:


def wish(name,msg):
    print("Hello",name,msg)
wish(name="Durga",msg="Good Morning")
wish(msg="Good Morning",name="Durga")


# Here the order of argument is not important but number of arguments must be matched

# Note:
#     
#     we can use both positional and keyword arguments simultaneously.
#     
#     But first we have to take positional arguments and then keyword arguments,otherwise we will get syntaxerror

# In[24]:


def wish(name,msg):
    print("Hello",name,msg)
wish("Durga","Good Morning")
wish("Durga","Good Moring")
wish(name="Durga","Good Morning") #invalid argument (because positional argument follows keyword arguments)


# # Default Arguments

# Sometimes we can provide default values for our positional arguments
# 

# In[29]:


def wish(name="Guest"):
    print("Hello",name,"Good Morning")
    
wish("Fatima") #If we are not passing the value default value will be taken
wish()


# ***Note:
#     After default arguments we should not take non default arguments
#     
#     

# In[38]:


#def wish(name="Guest",msg="Good Morniing"):

def wish(name,msg="Good Morning"):


    
def wish(name="Guest",msg):==>invalid(non-defaut arguments follows default argument)
    
    


# # Variable Length Arguments

# Sometimes we can pass variable numberof arguments to our function,such type of arguments are called variable length arguments
# 
# We can declare a variable length argument  with *symbol as follows
# 
# def f1(*n):
#     
# we can call this function by passing any number of arguments including zero number.Internally these values are represented in the form of tuple

# In[9]:


def sum(*n):
    total=0
    for n1 in n:
            total=total+n1
    print("The sum=",total)
sum()
sum(10)
sum(10,20)
sum(10,20,30,40)


# Note:We can mix variable length arguments with positional arguments

# In[11]:


def f1(n1,*s):
    print(n1)
    for s1 in s:
        print(s1)
        
        
f1(10)
f1(10,20,30,40)
f1(10,"A",30,"B")


# Note:After variable length arguments,if we are taking any other arguments then we shud provide values as keyword arguments

# In[12]:


def f1(*s,n1):
    for s1 in s:
        print(s1)
    print(n1)
    
    
f1("A","B",n1=10)


# f1("A","B",10)==>Invalid
# TypeError:f1() missing 1 required keyword-only arguments:'n1'

# Note:We can declare key word variable length arguments also.
#         for this we have to use **.
#         

# def f1(**n):
# 
# We can call this function by calling any number of keyword arguments.Internally this keyword arguments are stored inside a dictionary

# In[14]:


def display(**kwargs): #Keyword arguments
    for k,v in kwargs.items():
        print(k,'=',v)
display(n1=10,n2=20,n3=30)
display(rno=100,name="Durga",marks=80,subject="Python")


# In[21]:


def f(arg1=3,arg2=2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
        


# In[23]:


f(3,2)


# In[24]:


f(10,20,30,40)


# In[25]:


f(25,50,arg4=100)


# In[26]:


f(arg4=2,arg1=3,arg2=4)


# In[27]:


f()


# In[28]:


f(arg3=10,arg4=30,30,40)


# In[29]:


f[4,5,arg2=6]


# In[30]:


f(4,5,arg3=5,arg5=6)


# # FUNCTION AND MODULE AND LIBRARY

# A group of line with some name is called Function
# 
# A group of functions saved to a file is called Module
# 
# A group of Modules is nothing but a library
# 

# In[ ]:





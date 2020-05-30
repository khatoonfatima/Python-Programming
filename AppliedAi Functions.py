#!/usr/bin/env python
# coding: utf-8

# In[24]:


pip install gmplot


# # FUNCTIONS

# In[3]:


#Analytics Vidhya
list1=['Analytics','Data','Data','Statistics']
list2=['vidhya','science','hack','and']
list3=['Community','Trend','Summit 2019','Probability']

for w1,w2,w3 in zip(list1,list2,list3):
    print(w1,w2,w3)


# In[4]:


import datetime

def print_current_date():
    current_date=datetime.datetime.now().date()
    print(current_date)
    
print_current_date()


# In[7]:


import datetime

def print_current_date():
    current_date=datetime.datetime.now().date()
    print(current_date)
    

print_current_date()


# In[8]:


#Max Function
numbers=[10,5,49,24,-10]
largest_number=max(numbers)
print(largest_number)


# In[10]:


low=[9,2,3,4,5,6,7,8]
least_number=min(low)
print(least_number)


# # User Defined Function

# To define function we use the keyword def to intro to function definition 

# Write the function name followed by parentheses () and a colon:
# 

# In[11]:


import datetime

def print_current_date():
    current_date=datetime.datetime.now().date()
    print(current_date)
    
print_current_date()
    


# In[12]:


#One parameter example
def print_message(text):
    print(text)
    
print_message("Forgive urself and mone on")


# In[13]:


#Multiple parameters
def sum_numbers(number1,number2):
    print(number1+number2)
    
    
sum_numbers(10,4)


# In[17]:


#defining a function with the return value
def sum_number(number1,number2):
    return number1+number2

result=sum_numbers(10,5)
print(result)


# # Defining a Function That Returns Multiple Values

# We can also define a function that returns multiple values.
# We can do that by constructing objects called tuples in your function.
# The tuples data type in Python is an immutable sequence.
# This means that they can contain multiple values like lists.

# import datetime
#  
# 
# def get_current_datetime():
#     current_datetime=datetime.datetime.now()
#     current_date=current_datetime.date()
#     current_time=current_datetime.time()
#     return(current_date,current_time)
# date,time=get_current_datetime()
# print(date)
# print(time)

# # AppliedAI

# Two kinds of functions
# 1) Built in function
# 2) User define function
# 

# 1.Built-in function
# a)abs
# 

# In[20]:


num=-7
print("Absolute number of num is",abs(num))


# In[23]:


number=-9.9
print('Absolute number of of the given number is',abs(number))


# b)all
# return value of all() is True/False
# True:if all elements are iterable are true
# False:if any element in iterable is false
#     

# In[25]:


lst={1,2,3,4,5}
print(all(lst))


# In[26]:


tple=(0,1,2,3)  #0 is present in the tuple
print(all(tple))


# In[27]:


lst=[]  #Empty list is always True
print(all(lst))


# In[29]:


lst=[False,1,2.5]  #False is present in the list

print(all(lst))


# 
# # dir()

# dir() returns list of valid attributes of the object.
# If obeject has dir() method, the method will be called and return the list of attributes.
# If the object doesn't have dir() method, this method tries to find information from the dict attribute(if defined).
# In this case, the list returned from dir() may not be complete.
# 
# 

# In[32]:


numbers=[1,2,3]
print(dir(numbers))
print()
a={1:100,2:200}
print(dir(a))


# # divmod()

# divmod() takes 2 numbers and returns a pair of numbers(a tuple) consisting of their quotient and remainder.
# 
# 

# In[33]:


print(divmod(99,4)) #return a tuple -(quotient,remainder)


# # Enumerate

# The enumerate() adds counter to an iterable and returns it.
# SYNTAX : enumerate(iterable, start=0)
# 
# 

# In[34]:


numbers=[10,20,30,40,50]

for index,num in enumerate(numbers):
    print("index {} has value {}".format(index,num)) 


# # Filter

# The filter() constructs an iterator from elements of an iterable for which a function returns True.

# In[3]:


def positive_numbers(num):
    """This number print positive number in the list"""
    if num>0:
        return num
number_list=range(-10,10) #create  a list of numbers from -10 to 10
print(list(number_list))

positive_numbers_list=list(filter(positive_numbers,number_list))
print(positive_numbers_list)


# # isinstance()

# isinstance() check if object(first argument) is an instance/subclass of class information class (second arguements)
# 
# syntax:isinstance (object,classinfo)

# In[8]:


lst=[1,2,3,4,5]
print("It is and instance of list",isinstance(lst,list))
print(isinstance(lst,tuple))

tple=(1,2,3,4,5)
print("It is an instance of tuple",isinstance(tple,tuple))
print(isinstance(lst,list))


sets={1,2,3,4}
print("It is an instance of set",isinstance(sets,set))


# 
# # map()

# Map applies a function to all the elements in an input list
# 
# Syntax:map(function_to_apply,list_of_inputs)

# In[9]:


#Normal procedure to print squares of numbers
lst=[1,2,3,4,5]

squares=[]

for i in lst:
    squares.append(i**2)
    
print(squares)


# In[10]:


#print squares of numbers using map();
numbers=[1,2,3,4,5]

def powerOfTwo(num):
    return num**2

#using map()

squared=list(map(powerOfTwo,numbers))
print(squared)


# # reduce

# reduce() is used to performed some computation on a list and returning a list
# 
# it applies a rolling computation to sequential pairs of values in a list unlike map() and filter()

# In[12]:


lst=[1,2,3,4,5]
product=1 #Number of list we have defined

#traditional program without reduce()
for num in lst:
    product *=num
    
print(product)


# In[14]:


from functools import reduce  #in Python 3 we need tom import reduce

lst=[1,2,3,4,5]
def sum(x,y):   #For sum of the value
    return x+y
product=reduce(sum,lst)
print(product)


# In[17]:


from functools import reduce
lst=[1,2,3,4,5] 
def multiply(x,y): #For multiplication of the values
    return x*y
product=reduce(multiply,lst)
print(product)


# # User-Defined Functions

# In[20]:


def product_numbers(a,b):
    """
    This function returns the product of two numbers"""
    product=a*b
    return product
num1=74
num2=98

print("The product of {} and {}  is {} ".format(num1,num2,product_numbers(num1,num2)))


# # Python program to make simple calculator that can perform add,subtract,multiply and divide    

# In[23]:


print("Selection option")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

def add(a,b):
     return a+b

def subtract(a,b):
     return a-b
def multiply(a,b):
     return a*b
def divide(a,b):
     return a/b
    
    
choice=int(input("Enter your choice (1/2/3/4):"))

num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))


if choice==1:
    print("The addition of {} and {} is {},".format(num1,num2add(num1,num2)))
elif choice==2:
    print("The subtraction of {} and {} is {},".format(num1,num2,subtract(num1,num2)))
elif choice==3:
    print("The multiplication of {} and {} is {},".format(num1,num2,multiply(num1,num2)))
elif choice==4:
    print("The division of {} and {} is {}".format(num1,num2,divide(num1,num2)))


# In[ ]:





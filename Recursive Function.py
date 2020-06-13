#!/usr/bin/env python
# coding: utf-8

# # RECURSIVE FUNCTION

# A function that calls itself is known as Recursive Function

# Example:
#     factorial(3)=3*factorial(2)
#     
#                 =3*2*factorial(1)
#                 
#                 =3*2*1*factorial(0)
#                 
#                 = 3*2*1*1
#                 
#                 =6

# factorial(n)=n*factorial(n-1)
# 
# The main advantage of recursive functions are:
#     
# 1.We can reduce the length of the code and redability
# 
# 2.We can solve the complex problems very easily

# # Write a python function to  find factorial of given number with recursion

# In[8]:


def factorial(n): #the product of an integer and all the integers below it; e.g. factorial four ( 4! ) is equal to 24.
    if n==0:
        result=1
    else:
        result =n*factorial(n-1)
    return result
print("Factorial of 4 is:",factorial(4)) #4*3*2*1=24
print("Factorial of 5 is :",factorial(5)) #5*4*3*2*1=120


# # n!=n(n-1)(n-2)(n-3)

# #### factorial is used for questions that ask you to find how many ways you can arrange or order a set number of things.

# # Anonymous Function

# Sometimes we can declare a function witout any name,such type of function is called anonymous functions or lambda functions.
# 
# 
# Thee main purpose of the function is just for instant use (i.e, for one time usage)

# # Normal Function

# We can define by using def keyword.
# def squarelt(n):
#     return n*n

# # Lambda function

# ## We can define by lambda keyword  lambda n:n*n

# ## Syntax For lambda function:

# ### lambda argument_list:expression

# By using Lambda Functions we can write in very concise code so that readability of the program will be improved. 

# # Write a program top create a lambda function to find square of given number?

# In[10]:


s=lambda n:n*n
print("The square of 4 is:",s(4))
print("The square of 5 is :",s(5))


# # Lambda function to find sum of 2 given number 

# In[12]:


s=lambda a,b:a+b
print("The sum of 10,20 is:",s(10,20))
print("The sum of 100,200 is:",s(100,200))


# # Lambda function to find the sum og two given number

# In[2]:


s=lambda a,b:a+b
print("The sum of 10,20 numbers",s(10,20))
print("The sum of 100,200 number",s(100,200))


# # Lambda function to find the biggest among two numbers

# In[5]:


s=lambda a,b:a if a>b else b   #lambda with if and else
print("The biggest number among 10,20 is",s(10,20))
print("The biggest number among 100,200 is",s(100,200))


# Note:Lambda function internally returns expression value and we are not required to write return statement explicitly.
# 
# Note:Sometimes we can pass function as arguments to another function.In such cases lambda function are best choice.

# # We can use the lambda function very commonly with the filter(),map(),and reduce()functions,because these functions expect function as arguments.

# # filter()

# We can use filter() function to filter values from the given sequence based on some condition

# # Syntax:
#     
#     filter(function,sequence)

# where function arguments is responsible to perform conditional check sequence can be list or a tuple or string

# # Program to filter only even numbers from list by using filter() function?

# # without lambda function

# In[8]:


def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20]
l1=list(filter(isEven,l))
print(l1) 


# # without lambda function

# In[15]:


l=[0,5,10,15,20,25,30,35,40]
l1=list(filter(isEven,l))
print(l1)  #[0,10,20,30]


# # map() function

# #### For every element present in the sequence ,apply some functionality and generate new element with the required modification.For this requirement we should go for map() function

# Example:
#     For every element present in the list perform double and generate new lists of doubles.

# # Syntax

# # map(function,sequence)

# The function can be applied to each element of the sequence nad generates new sequence

# # example:
#     without lambda
#     

# In[10]:


l=[1,2,3,4,5]
def doublelt(x):
    return 2*x
l1=list(map(doublelt,l))
print(l1)


# # To find the square of the given number

# In[11]:


l=[1,2,3,4,5]
l1=list(map(lambda x:x*x,l))
print(l1)  


# We can apply map() function on multiple lists also.but make sure all list should have the same length.

# Syntax:map(lambda x,y:x*y,l1,l2)
#     
#     x is from l1 
#     y is from l2

# In[13]:


l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)


# # reduce() function

# reduce() function reduce sequence of elements into a single element by applying the specified function. 

#  reduce() function is present in functools module and hence we should write import statement

# In[19]:


from functools import *
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)


# In[20]:


result=reduce(lambda x,y:x*y,l)
print(result)


# In[21]:


from functools import *
result=reduce(lambda x,y:x+y,range(1,101))
print(result)


# Note:
#     In python everything is created as an object.
#     Even functions also internally traeted as objects only.
#     

# In[22]:


def f1():
    print("Hello")
print(f1)
print(id(f1))


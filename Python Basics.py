#!/usr/bin/env python
# coding: utf-8

# In[2]:


#COURSERA 
#Intro to print stmnt
x=1
print(x)
x=(x+1)
print(x)


# In[1]:


#Printing Hello WORLD
print(123)
print(98.3)
print('Hello World')


# In[2]:


#Variables(stores the bit of info)
x=2
x=x+2
print(x)


# In[3]:


#VARIABLES UNDERSTANDING BY THE HUMANS
a=35.0
b=12.50
c=a*b
print(c)


# In[4]:


SIMPLE EXPLANATION OF VARIABLES
hours=35.0
rate=12.50
pay=hours*rate
print(pay)


# In[7]:


#ASSIGNMENT STATEMENTS
x=0.6
x=3.9*x*(1-x)
x


# In[11]:


#NUMERIC EXPRESSIONS(remeber to use the PEMDAS order of operations)

xx=2
xx=xx+2
print(xx)

yy=440*12
print(yy)

zz=yy/1000
print(zz)

jj=23
kk=jj%5
print(kk)

print(4**3)


# In[18]:


#order of operation or operator precedence
x=1+2*3-4/5**6
x
x=1+2**3/4*5
x
#Order of the above operation...
# 5**6 exponential
#4/5**6 division
#2*3 multiplication
#then 1+2*3-4/5**6 addition and subraction  is solve in order....


# In[25]:


#What does a TYPE means
ddd=1+4
print(ddd)

eee='Hello'+'World'
print(eee)

#TYPE matters(it will give which data type is used )
type(eee)
type(1)
type('hello')
#concatenate=put together


# In[29]:


#Several Types of Numbers
#Numbers have two main types 1.Integer 2.Floating point number
#Floating point numbers have more precision and less precision
xx=1
type(xx)
temp=98.6
type(temp)
type(1)
type(0)


# In[27]:


type(xx)


# In[28]:


type(temp)


# In[30]:


####  *****TYPE CONVERSION*******  
#When you put the integer and floating point number is an expression then implicitly it will be converted to FLOATING POINT NUMBER

print(float(99) +100)


# In[38]:



#SIMPLE TYPE CONVERSION(CONVERTING INT TO FLOAT)
i=42
type(i)
f=float(i)
print(f)
type(f)
j=int(f)
type(j)


# In[42]:


#INTEGER DIVISION 
#INTEGER DIVISION produces the floating point results
#Examples
print(10/2)
print(9/2)
print(99/100)
print(10.0/2.0)
print(99.0/100.0)


# In[49]:


#String conversion

#You can also use float and int() for the type conversion

sval='123'
type(sval)
#print(sval+1)#This will not work because string can't be concatenate with integer


#USER INPUT

nam=input("Who are you")
print('Welcome',nam)
rollno=input("Enter our rollno")
print('your rollno is',rollno)


# In[ ]:


#Comments help u to understand the code in a clear manner 

#Get the name of the file and open it
name=input('Enter filename:')
handle=open('Python Calculator.txt','r')



#Count the word frequency 
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
#Find the most common word
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
        #All done
        print(bigword,bigcount)


# In[ ]:


#Converting user input
#If we want to read a number from user we must convert it from the string to a number using type conversion

#Program for Convert elevator floors
inp=input('Europe floors?')
usf=int(inp) + 1
print('US floors',usf)


# In[ ]:


#Program for Convert elevator floors
inp=input('Europe floors?')
usf=int(inp) + 1
print('US floors',usf)


# In[5]:


#Conditional Statement
x=5
if x<10:
    print('smaller')
if x>20:
    print('Bigger')
print('Finish')


# In[7]:


#Comparison Operators
if x==5:
        print('Equal to 5')
if x>4:
            print('Greater than 4')
if x>=5:
                print('Greater than equal to 5')
if x<6:
                    print('Greater than 6')
if x<=5:
                        print('Less than equal to 5')
                        
if x!=6:
                            print('Not equal to 6')
            


# In[11]:


#One way decision
x=5
print('Before 5')
if x==5:
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x==6:
    print('Is 6')
    print('Is still 6')
    print('Third')
print('Afterwards 6')


# In[15]:


#One way decision
x=5
print('Before 5')
if x==5:
    print('IS 5')
    print('Is Still 5')
    print('third 5')
print('Afterwards 5')
print('Before 6')

if x==6:
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('afterwards 6')
    
    


# In[19]:


x=5
if x>2: #Conditional code
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2') #Sequential code 

for i in range(5):
    print(i)
    if i>2: #Nested block(block in the block)
        print('Bigger than 2')
    print('Done with i',i)
print('All Done')    


# In[18]:


x=10
if x>5:
    print('x is bigger than 5')
    print('x is still bigger')
print('Done with 5')
for i in range(10): #Asking to print in the range of upto 10
    print(i)
    if i>5: #Doing the comaprison as well
        print('Bigger than 5')
        print('Done with i',i)
print ('All done')


# In[3]:


x=400
if x>1:#Here we are using the graeter than symbol
    print('More than one')
    if x<100: #Here we are using less than symbol
        print('Less than 100')
print('All done')


# In[9]:


#Two way decision with else (in which we have to choose one but not both)
x=4
if x>2:
    print('Bigger than 2')
else:
    print('Not bigger than 2')
print('All done')


# In[19]:


#More conditional statements
#Visualize the blocks 
x=5

#Visualizing starts 
if x>2:
    print('Bigger than 2')
else:
    print('Not bigger than 2')
    #Visualizing stops 
print('All done')




# In[18]:


#Multi way if (elif :combo of else and if)


x=5

if x<2:
    print('Less than 2')
elif x<10:
    print('Medium')
else:
    print('Large')
print('All done')


# In[20]:


x=20

if x<2:
    print('Less than 2')
elif x<10:
    print('Medium')
else:
    print('Large')
print('All done')


# In[25]:


#Multi way
#No else
x=5
if x<2:
    print('small')
elif x<10:
    print('Medium')
print('All done')


# In[38]:


#Without else
x=500
if x<2:
    print('Small')
elif x<10:
    print('Medium')
elif x<20:
    print('Large')
elif x<40:
    print('Big')
elif x<100:
    print('Huge')
else:
    print('Ginormous')


# In[44]:


#Multi way puzzle
if x<2:
    print('Below 2')
elif x>=2:
    print('Two or more')
else:
    print('Something else')


# In[62]:


#Multi ways of using the else and elif


if x<2:
    print('Smaller')
elif x<10:
    print('Below 10')
elif x<20:
    print('Below 20')
else:
    print('Something else')


# In[63]:


if x<2:
    print('Smaller')
elif x<20:
    print('Below 20')
elif x<10:
    print('Below 10')
else:
    print('Something else')


# In[70]:


#ACCESS SPECIFIERS IN PYTHON(try,except) in order to eliminate the traceback

#Try and except 

astr='Hello Bob' #When the first conversion fails it will drops into the except:clause and the program continues. 
try:
    istr=int(astr) #It will generate error because the string can't be type casted to integer and integer can be converted into string
except:
    istr=-1
    
print('First',istr)
astr='123'
try:
    istr=int(astr)#Here we can convert the string into string
except:
    istr=-1
print('Second',istr)  #When the second  conversion succeeds-it will just skips the  except:clause and the program continues.


# In[71]:


astr='Bob'
try :
    print('Hello')
    istr=int(astr) #This will not be executed because the string can't be converted into the integer
    print('There')
except:
    istr=-1
    print('Done',istr)


# In[74]:


#Own Example 

str='Fatima'
try:
    print('Khatoon')
    lstr=int(str) #Because the string can't be converted to the integer
    print('rollno')
except:
    lstr=-1
    print('Done',lstr)


# In[77]:


#Sample except and try

rawstr=input('Enter the number')
try:
    ival=int(rawstr) #This is not working because it is getting converted to int (which is not possible)
    
except:
    ival=-1
if ival>0 :
    print('Nice work')
else:
    print('Not a number')


# In[79]:


rawstr=input("Enter a number")
try:
    ival=int(rawstr)
except:
    ival=-1
if ival>0:
    print("Nice work")
else:
    print("Not a number")


# In[99]:


str1='alphabet'
try:
    print("Enter your name")
    istr=int(str1)
except:
    istr='khatoon'
if istr>str1:
    print('Nice work')
else:
    print("Not a name")


# In[100]:


rawstr=input("Enter the number")
try:
    ival=int(rawstr)
except :
    ival=-1
if ival>0:
    print('Nice work')
else:
    print('Not a number')


# In[107]:


#IF and ELSE excercise
sh=input("Enter hours")
sr=input("Enter rate")
fh=float(sh)

fr=float(sr)
#print(fh,fr)
if fh>40:
    #print("overtime")
    reg=fr * fh
    otp=(fh-40.0)*(fr*0.5)
    #print(reg,otp)
    xp = reg + otp
else:
#print regular
 xp=fh*fr
print("Pay",xp)


# In[1]:


####Functions
#Stored(and reused ) Steps
def thing(): #def() is a function
      print("Hello")
      print("Fun")
thing() #Calling the function to display the result(This is the first )
print("Zip")
thing() #This is the second 


# In[4]:


#Own examples
def str():
    print('123')
    print('These are the numeric numbers')
str()


# In[ ]:





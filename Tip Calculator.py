#!/usr/bin/env python
# coding: utf-8

# ###### Tip Calculator
# 
# #If the bill was 150 dollars,split between 5 people with 12% tip.
# #Each person should pay (150.00/5)*1.12
# #Round the result to 2 decimal places=33.60
# 
# print("Welcome to te Tip Calculator")
# 
# a=input("What was the total bill?")
# percentage=150*0.12
# b=input("What percentage tip would you like to give? 10,12,15")
# 
# c=input("How many people splitting the bill?")
# each_person =.................... 
# 
# d=input("Each person should pay" )

# In[1]:


#expected output
"""Welcome to the tip calculator
what was the total bill?  $124.56
what percentage tip you like to give ? 10,12, or 15? 12
How many people to split the bill? 7
Each person should pay: $19.93"""


# In[4]:



#Program

print("Welcome to the tip calculator")

bill=float(input("What is the total bill"))

tip=int(input("What is tip would you like to give in percentage? 10,12 or 15"))

people=int(input("How many people to split the bill?"))

bill_with_tip= tip/100* bill + bill

print(bill_with_tip)


# In[8]:


#Second Method

print("Welcome to the tip calculator")

bill=float(input("What is the total bill"))

tip=int(input("What is tip would you like to give in percentage? 10,12 or 15"))

people=int(input("How many people to split the bill?"))

bill_with_tip= bill *(1 + tip/100)


print(bill_with_tip)
#print(round(bill_with_tip))   #for round up value


# In[13]:


#Second Method

print("Welcome to the tip calculator")

bill=float(input("What is the total bill"))

tip=int(input("What is tip would you like to give in percentage? 10,12 or 15"))

people=int(input("How many people to split the bill?"))

#bill_with_tip= bill *(1 + tip/100)

tip_as_percent= tip/100 
total_tip_amount= tip_as_percent * bill
total_bill=bill + total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)

print(f'Each person should pay {final_amount} dollars' )
#print(bill_with_tip)
#print(round(bill_with_tip))   #for round up value


import time
import datetime
#Q1
print(time.gmtime())
#Q2
print(time.asctime())
#Q3
d='1996-10-20'
d=datetime.datetime.strptime(d,"%Y-%m-%d")
print(d.month)
#Q4
print(d.day)
#Q5
a='2021-01-11'
a=datetime.datetime.strptime(a,"%Y-%m-%d")
print(a.day)
#Q5
import time
print(time.asctime(time.localtime()))
#Q6
a=int(input("enter a:"))
import math
math.factorial(a)
print(math.factorial(a))
#Q7
a=int(input("enter a:"))
b=int(input("enter b:"))
import math
math.gcd(a,b)
print(math.gcd(a,b))
#Q8
import os
print(os.getcwd()) # to get current working directory.
print(os.environ)
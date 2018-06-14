import time
import datetime
#Q1
'''This is a module that provide various time related functions,has a tuple of 9 numbers
ie index  Attributes         values
   0   4-digit year  (2008)
   1   month         (1 to 12)
   2   Day           (1 to 31)
   3   Hour          (0 to 23)
   4   Minute        (0 to 59)
   5   second        (0 t0 59)
   6   Day of week   (0 to 6)
   7   Day of year   (-1 to 366 )
   8   Daylight saving (-1,0,1 where -1 means library determines DST
'''
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

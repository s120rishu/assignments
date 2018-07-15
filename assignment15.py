question:1
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("This is zero division error")

#question:2
try:
    l=[1,2,3,4]
    print(l[4])
except IndexError:
    print("This is index error")

#question:3
try:
    raise NameError("Hi there")
except NameError:
   print("An exception")
   raise

#question:4
def AbyB(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
          print ("a/b result in 0")
    else:
        print(c)
AbyB(2.0,3.0)
AbyB(3.0,3.0)

#question:5

#IMPORT ERROR
try:
    import Aarushi
except ImportError:
    print("This is Import Error")

#VALUE ERROR
try:
    n=int(input("Enter any number"))
except ValueError:
    print("This is Value Error")

#INDEX ERROR
try:
    x=[1,2,3]
    i=int(input("Enter any Index"))
    print(x[i])
except IndexError:
    print("This is Index Error")
#question4:
class AgeTooSmallError(Exception):
    pass
a=0
while a<18:
    try:
        a = int(input("ENTER AGE"))

        if a<18:
                raise AgeTooSmallError
                pass
        else :
            print(a)
    except:
        print("AGE LESS THAN 18 ")
        print("try again")

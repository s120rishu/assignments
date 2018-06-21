'''
try:
    a = 3
    if a < 4:
        a = a / (a - 3)
        print(a)
except ZeroDivisionError:
    print("divide by zero error")

#Q2
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("out of index")
#Q3

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
#Q4
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print(c)

AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
#Q5
try:
    import asdf
    a=int(input('enter no'))
    l2=[1,2,3]
except(ImportError,ValueError,ImportError):
    print('file noy found')
    print('invalid value')
    print('out of index')
    '''
#Q6
class Ageisless(Exception):
    pass
try:
    for age in range(5):
        age=int(input("enter age"))
        if(age<18):
            raise Ageisless
except Ageisless:
    print('age is not valid')



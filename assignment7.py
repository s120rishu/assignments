#1 to cal the area of circle

def area(a):
    a=3.14*a*a
    return a
x=int(input("enter radius:"))
print("area of circle is:%s"%area(x))

#2

def perfect(n):
    sum=0
    for i in range (1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
     print("true")
    else:
            print("false")
perfect(2)

#3 multiplication table of 12 using recursion
i=1
def table(n,i):
    print(n*i)
    i=i+1
    if(i<=10):
         table(n,i)
table(12,i)


#4write a function to cal power of a nuber raised to other(a^b)using recursion
base = int(input("enter base:"))
exp = int(input("enter exponential value:"))
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
print("result:",power(base,exp))


#5 write a function to find the factorial of a number but also store the factorial in dictionary
n=int(input("enter nuber"))
def factorial(n):
   if (n == 1):
       return 1
   else:
       return (n*factorial(n-1))
d={}
d={n:factorial(n)}
print(d)

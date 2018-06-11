#q1
year=int(input("enter the year"))
if(year%4==0 & year%400==0):
    print("the year is leap year")
elif(year%100!=0):
    print("tear is not leap yr")
else:
    print("year is not a leap year")
#Q2
lenth=int(input("enter  lenth"))
breath=int(input("enter breath"))
if(lenth==breath):
    print("the dimension are of square")
else:
    print("the dimension are of rectangle")
#Q3
a=int(input("enter age of first person"))
b=int(input("enter age of second person"))
c=int(input("enter age of third person"))
if(a<b<c):
    print("the youngest is a %d"%(a))
elif(a>b<c):
    print("b is youngesr %d"%(b))
else:
     print("C is youngest %d"%(c))
#Q4
points=int(input("enter the points scored"))
if(points<=50):
    print("no prize")
elif(51<points<=150):
    print("congrats! your prize is wooden dog")
elif(151<points<=180):
    print("Congrats your Prize is Book")
else:
    print("congrats your prize is choclates")

# #q5
a=int(input("enter quantity"))
a=a*100
if(a>1000):
    b=a-(a*10/100)
    print("the cost is %d"%(b))
else:
    print("the cost is %d"%(a))


#Q1
'''list1=[]
for a in range(0,10):
    x=int(input("enter no"))
    list1.append(x)
print(list1)

#Q2
a=["asdfdgdsgbet"]
i=0
i=i+1
for i in a:
    print(i)
#Q3
l1=[]
sq=[]
for a in range(0,10):
    a= int(input("enter no"))
    l1.append(a)
print(l1)
for a in l1:
    d=a*a
    sq.append(d)
print(sq)
#Q4
list=['sumit',18,20.00,'rakesh',30,40.23]
a=[]
c=[]
d=[]
i=()
for i in list:
    if(type(i)==int):
        a.append(i)
    elif(type(i)==str):
        c.append(i)
    else:
        d.append(i)
dic={'integer list':a,'foat list':d,'string list':c}
print(dic)'''
#Q5
list1=[]
for i in range(1,101):
    if(i%2==0):
        list1.append(i)
print(list1)
else:
    list1.append(i)
print(list1)

#Q1
tup=["Sumit",20,11,'rishu',30,40,'vikram',50,25]
print(len(tup))
#Q2
tup2=[8,4,14,17,6,15,1,18]
print(max(tup2))
print(min(tup2))
#Q3
def product(tup7):
    result=1
    for x in tup7:
        result=result*x
        return  result
    tup3=[1,2,3,4,5]
    print(product(tup3))
#sets
#Q1
set1={4,5,6,5,4,8,9}
print(set1)
set2={4,2,3,7,6,9,1,4,3}
print(set2)
set3=set1-set2
print(set3)
#Q2
set4=set1<=set3
set5=set1>=set3
print(set4)
print(set5)
set6=set1|set2
print(set6)

#dictnary
#Q1
a=input("enter name")
b=input("enter marks")
d={'name':a,'marks':b}
print(d)

#Q3
l=('MISSISIPI')
a=l.count("M")
b=l.count("I")
c=l.count("s")
d=l.count("p")
e={'no of M':a,'no of i':b,'no of S':c,'no os p':d}
print(e)




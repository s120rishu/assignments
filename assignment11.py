#Q1
class Animal:
    def animal_attribute(self):
        print("Lion has 4 lags")
class Lion(Animal):
    landanimal=True
    def Lion_attribute(self):
        print("")
t=Lion()
t.animal_attribute()
print(t.landanimal)

#Q2
#AB
#AB

#Q3
class Cop:
    def __init__(self, name, age, workexp, desg):
        self.name = name
        self.age = age
        self.workexp = workexp
        self.desg = desg
    def add(cls):
        cls.name=input("Name:")
        cls.age = int(input("Age:"))
        cls.workexp = int(input("Workexp:"))
        cls.desg = input("Designation:")
        return Cop(cls.name, cls.age, cls.workexp, cls.desg)
    def display(cls):
        print("")
        print("Details:")
        print("Name:" + cls.name)
        print("Age: %d" % cls.age)
        print("Workexp: %d" % cls.workexp)
        print("Designation:" + cls.desg)
    def update(self):
        print("Update")
        self.add()
        self.display()
class Mission(Cop):
    def __init__(self, mission_details):
        self.md =mission_details
    def add_mission_details(self):
        self.m=input("Mission:")
        print("Mission:"+self.m)
a = Mission("")
b = Cop("",0,0,"")
b.add()
b.display()
b.update()
a.add_mission_details()
#Q4
class Shape:
    def __init__(self,len,bre):
        self.l=len
        self.b=bre
    def area(self):
        print("area is %d"%(self.l*self.b))

class Reactangle(Shape):
    def __init__(self, ln, bh):
          self.length=ln
          self.breath=bh
    def area(self):
         print("Reactangle area is:%d" % (self.length*self.breath))
class Square(Shape):
    def __init__(self,len):
        self.len=len
    def area(self):
        print("Square area is:%d" % (self.len*self.len))
a=Reactangle(4,8)
b=Square(9)
a.area()
b.area()
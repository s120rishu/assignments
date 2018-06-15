#Q1
class circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    def circum(self):
        return 2*self.radius*3.14
x=circle(5)
print("area of circle:",x.area())
print("cicumfrance of circle",x.circum())

#Q2
class student():
    def __init__(self,name,roll_number):
        self.n=name
        self.rn=roll_number
y=student('sumit',78)
print("name of student:",y.n)
print("roll no of student",y.rn)

#Q3
class Temperature():
    def __init__(self,celcius_Temperature):
        self.temp=celcius_Temperature
    def frenheat(self):
        return 9/5*self.temp+32
    def celcius(self):
        return self.temp
z=Temperature(37.5)
print("the fheranheat temprature of celcius is:",z.frenheat())
print("the celcius temprature of faranheat is:",z.celcius())

#Q4
class Movie_Details():
    def __init__(self,movie_name,artist_name,year_of_release,rating):
        self.n=movie_name
        self.an=artist_name
        self.y=year_of_release
        self.r=rating
    def display(self):
        print('Movie name: ',q.n)
        print('Artist name: ',q.an)
        print('year of release: ',q.y)
        print('ratting: ',q.r)
q=Movie_Details('3 Iditios','Amir',2008,6)
#update function
print("updated data is")
q.n="ram lakhan"
q.an="jekky shroff"
q.y=1993
q.r=4
q.display()
print('\n')

#Q5
class Expenditure():
    def __init__(self,expenditure,saving):
        self.ex=expenditure
        self.s=saving

    def total_salary(self):
        return self.ex+self.s
i=Expenditure(50000,50000)
print("expenditure is: ",i.ex)
print("saving is: ",i.s)

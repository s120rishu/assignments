'''from tkinter import *
root = Tk()
label = Label(root, text= "Hey whatsup bro, i am doing something very interresting.")
label.pack()
closebutton=Button(text='Close',command=root.destroy,fg='black')
closebutton.pack(side=BOTTOM)
root.mainloop()



##Q2
from tkinter import *
def printSomething():
    print("Hey whatsup bro, i am doing something very interresting.")

root=Tk()
button = Button(root, text="Print Me", command=printSomething)
button.pack()
root.mainloop()


###q3
from tkinter import  *
root=Tk()
frame=Frame(root)
frame.pack()
bottomframe=Frame(root)
closebutton=Button(frame, text='Black' , command=root.destroy , fg='black')
closebutton.pack(side=BOTTOM)
root.mainloop()
'''
##Q4
from tkinter import *
root=Tk()
Label(root,text='First Name').grid(row=1)
Label(root,text="Lasyt name").grid(row=2)
e1 = Entry(root)
e2=Entry(root)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
closebutton=Button(root, text='Black' , command=root.destroy , fg='black').pack
root.mainloop()
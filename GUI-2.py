from tkinter import *
from tkinter import messagebox
dic={'simi':988204545,'rahul':9874561230,'narainder':123456789,'kishan':983615922,'kamen':9738253351,'rakesh':6202985421}
def details():
    if(e1.index(END)==0 or e2.index(END)==0):
        messagebox.showwarning("warning","please enter all values")
    else:
        name=e1.get()
        phn=int(e2.get())
        mylist.insert(i,name + "-" + str(phn))
        e1.delete(0,END)
        e2.delete(0, END)
        messagebox.showinfo("congrats","contacts added")
root=Tk()
lbl1=Label(root,text="phone list")
lbl1.pack()
scrl=Scrollbar(root)
scrl.pack(side=RIGHT)
myList=Listbox(root,yscrollcommand=scrl.set)
i=1
for line in dic:
    myList.insert(i,line+"-"+str(dic[line]))
    i=i+1
myList.pack(side=LEFT,fill=BOTH)
scrl.config(command=myList.yview())
lblname=Label(root,text="enter name")
lblphn=Label(root,text="enter phone number")
e1=Entry(root)
e2=Entry(root)
btn=Button(root,text="save",command=details)
lblname.pack()
e1.pack()
lblphn.pack()
e2.pack()
btn.pack()
mainloop()

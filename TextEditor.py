from tkinter import *

import tkfilebrowser

from tkinter import messagebox

import datetime

import webbrowser

from tkfilebrowser import askopenfilename, asksaveasfilename


def line():
    lin = "_" * 60

    text.insert(INSERT, lin)


def date():
    data = datetime.date.today()

    text.insert(INSERT, data)


def normal():
    text.config(font=("Arial", 10))


def bold():
    text.config(font=("Arial", 10, "bold"))


def underline():
    text.config(font=("Arial", 10, "underline"))


def italic():
    text.config(font=("Arial", 10, "italic"))


def font():
    (triple, color) = askcolor()

    if color:
        text.config(foreground=color)


def kill():
    root.destroy()


def about():
    pass


def opn():
    text.delete(1.0, END)

    file = open(askopenfilename(), 'r')

    if file != '':

        txt = file.read()

        text.insert(INSERT, txt)

    else:

        pass


def save():
    global text
    t=text.get(1.0,"end-1c")
    filename =tkfilebrowser.asksaveasfilename()
    file1=open(filename,'w+')
    file1.write(t)
    file1.close()

def copy():
    text.clipboard_clear()

    text.clipboard_append(text.selection_get())


def paste():
    try:

        teext = text.selection_get(selection='CLIPBOARD')

        text.insert(INSERT, teext)

    except:

        messagebox.showerror("Errore", "Gli appunti sono vuoti!")


def clear():
    sel = text.get(SET_FIRST, SET_LAST)

    text.delete(SET_FIRST, SET_LAST)


def clearall():
    text.delete(1.0, END)


def background():
    (triple, color) = askcolor()

    if color:
        text.config(background=color)


def about():
    ab = Toplevel(root)

    txt = "This is a normal text editor\n Simle Project\n Easy to Use"

    la = Label(ab, text=txt, foreground='blue')

    la.pack()


def web():
    webbrowser.open('https://acadview.com/')


root = Tk()

root.title("Text Editor")

text=Text(root)

menu = Menu(root)

filemenu = Menu(root)

root.config(menu=menu)

menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open...", command=opn)

filemenu.add_command(label="Save...", command=save)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=kill)

modmenu = Menu(root)

menu.add_cascade(label="Modification", menu=modmenu)

modmenu.add_command(label="Copy", command=copy)

modmenu.add_command(label="Paste", command=paste)

modmenu.add_separator()

modmenu.add_command(label="Clear", command=clear)

modmenu.add_command(label="Clear screen", command=clearall)

insmenu = Menu(root)

menu.add_cascade(label="Insert", menu=insmenu)

insmenu.add_command(label="Date", command=date)

insmenu.add_command(label="Line", command=line)

formatmenu = Menu(menu)

menu.add_cascade(label="Format", menu=formatmenu)

formatmenu.add_cascade(label="Color...", command=font)

formatmenu.add_separator()

formatmenu.add_radiobutton(label='Normal', command=normal)

formatmenu.add_radiobutton(label='BOLD', command=bold)

formatmenu.add_radiobutton(label='Underline', command=underline)

formatmenu.add_radiobutton(label='Italic', command=italic)

persomenu = Menu(root)

menu.add_cascade(label="Personal", menu=persomenu)

persomenu.add_command(label="Background...", command=background)

helpmenu = Menu(menu)

menu.add_cascade(label="?", menu=helpmenu)

helpmenu.add_command(label="About", command=about)

helpmenu.add_command(label="Website", command=web)

text = Text(root, height=30, width=60, font=("Arial", 10))

scroll = Scrollbar(root, command=text.yview)

scroll.config(command=text.yview)

text.config(yscrollcommand=scroll.set)

scroll.pack(side=RIGHT, fill=Y)

text.pack()

root.resizable(0, 0)

root.mainloop()
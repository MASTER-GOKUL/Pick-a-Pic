import mysql.connector
import tkinter as tk
from tkinter import *
import PIL
def view(b,c,d,e,f,g,simg):
    win = tk.Tk()
    win.geometry("700x800")
    win.configure(bg="black")
    canvas = Canvas(win, width=1500, height=800)
    canvas.pack(expand=1)
    canvas.configure(bg="black")
    img= PhotoImage(file= simg)
    label1 = Label(i=img)
    label1.i=img
    label1.place(relx=.5, rely=.2,anchor= CENTER)
    label1.pack()
    it=canvas.create_image(60,60,image=img)
    canvas.move(it,300,100)
    nam= tk.Label(win, text =b, font = "50",bg="black",fg="white")
    nam.place(rely=.65,anchor= W)
    gen= tk.Label(win, text =c, font = "50",bg="black",fg="white")
    gen.place(rely=.7,anchor= W)
    dob= tk.Label(win, text =d, font = "50",bg="black",fg="white")
    dob.place(rely=.75,anchor= W)
    pno= tk.Label(win, text =e, font = "50",bg="black",fg="white")
    pno.place(rely=.8,anchor= W)
    add= tk.Label(win, text =f, font = "25",bg="black",fg="white")
    add.place(rely=.85,anchor= W)
    bgt= tk.Label(win, text =g, font = "50",bg="black",fg="white")
    bgt.place(rely=.9,anchor= W)

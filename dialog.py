import recog as t
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import PIL
import os
import cam as c
import cv2
global file1
def dialog():
    def openfile():
        fop=filedialog.askopenfilename()
        if fop:
            filepath=os.path.abspath(fop)
        fpath1=str(filepath)
        file1=fpath1.replace('\\','/')
        win.destroy()
        t.facerecog(file1)
    def des1():
            win.destroy()
            c.cam()
    win=tk.Tk()
    win.geometry("500x500")
    canvas = Canvas(win, width=500, height=500)
    canvas.pack()
    photo = PhotoImage(file="photo/bg2.png")
    canvas.create_image(125, 125, image=photo)
    but1=Button(win,text = "Take photo", font= ('Helvetica 25 bold'),command=des1).place(relx=.5, rely=.3,anchor= CENTER)
    Label(win,text = "(or)", font= ('Helvetica 25 bold')).place(relx=.5, rely=.52,anchor= CENTER)
    but2=Button(win,text="Select file location",command=openfile,font= ('Helvetica 20 bold')).place(relx=.5,rely=.7,anchor=CENTER)
    win.mainloop()

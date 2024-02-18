import mysql.connector
import tkinter as tk
from tkinter import *
import view as v
def dbhandle(sno,var1):
    
        simg = var1
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db"
        )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM test WHERE SNO='%s'"%sno)

        m1 = mycursor.fetchone()
        i=0
        a=[]
        for x in m1:
            a.append(x)
            match i:
                case(1):
                    b="NAME:"+str(x)
                case(2):
                    c="GENDER:"+str(x)
                case(3):
                    d="DATE OF BIRTH:"+str(x)
                case(4):
                    e="PHONE NUMBER:"+str(x)
                case(5):
                    f="ADDRESS:"+str(x)
                case(6):
                    g="BLOOD GROUP TYPE:"+str(x)
            i+=1
        v.view(b,c,d,e,f,g,simg)


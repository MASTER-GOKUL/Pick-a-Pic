import face_recognition
import mysql.connector
import tkinter as tk
from tkinter import *
import PIL
import dbase as dba
def facerecog(pict="C:/Users/Gokul/Desktop/prefinal/dat/source.png"):
        for i in range(1,6):
            var='photo/'+str(i)+'.png'
            known_image = face_recognition.load_image_file(var)
            unknown_image = face_recognition.load_image_file(pict)
            biden_encoding = face_recognition.face_encodings(known_image)[0]
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
            if(results == [True]):
                sno = i
                var1 = var
                dba.dbhandle(sno,var1)
                break

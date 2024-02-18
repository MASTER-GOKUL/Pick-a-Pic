import recog as t
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import PIL
import os
import cv2
def cam():
    
        face=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cap=cv2.VideoCapture(0)
        folder="C:/Users/Gokul/Desktop/prefinal/dat"
        
        def detect(img):
            gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face.detectMultiScale(gimg,1.1,5,minSize=(40,40))
            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
            return faces
        while  True:
            success, img=cap.read()
            cam=img
            if(cv2.waitKey(1) & 0xFF==ord("s")):
                
                cv2.imwrite(f'{folder}/source.png',img)
                print("Image taken")
            if(cv2.waitKey(1) & 0xFF==ord("q")):
               break
            fac=detect(img)
            cv2.imshow("cam",img)
        cap.release()
        cv2.destroyAllWindows()
        t.facerecog()


import sys
import os
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
import tkinter.messagebox
from PIL import Image, ImageTk


root = Tk()
root.title('Smart Educational Institute')
root.iconbitmap('D:\FYP FINAL\seilogo.ico')
root.geometry("700x500")

root.config(bg='yellow')

img = ImageTk.PhotoImage(file="img.jpg")
lab = Label(
    root,
    image=img
)
lab.place(x=0, y=0,)


def collect():
    os.system('"%s"' % '1- Collect-Image.py')

def model():
    os.system('"%s"' % '2- Model Train.py')

def attendance():
    os.system('"%s"' % '3- Recongize - Detection.py')

def save():
    os.system('"%s"' % '4 - Save Attendance.py')

def mongoface():
    os.system('"%s"' % '5- MongoSend.py')

def smartcard():
    os.system('"%s"' % '6- Save RFID Attendance.py')

def msmartcard():
    os.system('"%s"' % '7- MongoSend RFID.py')



status=Label(root,text="FYP F204 -Bahria University Karachi Campus", relief=SUNKEN,font='Courier 15 italic')
status.pack(side=BOTTOM,fill=X)

my_label =Label(root,text=" Welcome to Smart Education Institute" ,relief=GROOVE,font='Times 15 bold')
my_label.pack(pady=10)

my_label2 =Label(root,text="----------------Face Attendance----------------",font='Helvetica 12 bold',) 
my_label2.pack(pady=10)

B1=tkinter.Button(root,text="01 Enter New Student",command= collect)
B1.pack(pady=5)

B2=tkinter.Button(root,text="02 Train Model ",command= model)
B2.pack(pady=5)

B3=tkinter.Button(root,text="03 Face Attendance & Mask Detection",command= attendance)
B3.pack(pady=5)

B3=tkinter.Button(root,text="04 Save Face Attendace File",command= save)
B3.pack(pady=5)

B4=tkinter.Button(root,text="05 Upload Face Attendance File",command= mongoface)
B4.pack(pady=5)

my_label3 =Label(root,text="----------------Smart Card----------------",font='Helvetica 12 bold')
my_label3.pack(pady=10)

B5=tkinter.Button(root,text="01 -Save Smart Card Attendance",command=smartcard)
B5.pack(pady=5)
B5=tkinter.Button(root,text="02 -Upload Smart Card Attendance",command= msmartcard)
B5.pack(pady=5)


root.mainloop()

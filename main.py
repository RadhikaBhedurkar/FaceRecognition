from tkinter import *
from tkinter import ttk
import tkinter.messagebox 
from PIL import Image,ImageTk
from student import Student
from help import Help
import tkinter
from time import strftime
from datetime import datetime
from train import Train
from attendance import Attendance


import os


class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face  Recognition  Attendance  System")
        
        #first img
        img=Image.open(r"C:\Users\admin\OneDrive\Desktop\Radhika Project\images\title.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=130)
        
        #second img
        img1=Image.open(r"C:\Users\admin\OneDrive\Desktop\Radhika Project\images\download.jpeg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=500,y=0,width=500,height=130)
        
        #Third img
        img2=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\i1.jpeg")
        img2=img2.resize((549,180))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1=Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1000,y=0,width=550,height=130)

        #bg img
        img3=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\bg.webp")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lb1=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        def time():
            string=strftime('%H:%M:%S:%p')
            lb1.config(text = string)
            lb1.after(1000,time)

        lb1=Label(title_lb1,font=("times new roman",14,"bold"),bg="white",fg="blue")
        lb1.place(x=0,y=0,width=110,height=50)
        time()

        #user Detail
        img4=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\images.jpeg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.user_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="User Details",command=self.user_details,cursor="hand2",font=("times new roman",20,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect face
        img5=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\img.jpeg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.detect)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.detect,font=("times new roman",20,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attendance face
        img6=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\facereader.png")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",20,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #Help Desk
        img7=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\help.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",command=self.help_data,cursor="hand2",font=("times new roman",20,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
       #train data
        img8=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\train.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        #photos
        img9=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\photos.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",20,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        #Report
        img10=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\report.jpeg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.report_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Report",cursor="hand2",command=self.report_data,font=("times new roman",20,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        #Exit
        img11=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\exit.jpg")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",20,"bold"),bg="dark blue",fg="white")  
        b1_1.place(x=1100,y=580,width=220,height=40)


    def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do You Want to Exit?",parent=self.root)
       if  self.iExit >0:
           self.root.destroy()
       else:
         return
            
    def open_img(self):
        os.startfile("data")

    def report_data(self):
        os.startfile("face.csv")


 #functions buttons
    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window) 

    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
       

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window) 

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def detect(self):
        self.new_window=Toplevel(self.root)
        self.app=(self.new_window) 

    




    
if __name__ =="__main__":
     root=Tk()
     obj=Face_Recognition_system(root)
     root.mainloop()


     

       



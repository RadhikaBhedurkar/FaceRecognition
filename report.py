from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Report:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        title_lb1=Label(self.root,text="USER REPORT",compound=self.font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=0,width=1530,height=45)
     
    

        


        
if __name__ == "__main__":
     root=Tk()
     obj=Report(root)
     root.mainloop()
       

        
from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lb1=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\trainimg.png")
        img_top=img_top.resize((1530,325))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1530,height=325)

        b1_1=Button(self.root,bd=2,relief=RIDGE,text="TRAIN DATA",command=self.train_classifier,font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\faces.jpg")
        img_bottom=img_bottom.resize((1530,325))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb1=Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        pnrs=[]

        for image in path:
            img=Image.open(image).convert('L')  #grey scale img
            imageNp=np.array(img,'uint8')
            pnr=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            pnrs.append(pnr)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        pnrs=np.array(pnrs)


        #train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,pnrs)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")



if __name__ == "__main__":
     root=Tk()
     obj=Train(root)
     root.mainloop()
       
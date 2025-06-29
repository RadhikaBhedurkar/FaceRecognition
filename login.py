from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from student import Student
from help import Help
import tkinter
from time import strftime
from datetime import datetime
from face_recognition import Face_Recognition
from train import Train
from attendance import Attendance
import os

def main():
    win=Tk()
    app=Login_page(win)
    win.mainloop()



class Login_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  
        self.root.title("login")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\admin\OneDrive\Desktop\Radhika Project\images\login.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,width=1920,height=1080)   

        frame=Frame(self.root,bg="black")
        frame.place(x=815,y=140,width=340,height=450)

        img1=Image.open(r"C:\Users\admin\OneDrive\Desktop\Radhika Project\images\icon.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img1)
        img1lb=Label(image=self.photoimg,bg="black",borderwidth=0)
        img1lb.place(x=925,y=140,width=100,height=100)
    
        
        get_str=Label(frame,text="WELCOME",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=90,y=110)

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=160)
        
        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=230)
        
        self.txtpass=Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=260,width=270)


        img2=Image.open(r"C:\Users\admin\OneDrive\Desktop\Radhika Project\images\icon.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        img2lb=Label(image=self.photoimg2,bg="black",borderwidth=0)
        img2lb.place(x=850,y=300,width=25,height=25)

        
        img3=Image.open(r"C:\Users\admin\OneDrive\Desktop\Radhika Project\images\lock.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        img3lb=Label(image=self.photoimg3,bg="black",borderwidth=0)
        img3lb.place(x=850,y=370,width=25,height=25)

        loginbtn=Button(frame,command=self.login,text="LOGIN",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=310,width=120,height=35)
        
        registerbtn=Button(frame,command=self.regs_window,text="New User Register",font=("times new roman",12,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="blue",activebackground="black")
        registerbtn.place(x=20,y=360,width=160)

        forgetbtn=Button(frame,command=self.forget_pass,text="Forget Password",font=("times new roman",12,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="blue",activebackground="black")
        forgetbtn.place(x=10,y=390,width=160)
    
    def regs_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
           messagebox.showerror("Error","All field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome")
        else:
             conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from register where email=%s and pswd=%s",(
                                                                                     self.txtuser.get(),
                                                                                     self.txtpass.get()
                                                                                     
                                                                            ))
             row=my_cursor.fetchone()
             if row==None:
                 messagebox.showerror("Error","Invalid Username & Paswword")
             else:
                 open_main=messagebox.askyesno("YesNo","Access only admin")
                 if open_main>0:
                     self.new_window=Toplevel(self.root)
                     self.app=Face_Recognition_system(self.new_window)
                 else:
                     if not open_main:
                         return 
             conn.commit()
             conn.close()
                         
    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security question")
        elif self.security_entry.get()=="":
            messagebox.showerror("Errpr","Please enter the anewer")
        elif self.new_password_entry.get()=="":
            messagebox.showerror("Error","Please enter new password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.security_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer")
            else:
                query=("update register set pswd=%s where email=%s")
                value=(self.new_password_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset")

   

    def forget_pass(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter email address to reset the password")
        else:
             conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
             my_cursor=conn.cursor()
             query=("select * from register where email=%s")
             value=(self.txtuser.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             #print(row)

             if row==None:
                 messagebox.showerror("My Error","Please enter vaild username")
             else:
                 conn.close()
                 self.root2=Toplevel()
                 self.root2.title("Forget password")
                 self.root2.geometry("340x450+610+170")

                 l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="blue",bg="white")
                 l.place(x=0,y=10,relwidth=1)
            
                 security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                 security_Q.place(x=50,y=80)

                 self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                 self.combo_security_Q["values"]=("Select","Your pet name","Your favourite color")
                 self.combo_security_Q.place(x=50,y=110,width=250)
                 self.combo_security_Q.current(0)

                 security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                 security_A.place(x=50,y=150)

                 self.security_entry=ttk.Entry(self.root2,font=("times new roman",12,"bold"))
                 self.security_entry.place(x=50,y=180,width=250)

                 new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                 new_password.place(x=50,y=220)

                 self.new_password_entry=ttk.Entry(self.root2,font=("times new roman",12,"bold"))
                 self.new_password_entry.place(x=50,y=250,width=250)

                 btn=Button(self.root2,command=self.reset_password,text="Reset",font=("times new roman",15,"bold"),bg="green",fg="white")
                 btn.place(x=100,y=290)

    

        
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_securityQ=StringVar()
        self.var_pswd=StringVar()
        self.var_conf=StringVar()
        self.var_email=StringVar()
        self.var_securityA=StringVar()
        self.var_check=IntVar()

       
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\admin\OneDrive\Desktop\Radhika Project\images\register.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        


        frame=Frame(self.root,bg="white")
        frame.place(x=310,y=110,width=900,height=490)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="red",bg="white")
        register_lbl.place(x=40,y=40)

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",12,"bold"))
        fname_entry.place(x=50,y=130,width=250)


        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",12,"bold"))
        lname_entry.place(x=370,y=130,width=250)
 
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=640,y=100)

        combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        combo_security_Q["values"]=("Select","Your pet name","Your favourite color")
        combo_security_Q.place(x=640,y=130,width=250)
        combo_security_Q.current(0)
        

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=170)

        pswd_entry=ttk.Entry(frame,textvariable=self.var_pswd,font=("times new roman",12,"bold"))
        pswd_entry.place(x=50,y=200,width=250)


        conf=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        conf.place(x=370,y=170)

        conf_entry=ttk.Entry(frame,textvariable=self.var_conf,font=("times new roman",12,"bold"))
        conf_entry.place(x=370,y=200,width=250)

        email=Label(frame,text="Email Id",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=50,y=240)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.place(x=50,y=270,width=250)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        security_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",12,"bold"))
        security_entry.place(x=370,y=270,width=250)

        
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms and Conditions" ,font=("times new roman",15,"bold"), onvalue=1,offvalue=0 ,bg="white")
        checkbtn.place(x=50,y=310)

        b1=Button(frame,text="Register",command=self.register_data,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        b1.place(x=120,y=360,width=160)
        
        b2=Button(frame,text="Login Now",command=self.register_data,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="red")
        b2.place(x=390,y=360,width=160)


 
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required ")
        elif self.var_pswd.get()!=self.var_conf.get():
            messagebox.showerror("Error","Password and Confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
             conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
             my_cursor=conn.cursor()
             query=("select * from register where email=%s")
             value=(self.var_email.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             if row!=None:
                 messagebox.showerror("Error","User already exist,Please try another email")
             else:
                 my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_fname.get(),
                                                                                self.var_lname.get(),
                                                                                self.var_securityQ.get(),
                                                                                self.var_pswd.get(),
                                                                                self.var_email.get(),
                                                                                self.var_securityA.get()
                                                                                 ))
             conn.commit()
             conn.close()
             messagebox.showinfo("Success","Register Successfully")


        


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

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",20,"bold"),bg="dark blue",fg="white")
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
       
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window) 

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

   




        
        
if __name__=="__main__":
  main()
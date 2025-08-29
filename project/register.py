from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_pswd=StringVar()
        self.var_conf=StringVar()
        self.var_email=StringVar()
        self.var_check=IntVar()

       
        self.bg=ImageTk.PhotoImage(file=r"E:/project/Images/register.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        


        frame=Frame(self.root,bg="white")
        frame.place(x=310,y=110,width=700,height=450)

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
        
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms and Conditions" ,font=("times new roman",15,"bold"), onvalue=1,offvalue=0 ,bg="white")
        checkbtn.place(x=50,y=310)

        b1=Button(frame,text="Register",command=self.register_data,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        b1.place(x=270,y=360,width=160)
 
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required ")
        elif self.var_pswd.get()!=self.var_conf.get():
            messagebox.showerror("Error","Password and Confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
             conn=mysql.connector.connect(host="localhost",user="root",password="Chandu$0609",database="mydata")
             my_cursor=conn.cursor()
             query=("select * from register where email=%s")
             value=(self.var_email.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             if row!=None:
                 messagebox.showerror("Error","User already exist,Please try another email")
             else:
                 my_cursor.execute("insert into register values(%s.%s,%s,%s)",(
                                                                                self.var_fname.get(),
                                                                                self.var_lname.get(),
                                                                                self.var_email.get(),
                                                                                self.var_pswd.get()
                                                                              ))
             conn.connect()
             conn.close()
             messagebox.showinfo("Success","Register Successfully")


        



if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()




    
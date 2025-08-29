from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox



class Admin_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("login")

        self.bg=ImageTk.PhotoImage(file=r"G:/project/Images/login.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,width=1430,height=760)

        

        frame=Frame(self.root,bg="black")
        frame.place(x=815,y=140,width=340,height=450)

        img1=Image.open(r"G:/project/Images/icon.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img1)
        img1lb=Label(image=self.photoimg,bg="black",borderwidth=0)
        img1lb.place(x=925,y=140,width=100,height=100)
    

        
        get_str=Label(frame,text="WELCOME",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=90,y=110)

        username=lbl=Label(frame,text="Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=160)
        
        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=230)
        
        self.txtpass=Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=260,width=270)


        img2=Image.open(r"G:/project/Images/icon.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        img2lb=Label(image=self.photoimg2,bg="black",borderwidth=0)
        img2lb.place(x=850,y=300,width=25,height=25)

        
        img3=Image.open(r"G:/project/Images/lock.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        img3lb=Label(image=self.photoimg3,bg="black",borderwidth=0)
        img3lb.place(x=850,y=370,width=25,height=25)

        loginbtn=Button(frame,command=self.admin,text="LOGIN",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=310,width=120,height=35)
        
        

    
    def admin(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
           messagebox.showerror("Error","All field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome")
        else:
            messagebox.showerror("Invalid","Invalid Usename and Password")
            






if __name__=="__main__":
   root=Tk()
   obj=Admin_page(root)
   root.mainloop()
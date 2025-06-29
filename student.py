from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("User Details")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_pnr=StringVar()
        self.var_std_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone_no=StringVar()
        self.var_teacher_id=StringVar()
        self.var_teacher_name=StringVar()
        self.var_teacher_dept=StringVar()

        #first img
        img=Image.open(r"C:\Users\admin\OneDrive\Desktop\Radhika Project\images\s2.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=130)
        
        #second img
        img1=Image.open(r"C:\Users\admin\OneDrive\Desktop\Radhika Project\images\s1.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=500,y=0,width=500,height=130)
        
        #Third img
        img2=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\s3.webp")
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

        title_lb1=Label(bg_img,text="USER  MANAGEMENT  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="User Details",font=("times new roman",13,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\s4.jpg")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=720,height=130)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=125)

        #Department
        dee_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dee_label.grid(row=0,column=0,padx=10,sticky=W)

        dee_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly")
        dee_combo["values"]=("Select Department","BCA","HM","Nursing")
        dee_combo.current(0)
        dee_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly")
        course_combo["values"]=("Select Course","KKSU","SNDT")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","sem1","sem2","sem3","sem4","sem5","sem6")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #User Information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="User Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=260,width=720,height=300)

        #student PNR
        studentPNR_label=Label(class_student_frame,text="Student PNR",font=("times new roman",13,"bold"),bg="white")
        studentPNR_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentPNR_entry=Entry(class_student_frame,textvariable=self.var_pnr,width=20,font=("times new roman",13,"bold"),bg="white")
        studentPNR_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student Name
        studentName_label=Label(class_student_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"),bg="white")
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #student Gender
        studentId_label=Label(class_student_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentName_entry=Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"),bg="white")
        studentName_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        gen_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly")
        gen_combo["values"]=("Select Gender","Male","Female","Other")
        gen_combo.current(0)
        gen_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #student DOB
        studentDiv_label=Label(class_student_frame,text="DOB",font=("times new roman",13,"bold"),bg="white")
        studentDiv_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentDiv_entry=Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"),bg="white")
        studentDiv_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
       
       
        #student Email
        studentName_label=Label(class_student_frame,text="Email",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        studentName_entry=Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"),bg="white")
        studentName_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #student phone no
        studentDOB_label=Label(class_student_frame,text="Phone No",font=("times new roman",13,"bold"),bg="white")
        studentDOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentDOB_entry=Entry(class_student_frame,textvariable=self.var_phone_no,width=20,font=("times new roman",13,"bold"),bg="white")
        studentDOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Teacher ID
        Email_label=Label(class_student_frame,text="Teacher ID",font=("times new roman",13,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entry=Entry(class_student_frame,textvariable=self.var_teacher_id,width=20,font=("times new roman",13,"bold"),bg="white")
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        phoneno_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",13,"bold"),bg="white")
        phoneno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phoneno_entry=Entry(class_student_frame,textvariable=self.var_teacher_name,width=20,font=("times new roman",13,"bold"),bg="white")
        phoneno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Teacher Department
        Address_label=Label(class_student_frame,text="Teacher Department",font=("times new roman",13,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=Entry(class_student_frame,textvariable=self.var_teacher_dept,width=20,font=("times new roman",13,"bold"),bg="white")
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        dept_combo=ttk.Combobox(class_student_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly")
        dept_combo["values"]=("Select Department","BCA","HM","Nursing")
        dept_combo.current(0)
        dept_combo.grid(row=4,column=1,padx=2,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a photo sample",value="yes")
        Radiobutton1.grid(row=5,column=0)
        
        Radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        Radiobutton2.grid(row=5,column=1)


        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=715,height=45)
    
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=715,height=40)

       

        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="User Details",font=("times new roman",13,"bold"))
        right_frame.place(x=750,y=10,width=730,height=580)

        img_right=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\s5.jpg")
        img_right=img_right.resize((720,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lb1=Label(right_frame,image=self.photoimg_right)
        f_lb1.place(x=5,y=0,width=720,height=130)  

        #search system
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        search_frame.place(x=5,y=130,width=710,height=70)

        search_label=Label(search_frame,text="Search By",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly")
        search_combo["values"]=("Select","Student PNR")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        show_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        show_btn.grid(row=0,column=4,padx=4)
         
        #Table frame
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Dep","Course","Year","Sem","PNR","Name","Gender","DOB","Email","Phone No","Teacher ID","Teacher Name","Teacher Department","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("PNR",text="PNR No")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone No",text="Phone No")
        self.student_table.heading("Teacher ID",text="Teacher ID")
        self.student_table.heading("Teacher Name",text="Teacher Name")
        self.student_table.heading("Teacher Department",text="Teacher Department")
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.heading("photo",text="photo")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("PNR",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100) 
        self.student_table.column("Phone No",width=100) 
        self.student_table.column("Teacher ID",width=120)
        self.student_table.column("Teacher Name",width=120)
        self.student_table.column("Teacher Department",width=130)
        self.student_table.column("photo",width=120)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()  

    
    #function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_pnr.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_pnr.get(),
                            self.var_std_name.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone_no.get(),
                            self.var_teacher_id.get(),
                            self.var_teacher_name.get(),
                            self.var_teacher_dept.get(),
                            self.var_radio1.get()


                ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","User details has been added successfully",parent=self.root)
            except Exception as es:
             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #fetch data
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from user")
         data=my_cursor.fetchall()

         if len(data)!=0:
              self.student_table.delete(*self.student_table.get_children())
              for i in data:
                   self.student_table.insert("",END,values=i)
                   conn.commit()
         conn.close()  

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]), 
        self.var_semester.set(data[3]),
        self.var_pnr.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone_no.set(data[9]),
        self.var_teacher_id.set(data[10]),
        self.var_teacher_name.set(data[11]),
        self.var_teacher_dept.set(data[12]),
        self.var_radio1.set(data[13])


    #Update data
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_pnr.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                    Update=messagebox.askyesno("Update","Do you want to update this user data",parent=self.root)
                    if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update user set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Gender=%s,DOB=%s,Email=%s where Student_PNR=%s",(

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_pnr.get()
                    
                ))
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("Success","User details has been updated successfully",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
            except Exception as es:
             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
  

    #Delete data
    def delete_data(self):
        if self.var_dep.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Update","Do you want to delete this user data",parent=self.root)
                if delete>0:
                       conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                       my_cursor=conn.cursor()  
                       sql="delete from user where Student_PNR=%s"
                       val=(self.var_pnr.get(),)
                       my_cursor.execute(sql,val)

                else:
                         if not delete:
                              return
                         
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","User details has been deleted successfully",parent=self.root)
            except Exception as es:
             messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #Reset data
    def reset_data(self):
      self.var_dep.set("Select Department"),
      self.var_course.set("Select Course"),
      self.var_year.set("Select Year"),
      self.var_semester.set("Select Semester"),
      self.var_pnr.set(""),
      self.var_std_name.set(""),
      self.var_gender.set(""),
      self.var_dob.set(""),
      self.var_email.set(""),
      self.var_phone_no.set(""),
      self.var_teacher_id.set(""),
      self.var_teacher_name.set(""),
      self.var_teacher_dept.set(""),
      self.var_radio1.set("")
    
    
   

    
    

if __name__ == "__main__":
     root=Tk()
     obj=Student(root)
     root.mainloop()
       
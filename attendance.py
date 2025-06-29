from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("User Attendance System")

        #variables
        self.var_atten_pnr=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_department=StringVar()
        self.var_atten_status=StringVar()
        

        #first img
        img=Image.open(r"C:\Users\admin\OneDrive\Desktop\Radhika Project\images\s2.jpg")
        img=img.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=800,height=200)
        
        #second img
        img1=Image.open(r"C:\Users\admin\OneDrive\Desktop\Radhika Project\images\s1.jpg")
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=800,y=0,width=800,height=200)

        #bg img
        img3=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\bg.webp")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lb1=Label(bg_img,text="ATTENDANCE MANAGEMENT  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="User Attendance Details",font=("times new roman",13,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\s4.jpg")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #labels and entry
        #PNR
        attendancePNR_label=Label(left_inside_frame,text="Student PNR",font=("times new roman",13,"bold"),bg="white")
        attendancePNR_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendancePNR_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_pnr,font=("times new roman",13,"bold"),bg="white")
        attendancePNR_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Name
        attendanceName_label=Label(left_inside_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        attendanceName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        attendanceName_label=Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"),bg="white")
        attendanceName_label.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Date
        attendanceDate_label=Label(left_inside_frame,text="Date",font=("times new roman",13,"bold"),bg="white")
        attendanceDate_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        attendanceDate_label=Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"),bg="white")
        attendanceDate_label.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        attendanceTime_label=Label(left_inside_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        attendanceTime_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        attendanceTime_label=Entry(left_inside_frame,width=20,textvariable=self.var_atten_department,font=("times new roman",13,"bold"),bg="white")
        attendanceTime_label.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Attendance
        attendance_label=Label(left_inside_frame,text="Attendance Status",font=("times new roman",13,"bold"),bg="white")
        attendance_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        attendance_label=Entry(left_inside_frame,width=20,textvariable=self.var_atten_status,font=("times new roman",13,"bold"),bg="white")
        attendance_label.grid(row=2,column=1,padx=10,pady=5,sticky=W)
     
        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=715,height=40)
    
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=23,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=23,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=23,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",13,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=445)

        #--------------scroll bar table---------------------
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame,columns=("PNR","Name","Date","Department","Attendance","Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("PNR",text="PNR")
        self.AttendaceReportTable.heading("Name",text="Name")
        self.AttendaceReportTable.heading("Date",text="Date")
        self.AttendaceReportTable.heading("Department",text="Department")
        self.AttendaceReportTable.heading("Attendance",text="Attendance")
        
        self.AttendaceReportTable["show"]="headings"
        self.AttendaceReportTable.column("PNR",width=100)
        self.AttendaceReportTable.column("Name",width=100)
        self.AttendaceReportTable.column("Date",width=100)
        self.AttendaceReportTable.column("Department",width=100)
        self.AttendaceReportTable.column("Attendance",width=100)
        self.AttendaceReportTable.pack(fill=BOTH,expand=1)

        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)

        

    #fetch data 
    def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)

    def importCsv(self):
                global mydata
                mydata.clear(
                     
                )
                fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                with open(fin) as myfile:
                    csvread=csv.reader(myfile,delimiter=",")
                    for i in csvread:
                        mydata.append(i)
                    self.fetchData(mydata)

    def exportCsv(self):
        try:
             if len(mydata)<1:
                  messagebox.showerror("No Data","No data found to export",parent=self.root)
                  return False
             fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
             with open(fin,mode="w",newline="")as myfile:
                  exp_write=csv.writer(myfile,delimiter=",")
                  for i in mydata:
                       exp_write.writerow(i)
                  messagebox.showinfo("Data Export","Your data exported to"+ os.path.basename(fin)+ "successfully")

        except Exception as es:
             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
         cursor_row=self.AttendaceReportTable.focus()
         content=self.AttendaceReportTable.item(cursor_row)
         rows=content['values']
         self.var_atten_pnr.set(rows[0])
         self.var_atten_name.set(rows[1])
         self.var_atten_date.set(rows[2])
         self.var_atten_department.set(rows[3])
         self.var_atten_status.set(rows[4])
        
    
    def reset_data(self):
         self.var_atten_pnr.set("")
         self.var_atten_name.set("")
         self.var_atten_date.set("")
         self.var_atten_department.set("")
         self.var_atten_status.set("")



if __name__ == "__main__":
     root=Tk()
     obj=Attendance(root)
     root.mainloop()

       
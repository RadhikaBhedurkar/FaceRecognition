from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")

        img=Image.open(r"\Users\admin\OneDrive\Desktop\Radhika Project\images\banner.jpg")
        img=img.resize((1530,790))
        self.photoimg=ImageTk.PhotoImage(img)
       
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=130)

        bg1=Image.open(r"\Users\admin\OneDrive\Desktop\Radhika Project\images\bg4.png")
        bg1=bg1.resize((1530,790))
        self.photobg1=ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1530,height=790)

        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        std_img_btn=Image.open(r"\Users\admin\OneDrive\Desktop\Radhika Project\images\web.png")
        std_img_btn=std_img_btn.resize((180,180))
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.website,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.website,text="Website",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=250,y=380,width=180,height=45)

        det_img_btn=Image.open(r"\Users\admin\OneDrive\Desktop\Radhika Project\images\fb.png")
        det_img_btn=det_img_btn.resize((180,180))
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=480,y=380,width=180,height=45)

        att_img_btn=Image.open(r"\Users\admin\OneDrive\Desktop\Radhika Project\images\yt.png")
        att_img_btn=att_img_btn.resize((180,180))
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=720,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=720,y=380,width=180,height=45)

        hlp_img_btn=Image.open(r"\Users\admin\OneDrive\Desktop\Radhika Project\images\gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180))
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=940,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=940,y=380,width=180,height=45)
    
    
    def website(self):
        self.new = 1
        self.url = "https://exceleprep.com/"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/channel/UCwpFCX_Z4SVkAT_6hPeUnsA"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()

        
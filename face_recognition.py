from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import mysql.connector
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lb1 = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        # 1st image
        img_top = Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\scan.jpeg")
        img_top = img_top.resize((650, 730))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=55, width=650, height=730)

        # 2nd image
        img_bottom = Image.open(r"c:\Users\admin\OneDrive\Desktop\Radhika Project\images\detect.jpg")
        img_bottom = img_bottom.resize((950, 730))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lb2 = Label(self.root, image=self.photoimg_bottom)
        f_lb2.place(x=650, y=55, width=950, height=730)

        # Button
        b1 = Button(f_lb2, text="Face Recognition", command=self.face_recog, cursor="hand2",font=("times new roman", 18, "bold"), bg="green", fg="white")
        b1.place(x=365, y=590, width=200, height=40)

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbours)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_PNR=%s", (id,))
                result_name = my_cursor.fetchone()
                name = result_name[0] if result_name else "Unknown"

                my_cursor.execute("SELECT Dep FROM student WHERE Student_PNR=%s", (id,))
                result_dep = my_cursor.fetchone()
                dep = result_dep[0] if result_dep else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"PNR: {id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {name}", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Dep: {dep}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
        except AttributeError:
            messagebox.showerror("OpenCV Error", "cv2.face is not available. Please install opencv-contrib-python.")
            return

        if not os.path.exists("classifier.xml"):
           messagebox.showerror("Missing Model", "classifier.xml not found in the project directory.")
        return

        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13: 
                break

            video_cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

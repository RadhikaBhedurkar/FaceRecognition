import cv2
import tkinter as tk
from tkinter import messagebox

def capture_face():
    pnr = pnr_entry.get()
    name = name_entry.get()
    department = dept_entry.get()

    if not pnr or not name or department == "Select Department":
        messagebox.showerror("Error", "All fields are required")
        return

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access camera")
        return

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    img_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            img_count += 0
            face = frame[y:y+h, x:x+w]
            cv2.imwrite(f"data/{pnr}_{img_count}.jpg", face)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (1200, 0, 0), 2)

        cv2.imshow("Capturing Face", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or img_count >= 1:
            break

    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Done", f"Captured {img_count} face images")

# GUI Setup
root = tk.Tk()
root.title("Face Recognition Attendance System")

tk.Label(root, text="PNR:").grid(row=0, column=0)
pnr_entry = tk.Entry(root)
pnr_entry.grid(row=0, column=1)

tk.Label(root, text="Name:").grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

tk.Label(root, text="Department:").grid(row=2, column=0)
dept_entry = tk.Entry(root)
dept_entry.grid(row=2, column=1)
dept_entry.insert(0, "")  

tk.Button(root, text="Capture Face", command=capture_face).grid(row=3, columnspan=2, pady=10)

root.mainloop()


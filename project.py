from tkinter import *
from PIL import ImageTk,Image,ImageSequence
import pyglet
import mysql.connector
from tkinter  import messagebox
from attendence import Attendance
from student import Student
from databaseTest import *
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1537x768+0+0")
        self.root.title("Face_Recogonition_System")
        self.root.state("zoomed")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"images\dsa.jpg")
        img=img.resize((1537,130))
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1537,height=130)

        # backgorund image 
        bg1=Image.open(r"images\pexels-johannes-plenio-1103970.jpg")
        bg1=bg1.resize((1537,768))
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1537,height=768)


        #title section
        title_lb1 = Label(bg_img,text="FACE RECOGNITION ATTENDENCE MANAGEMENT SYSTEM",font=("verdana",32,"bold","underline"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1537,height=60)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"images\pics1s\student pannel.png")
        std_img_btn=std_img_btn.resize((180,180))
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Panel",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=250,y=280,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"images\b2-22-e1582998451498.jpg")
        det_img_btn=det_img_btn.resize((180,180))
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=600,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=600,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"images\pics1s\Attendance.png")
        att_img_btn=att_img_btn.resize((180,180))
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=960,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=960,y=280,width=180,height=45)

        # Top 3 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 4
        tra_img_btn=Image.open(r"images\pics1s\Data train.jpg")
        tra_img_btn=tra_img_btn.resize((180,180))
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=250,y=370,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Data Train",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=250,y=550,width=180,height=45)

        # Photo   button 5
        pho_img_btn=Image.open(r"images\data-center-icon_48369-2491.jpg")
        pho_img_btn=pho_img_btn.resize((180,180))
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=600,y=370,width=180,height=180)

        pho_b1_1 = Button(bg_img,command=self.open_img,text="DataSet",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=600,y=550,width=180,height=45)

       

        # exit   button 6
        exi_img_btn=Image.open(r"images\pics1s\exit.png")
        exi_img_btn=exi_img_btn.resize((180,180))
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=960,y=370,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=960,y=550,width=180,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def Close(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop() 

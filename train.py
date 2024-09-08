from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1166x718")
        self.root.title("Train Pannel")
        self.root.state("zoomed")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"images\student.jpg")
        img=img.resize((1537,150))
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1537,height=150)

        # backgorund image 
        bg1=Image.open(r"images\pexels-johannes-plenio-1103970.jpg")
        bg1=bg1.resize((1537,768))
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1537,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome  to  Training  Panel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1537,height=50)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"images\RDS_Top_Image.png")
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Label(bg_img,image=self.std_img1)
        std_b1.place(x=100,y=80)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",25,"bold"),bg="gold",fg="navyblue")
        std_b1_1.place(x=100,y=517,width=1365,height=60)

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop() 

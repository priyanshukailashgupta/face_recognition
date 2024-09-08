from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
from tkinter  import messagebox


def Register():
    window = Toplevel()
    window.geometry('1166x718')
    window.title('REGISTER')
    window.state('zoomed')
    window.resizable(0,0)


        #--------------------bg ----------------------

    bg_frame = Image.open(r"C:\Users\priya\Desktop\face_recognition\reg.jpeg")
    bg_frame = bg_frame.resize((1550,900))
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill= 'both' , expand='yes')


        #------------------------reg frame-------------------------
    reg_frame = Frame(window , width= 980 , height=430 , bg='#040405')
    reg_frame.place(x=200,y=400)

    img= Image.open(r"C:\Users\priya\Desktop\face_recognition\frame.jpeg")
    img= img.resize((450,430))
    photo = ImageTk.PhotoImage(img)
    img_label = Label(reg_frame , image = photo , bg='#040405')
    img_label.image = photo
    img_label.place(x=0, y=0)

    heading = Label(reg_frame, text = 'SIGN UP' , font=('yu gothic ui' , 25 , 'bold') , fg = '#FFCC00' , bg='#040405')
    heading.place(x=670, y=8)

    l1=Label(reg_frame,text="First Name",font=('yu gothic ui' , 16 , 'bold'),foreground="#B19CD9",width=20 , bg='#040405')
    l1.place(x=460,y=70)
    f1=Entry(reg_frame,font="bold")
    f1.place(x=700,y=75)

    l2=Label(reg_frame,text="Last Name",font=('yu gothic ui' , 16 , 'bold'),foreground="#B19CD9",width=20,bg='#040405')
    l2.place(x=460,y= 110)
    f2=Entry(reg_frame,font="bold")
    f2.place(x=700,y=115)

    l3=Label(reg_frame,text="Contact",font=('yu gothic ui' , 16 , 'bold'),foreground="#B19CD9",width=18,bg='#040405')
    l3.place(x=459,y=150)
    f3=Entry(reg_frame,font="bold")
    f3.place(x=700,y=155)

    l4=Label(reg_frame,text="E-Mail",font=('yu gothic ui' , 16 , 'bold'),foreground="#B19CD9",width=17,bg='#040405')
    l4.place(x=458,y=190)
    f4=Entry(reg_frame,font="bold")
    f4.place(x=700,y=195)

    l5=Label(reg_frame,text="Password",font=('yu gothic ui' , 16 , 'bold'),foreground="#B19CD9",width=20,bg='#040405')
    l5.place(x=456,y=230)
    f5=Entry(reg_frame,font="bold")
    f5.place(x=700,y=235)

    l6=Label(reg_frame,text="Confirm",font=('yu gothic ui' , 16 , 'bold'),foreground="#B19CD9",width=18,bg='#040405')
    l6.place(x=460,y=270)
    f6=Entry(reg_frame,font="bold")
    f6.place(x=700,y=275)
    
    check=IntVar()
    checkbtn=Checkbutton(reg_frame,variable=check,text="I agree the Terms & Conditions .",font=('times new roman' , 15 ),foreground='grey', activebackground='#040405',width=36,bg='#040405',onvalue=1,offvalue=0)
    checkbtn.place(x=460,y=320)
    
    def save():            
             if f1.get() =="" or f2.get() =="" or f3.get()=="" or f4.get()=="":
                 messagebox.showerror("Error","All Field Required !!!")
             elif f5.get()!=f6.get():
                 messagebox.showerror("Error","Both must be same")
             elif check.get()==0:
                 messagebox.showerror("Error","Please agree our Terms & Condition")
             else:                   
                try:
                    con=mysql.connector.connect(user='root', password='root',host='localhost',database='face_recognition',port=3306)
                    my=con.cursor()
                    my.execute("insert into register values('"+f1.get()+"', '"+f2.get()+"', '"+f3.get()+"', '"+f4.get()+"', '"+f5.get()+"', '"+f6.get()+"')")
                    print("DATA SAVE")
                    con.commit()
                    messagebox.showinfo("my message Box","SAVE!!!")
                except Exception as e:
                    messagebox.showinfo("my message Box","Record Not Save!!!")
                    print(e)
             window.destroy()
              
    b1=Button(reg_frame,text="Register Now",font=('yu gothic ui' , 16 , 'bold'),background="#B19CD9", bd =2 , foreground="white" , command = save )
    b1.place(x=640,y=370,width=200)


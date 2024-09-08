from tkinter import *
from PIL import ImageTk,Image
from register import Register
import mysql.connector
from tkinter  import messagebox
from project import Face_Recognition_System


def next():
     Register()
     
     
class loginpage:
     def __init__(self, window):
        self.window = window

        window.geometry('1166x718')
        window.title('Login')
        window.state('zoomed')
        window.resizable(0,0)

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
     
        #------------------------background image-------------------------
        bg_frame = Image.open("present.jpg")
        photo = ImageTk.PhotoImage(bg_frame)
        bg_panel = Label(window, image=photo)
        bg_panel.image = photo
        bg_panel.pack(fill= 'both' , expand='yes')
                                   
        #------------------------login frame-------------------------
        lgn_frame = Frame(window , bg= '#040405' ,  width= 450 , height=650)
        lgn_frame.place(x=900,y=65)

        heading = Label(lgn_frame, text = 'WELCOME' , font=('yu gothic ui' , 25 , 'bold') , bg= '#040405'  , fg = 'white')
        heading.place(x=80, y=30 , width= 300 , height= 30)

        #----------------signin image-------------------------
        sign_in_image= Image.open(r"login.jpg")
        sign_in_image= sign_in_image.resize((100,100))
        photo = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(lgn_frame , image = photo , bg='#040405')
        sign_in_image_label.image = photo
        sign_in_image_label.place(x=180, y=100)

        sign_in_label = Label(lgn_frame, text= 'Sign In' , bg='#040405' , fg='white' , font=('yu gothic ui' , 17 , 'bold'))
        sign_in_label.place(x=195 , y=210)

        #---------------username--------------------------

        username_label = Label(lgn_frame, text='E-Mail' , font= ('yu gothic ui' , 13 , 'bold') , bg='#040405' , fg='#4f4e4d')
        username_label.place(x=70, y=300)

        username_entry = Entry(lgn_frame, highlightthickness=0 , relief= FLAT , bg='#040405' , fg='#6b6a69' , font=('yo gothic ui' , 12,'bold'))
        username_entry.place(x=110 , y=335 , width = 270)
                
        username_line = Canvas(lgn_frame , width = 300 , height = 2.0 , bg='#bdb9b1' ,  highlightthickness=0 ) 
        username_line.place(x=70, y=359)

        #--------------------username icon---------------------

        username_icon= Image.open(r"images\username_icon.png")
        photo = ImageTk.PhotoImage(username_icon)
        username_icon_label = Label(lgn_frame , image = photo , bg='#040405')
        username_icon_label.image = photo
        username_icon_label.place(x=70, y=330)
        #----------------------------password---------------

        password_label = Label(lgn_frame, text='Password' , font= ('yu gothic ui' , 13 , 'bold') , bg='#040405' , fg='#4f4e4d')
        password_label.place(x=70, y=380)

        password_entry = Entry(lgn_frame, highlightthickness=0 , relief= FLAT , bg='#040405' , fg='#6b6a69' , font=('yo gothic ui' , 12,'bold'))
        password_entry.place(x=110 , y=415 , width = 270)
                
        password_line = Canvas(lgn_frame , width = 300 , height = 2.0 , bg='#bdb9b1' ,  highlightthickness=0 ) 
        password_line.place(x=70, y=439)      
                
        #--------------------password icon---------------------

        password_icon= Image.open(r"images\password_icon.png")
        photo = ImageTk.PhotoImage(password_icon)
        password_icon_label = Label(lgn_frame , image = photo , bg='#040405')
        password_icon_label.image = photo
        password_icon_label.place(x=70, y=410)


        def submit():
               if username_entry.get() =="" or password_entry.get() =="" :
                   messagebox.showerror("Error","All Field Required !!!")
               else: 
                   con=mysql.connector.connect(user='root', password='root',host='localhost',database='face_recognition',port=3306)
                   my=con.cursor()
                   
                   my.execute("select * from register where email='"+username_entry.get()+"' and password='"+password_entry.get()+"'")
                   res=my.fetchall()
                   f=0
                   for x in res:
                      name=x[0]
                      print("name=",name)
                      f=f+1
                      
                   con.commit()
                   if f==0:
                        messagebox.showinfo("Login Messagebox","Invalid Username and Password!!")
                   else:
                        messagebox.showinfo("Login Message","Welcome:" + str(name))
                        app=Face_Recognition_System(window)
                        
        #---------------------login button----------------------

        lgn_button= Image.open(r"images\btn1.png")
        photo = ImageTk.PhotoImage(lgn_button)
        lgn_button_label = Label(lgn_frame , image = photo , bg='#040405', bd=0 )
        lgn_button_label.image = photo
        lgn_button_label.place(x=70, y=450)

        login = Button(lgn_button_label ,text='LOGIN' , font= ('yu gothic ui' , 13 , 'bold') , bg='#3047ff' , fg='white' , activebackground='#3047ff' , cursor='hand2' , width=25 , bd=0 , command= submit) 
        login.place(x=20, y=10)



        #-------------------------forgot password--------------

        forgot_btn = Button(lgn_frame ,text='Forgot Password ?' , font= ('yu gothic ui' , 13 , 'bold underline') , bg='#040405' , fg='white' , activebackground='#040405'  , width=25 , bd=0) 
        forgot_btn.place(x=95, y=510)


        #-------------------signup-------------------------

        signup_label = Label(lgn_frame, text='No account yet ?' , font= ('yu gothic ui' , 9 , 'bold') , bg='#040405' , fg='white')
        signup_label.place(x=70, y=560)

        signup_btn = Image.open(r"images\register.png")
        photo = ImageTk.PhotoImage(signup_btn)
        signup_btn_label = Button(lgn_frame , image = photo , bg='#040405' , cursor='hand2' , activebackground='#040405' , bd=0 , command=next)
        signup_btn_label.image = photo
        signup_btn_label.place(x=170, y=550)

        #============show hide password-------------------
        

        def show():
             hide_button = Button(lgn_frame , image=photo , bg='white', activebackground='white' , cursor='hand2' , bd=0 , command = hide)  
             hide_button.image = photo
             hide_button.place(x=370, y=415)
             password_entry.config(show='')

        def hide():
             show_button = Button(lgn_frame , image=photo1 , bg='white', activebackground='white' , cursor='hand2' , bd=0 , command = show)  
             show_button.image = photo1
             show_button.place(x=370, y=415)
             password_entry.config(show='*')


        show_image= Image.open(r"images\show.png")
        photo1 = ImageTk.PhotoImage(show_image)
        show_button = Button(lgn_frame , image=photo1 , bg='white', activebackground='white' , cursor='hand2' , bd=0 , command= show)  
        show_button.image = photo1
        show_button.place(x=370, y=415)

        hide_image= Image.open(r"images\hide.png")
        photo = ImageTk.PhotoImage(hide_image)





       #----------------------slider frame-------------------------------

        slider_frame1 = Frame(window , bg= 'gold' ,  width= 775, height=620) 
        slider_frame1.place(x=48,y=80)
        

        slider_frame = Frame(window , bg= '#040405' ,  width= 750 , height=550)
        slider_frame.place(x=60,y=140)

        img1 = ImageTk.PhotoImage(file=r"l1.jpg")
        img2 = ImageTk.PhotoImage(file=r"l2.jpg")
        img3 = ImageTk.PhotoImage(file=r"l3.jpg")

        slider_label = Label(slider_frame ,  bd=0)
        slider_label.place(x=0,y=0)

        slider_label1 = Label(slider_frame1 , text='FACE RECOGNITION ATTENDENCE MANAGEMENT SYSTEM',font= ('verdana' , 16, 'bold',),bg= 'gold' )
        slider_label1.place(x=0,y=10 , width=775 ,height=50) 
        
        
        def slider_func():
             
           global x
           if x==4:
                x=1
           if x==1:
                slider_label.config(image=img1)
           elif x==2:
                slider_label.config(image=img2)
           elif x==3:
                slider_label.config(image=img3)

           x=x+1

           slider_frame1.after(2000,slider_func)

        slider_func()


x=1               

        
def page():
    window = Tk()
    loginpage(window)
    window.mainloop()


if __name__== '__main__':
    page()

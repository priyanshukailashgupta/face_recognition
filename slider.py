
from tkinter import *
from tkinter .ttk import Progressbar
import sys
import loginwindow

root=Tk()
root.resizable(0,0)

height = 430
width = 530
x= (root.winfo_screenwidth()//2)-(width//2)
y= (root.winfo_screenheight()//2)-(height//2)

root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
root.wm_attributes('-topmost', True)

root.overrideredirect(1)
root.config(background='#b800c4')

exit_btn = Button(root, text='X' , command=lambda: exit_window(), font=("yu gothic ui",13, 'bold'), fg='yellow', bg='#b800c4', bd=0 , activebackground='#b800c4')
exit_btn.place(x=495,y=15)

welcome_label = Label(root, text='FACE RECOGNITION ATTENDENCE MANAGEMENT SYSTEM' , font=("yu gothic ui", 13, 'bold'), bg='#b800c4')
welcome_label.place(x=20, y=19)

image = PhotoImage(file='attend.png')
bg_label = Label(root, image = image , bg='#b800c4')
bg_label.place(x=100, y=65)

progress_label = Label(root, text = "Please Wait..." , font=("yu gothic ui" , 13 , 'bold') , bg='#b800c4')
progress_label.place(x=190 , y=330)

progress = Progressbar(root, orient= HORIZONTAL , length= 500 , mode ='determinate')
progress.place(x=15, y=370)

def exit_window():
    sys.exit(root.destroy())

def top():
    win = Toplevel()
    loginwindow.loginpage(win)
    root.withdraw()
    win.deiconify()

    

i=0

def load():
    global i
    if i<=5:
        txt = 'Please Wait...' +  (str(20*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(700, load)
        progress['value'] = 20*i
        i+= 1
    else:
        top()
        
        
load()
root.mainloop()

                  

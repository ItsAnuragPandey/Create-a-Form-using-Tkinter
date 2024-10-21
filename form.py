from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

root = Tk()
root.title('Login Form')
root.geometry("925x500+300+200")
root.config(bg="lightblue")
root.resizable(True,True)

def signup():
    Username = user.get()
    Password = code.get()
    if Username == "admin" and Password == "1234" :
        screen = Toplevel(root)
        screen.title('App')
        screen.geometry("700x800")
        screen.config(bg="white")
        Label(screen , text='HI, WELCOME TO MY SITE',fg= 'black', bg='white',font=('Times',50,'bold')).pack(expand=True)
        screen.mainloop()
    elif Username!='admin' and Password != '1234':
        messagebox.showerror('Invalid', 'Invalid username and Password')
    elif Password!= '1234':
        messagebox.showerror('Invalid', 'Invalid Password')

    elif Username!= 'admin':
        messagebox.showerror('Invalid', 'Invalid Username')

img= PhotoImage(file='login.png')
ttk.Label(root, image=img).place(x=50,y=50)


frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480,y=70)

heading = Label(frame , text = 'Login' , fg = 'black' , bg = 'white' , font=('Times', '24','bold italic') )
heading.place(x= 130,y = 5 )

#now for the box
def on_entry(e):
    user.delete(0, 'end')

def on_leave(e):
    name= user.get()
    if name=='':
        user.insert(0,"Username")

user = Entry(frame, width= 20, border=0,  fg = 'black' , bg = 'white' , font=('Times', '19','bold '))
user.place(x=30 ,y= 80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_entry)
user.bind('<FocusOut>', on_leave)

Frame(frame, width= 295 , height=2 , bg= 'black').place(x=25 , y=107)

#box for password
def on_entry(e):
    code.delete(0, 'end')

def on_leave(e):
    name= code.get()
    if name=='':
        code.insert(0,"Password")

code = Entry(frame, width= 25, border=0,  fg = 'black' , bg = 'white' , font=('Times', '19','bold '))
code.place(x=30 ,y= 150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_entry)
code.bind('<FocusOut>', on_leave)

Frame(frame, width= 295 , height=2 , bg= 'black').place(x=25 , y=177)

Button(frame, width= 40 , pady= 7 , text = "Sign in ", bg = 'light blue', fg ='black', command= signup).place(x=35 , y=204 )
Label(frame, text = "Don't have an account?", bg='white',font= ('Times', 9, 'italic')).place(x=120, y=250)

Button(frame, text='Sign up', fg='blue' ,bg= 'white', cursor='hand2', border=0,font= ('Times', 9, 'italic')).place(x=240, y=250)

root.mainloop()
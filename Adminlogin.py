from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import connection
import main


class login:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title('Login')
        self.p1 = Panedwindow(self.root)

        Label(self.root, text='Login', font=('arial', 30, 'bold', 'underline')).pack()

        Label(self.p1, text='Enter Email').grid(row=0,column=0,padx=10,pady=10)
        self.txt1 = Entry(self.p1, width=50)
        self.txt1.grid(row=0, column=1,pady=10)
        Label(self.p1, text='Enter Password').grid(row=1,column=0,padx=10)
        self.txt2 = Entry(self.p1, width=50, show='*')
        self.txt2.grid(row=1, column=1)
        self.p1.pack(pady=10)
        Button(self.root, text='Login', command=self.checkLogin).pack()
        self.root.mainloop()


    def checkLogin(self):
        self.email = self.txt1.get()
        self.password = self.txt2.get()
        conn = connection.Connect()
        cr = conn.cursor()
        q = 'select * from admin where email="{}" and password="{}"'.format(self.email,self.password)
        cr.execute(q)
        result = cr.fetchone()
        if result == None:
            showerror('','Invalid Email/Password')
        else:
            showinfo('','Login Successfull')
            self.root.destroy()
            main.main(email=self.email)

login()

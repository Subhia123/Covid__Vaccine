from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import connection

class changePass:
    def __init__(self,email):
        self.root = Tk()
        self.root.title('Change Password')
        self.root.geometry('500x500')
        self.f1 = Panedwindow(self.root)

        Label(self.root, text='Change Password', font=('arial',28,'bold','underline')).pack(pady=10)

        Label(self.f1, text='Email : ').grid(row=0, column=0,padx=5,pady=10)
        self.txt1 = Entry(self.f1, width=50)
        self.txt1.grid(row=0, column=1,pady=10)
        self.txt1.insert(0, email)
        self.txt1.config(state='readonly')

        Label(self.f1, text='Old Password : ').grid(row=1, column=0,padx=5,pady=10)
        self.txt2 = Entry(self.f1, width=50)
        self.txt2.grid(row=1, column=1, pady=10)

        Label(self.f1, text='New Password : ').grid(row=2, column=0,padx=5,pady=10)
        self.txt3 = Entry(self.f1, width=50)
        self.txt3.grid(row=2, column=1, pady=10)

        self.f1.pack()
        Button(self.root, text='Submit', command=self.changehospitalPass).pack()
        self.root.mainloop()

    def changehospitalPass(self):
        self.email = self.txt1.get()
        self.oldPass = self.txt2.get()
        self.newPass = self.txt3.get()
        conn = connection.Connect()
        cr = conn.cursor()
        q = 'select * from hospitalcamp where email="{}" and password="{}"'.format(self.email, self.oldPass)
        cr.execute(q)
        result = cr.fetchone()
        if result == None:
            showerror('','Incorrect Old Password')
        else:
            q = 'update hospitalcamp set password="{}" where email="{}"'.format(self.newPass, self.email)
            cr.execute(q)
            conn.commit()
            showinfo('','Password Changed Successfully')

#changePass(email='hospital@gmail.com')

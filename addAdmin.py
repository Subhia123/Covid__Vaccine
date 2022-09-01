from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import connection


class main:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title('Add Admin')
        self.p1 = Panedwindow(self.root)

        Label(self.root, text='Add Admin', font=('arial', 30, 'bold', 'underline')).pack()

        Label(self.p1, text='Enter Email').grid(row=0,column=0,padx=10,pady=10)
        self.txt1 = Entry(self.p1, width=50)
        self.txt1.grid(row=0, column=1,pady=10)
        Label(self.p1, text='Enter Password').grid(row=1,column=0,padx=10,pady=10)
        self.txt2 = Entry(self.p1, width=50)
        self.txt2.grid(row=1, column=1,pady=10)


        Label(self.p1, text='Select Role').grid(row=2, column=0,padx=10,pady=10)
        self.txt3 = Combobox(self.p1, value=('Super Admin','Admin'), width=47, state='readonly')
        self.txt3.grid(row=2, column=1, pady=10)
        self.p1.pack(pady=10)
        Button(self.root, text='Submit', command=self.addAdmin).pack()
        self.root.mainloop()


    def addAdmin(self):
        self.email = self.txt1.get()
        self.password = self.txt2.get()
        self.role = self.txt3.get()
        conn = connection.Connect()
        cr = conn.cursor()
        if self.email == '' and self.password == '' and self.role == '':
            showerror('','Please Enter all values')
        else:
            q = 'select * from admin where email="{}"'.format(self.email)
            cr.execute(q)
            result = cr.fetchone()
            if result == None:
                q = 'insert into admin values ("{}","{}","{}")'.format(self.email,self.password,self.role)
                cr.execute(q)
                conn.commit()
                showinfo('','Admin added successfully')
                self.txt1.delete(0,'end')
                self.txt2.delete(0,'end')
                self.txt3.set('')
            else:
                showerror('','Email already exists')



#main()

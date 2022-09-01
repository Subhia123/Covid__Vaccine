from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import connection
class main:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title('Add Hospital/Camp')
        self.p1 = Panedwindow(self.root)

        Label(self.root, text='Add Hospital/Camp', font=('arial', 30, 'bold', 'underline')).pack()
        Label(self.p1, text='Enter Hospital Name').grid(row=1,column=0,padx=10,pady=10)
        self.txt1=Entry(self.p1,width=50)
        self.p1.pack(pady=10)
        self.txt1.grid(row=1, column=1,pady=10)
        Label(self.p1, text='Enter Email').grid(row=2, column=0,padx=10,pady=10)
        self.txt2 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt2.grid(row=2, column=1, pady=10)
        Label(self.p1, text='Enter Mobile').grid(row=3, column=0, padx=10, pady=10)
        self.txt3 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt3.grid(row=3, column=1, pady=10)
        Label(self.p1, text='Enter Type').grid(row=4, column=0, padx=10, pady=10)
        self.txt4 = Combobox(self.p1,value=('Hospital/Permanent','Camp/Temporary'),width=50,state='readonly')
        self.p1.pack(pady=10)
        self.txt4.grid(row=4, column=1, pady=10)
        Label(self.p1, text='Enter Password').grid(row=5, column=0, padx=10, pady=10)
        self.txt5 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt5.grid(row=5, column=1, pady=10)
        Button(self.root, text='Submit', command=self.addHospital).pack()
        self.root.mainloop()


    def addHospital(self):
        self.Name = self.txt1.get()
        self.Email = self.txt2.get()
        self.Mobile = self.txt3.get()
        self.Type = self.txt4.get()
        self.Password = self.txt5.get()

        conn = connection.Connect()
        cr = conn.cursor()
        if self.Name == '' and self.Email == '' and self.Mobile== '' and self.Type== '' and self.Password== '':
            showerror('','Please Enter all values')
        else:
            q = 'insert into hospitalcamp values ("{}","{}","{}","{}","{}")'.format(self.Name, self.Email, self.Mobile, self.Type, self.Password)
            cr.execute(q)
            conn.commit()
            showinfo('', 'Information added successfully')

main()

from tkinter import*
from tkinter.ttk import *
from tkinter.messagebox import *
import connection

class main:

    def __init__(self):

        self.root = Tk()
        self.root.title('View Vaccination')
        self.root.state('zoomed')
        Label(self.root, text='View Vaccination', font=('arial', 32, 'bold', 'underline')).pack(ipady=20)

        col = ('id', 'name','age','gender','email','mobile','date','dose','hospitalName','vaccineID')
        self.obj = Treeview(self.root, column=col)
        for i in col:
            self.obj.heading(i, text=i.capitalize())
        self.obj['show'] = 'headings'
        self.obj.bind('<Double-1>', self.updatevaccine)
        self.obj.pack()
        self.getValues()
        self.root.mainloop()

    def getValues(self):
        conn = connection.Connect()
        cr = conn.cursor()
        q = 'select id, name,age, gender, email, mobile, date, dose,hospitalName,vaccineID from vaccination'
        cr.execute(q)
        result = cr.fetchall()
        print(result)
        count = 0
        for i in self.obj.get_children():
            self.obj.delete(i)
        for i in result:
            self.obj.insert('',index=count,value=i)
            count += 1
    def updatevaccine(self,event):
        self.items = self.obj.item(self.obj.focus())['values']
        self.root1 = Toplevel()
        self.root1.title('Update Vaccination')
        self.root1.geometry('500x500')

        Label(self.root1, text='Update vaccination', font=('arial',30,'bold','underline')).pack(pady=20)

        Label(self.root1, text='id :').pack(pady=10)
        self.txt1 = Entry(self.root1, width=50)
        self.txt1.pack()
        self.txt1.insert(0,self.items[0])
        self.txt1.config(state='readonly')

        Label(self.root1, text='Name').pack(pady=10)
        self.txt2 = Entry(self.root1, width=50)
        self.txt2.pack()
        self.txt2.insert(1, self.items[0])

        Label(self.root1, text='age :').pack(pady=10)
        self.txt3 = Entry(self.root1, width=50)
        self.txt3.pack()
        self.txt3.insert(2, self.items[0])

        Label(self.root1, text='gender :').pack(pady=10)
        self.txt4 = Entry(self.root1, width=50)
        self.txt4.pack()
        self.txt4.insert(3, self.items[0])

        Label(self.root1, text='email :').pack(pady=10)
        self.txt5 = Entry(self.root1, width=50)
        self.txt5.pack()
        self.txt5.insert(4, self.items[0])

        Label(self.root1, text='mobile :').pack(pady=10)
        self.txt6 = Entry(self.root1, width=50)
        self.txt6.pack()
        self.txt6.insert(5, self.items[0])

        Label(self.root1, text='date :').pack(pady=10)
        self.txt7 = Entry(self.root1, width=50)
        self.txt7.pack()
        self.txt7.insert(6, self.items[0])

        Label(self.root1, text='dose :').pack(pady=10)
        self.txt8 = Entry(self.root1, width=50)
        self.txt8.pack()
        self.txt8.insert(7, self.items[0])

        Label(self.root1, text='hospitalName :').pack(pady=10)
        self.txt9 = Entry(self.root1, width=50)
        self.txt9.pack()
        self.txt9.insert(8, self.items[0])
        Label(self.root1, text='vaccineID :').pack(pady=10)
        self.txt10 = Entry(self.root1, width=50)
        self.txt10.pack()
        self.txt10.insert(9, self.items[0])

        #Button(self.root1, text='Update',command=self.editAdmin).pack(pady=5)
        #Button(self.root1, text='Delete', command=self.deletevaccine).pack(pady=5)
        self.root1.mainloop()

    '''def editAdmin(self):
        self.email = self.txt1.get()
        self.role = self.txt2.get()
        q = 'update admin set role="{}" where email="{}"'.format(self.role, self.email)
        conn = connections.Connect()
        cr = conn.cursor()
        cr.execute(q)
        conn.commit()
        showinfo('','Admin Updated Successfully')
        self.getValues()
        self.root1.destroy()'''

    def deletevaccination(self):
        self.id = self.txt1.get()
        self.Name = self.txt2.get()
        self.age = self.txt3.get()
        self.gender = self.txt4.get()
        self.email = self.txt5.get()
        self.mobile = self.txt6.get()
        self.date = self.txt7.get()
        self.dose = self.txt8.get()
        self.hospitalName = self.txt9.get()
        self.vaccineID = self.txt10.get()

        conn = connection.Connect()
        cr = conn.cursor()
        q = 'delete from vaccination where id="{}"'.format(self.id)
        cr.execute(q)
        conn.commit()
        showinfo('','Deleted Successfully')
        self.root1.destroy()
        self.getValues()

#main()
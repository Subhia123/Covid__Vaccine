from tkinter import*
from tkinter.ttk import *
from tkinter.messagebox import *
import connection

class main:

    def __init__(self):
        self.root = Tk()
        self.root.title('View Hospital')
        self.root.state('zoomed')
        Label(self.root, text='View Hospital', font=('arial', 32, 'bold', 'underline')).pack(ipady=20)

        col = ('name', 'email','mobile','type')
        self.obj = Treeview(self.root, column=col)
        for i in col:
            self.obj.heading(i, text=i.capitalize())
        self.obj['show'] = 'headings'
        self.obj.bind('<Double-1>', self.updatehospital)
        self.obj.pack()
        self.getValues()
        self.root.mainloop()

    def getValues(self):
        conn = connection.Connect()
        cr = conn.cursor()
        q = 'select name,email,mobile,type from hospitalcamp'
        cr.execute(q)
        result = cr.fetchall()
        print(result)
        count = 0
        for i in self.obj.get_children():
            self.obj.delete(i)
        for i in result:
            self.obj.insert('',index=count,value=i)
            count += 1
    def updatehospital(self,event):
        self.items = self.obj.item(self.obj.focus())['values']
        self.root1 = Toplevel()
        self.root1.title('Update Hospital')
        self.root1.geometry('500x500')

        Label(self.root1, text='Update Hospital', font=('arial',30,'bold','underline')).pack(pady=20)


        Label(self.root1, text='Name :').pack(pady=10)
        self.txt1 = Entry(self.root1, width=50)
        self.txt1.pack()
        self.txt1.insert(1, self.items[0])

        Label(self.root1, text='Email :').pack(pady=10)
        self.txt2 = Entry(self.root1, width=50)
        self.txt2.pack()
        self.txt2.insert(2, self.items[1])

        Label(self.root1, text='Mobile :').pack(pady=10)
        self.txt3 = Entry(self.root1, width=50)
        self.txt3.pack()
        self.txt3.insert(3, self.items[2])

        Label(self.root1, text='Type :').pack(pady=10)
        self.txt4 = Entry(self.root1, width=50)
        self.txt4.pack()
        self.txt4.insert(4, self.items[3])

        Button(self.root1, text='Update',command=self.edithospital).pack(pady=5)
        Button(self.root1, text='Delete', command=self.deletehospital).pack(pady=5)
        self.root1.mainloop()

    def edithospital(self):
        self.Name = self.txt1.get()
        self.email = self.txt2.get()
        self.mobile = self.txt3.get()
        self.type = self.txt4.get()
        q = 'update hospitalcamp set email="{}",mobile="{}",type="{}" where Name="{}"'.format(self.email, self.mobile,self.type,self.Name)
        conn = connection.Connect()
        cr = conn.cursor()
        cr.execute(q)
        conn.commit()
        showinfo('','Hospital Updated Successfully')
        self.getValues()
        self.root1.destroy()

    def deletehospital(self):
        self.Name = self.txt1.get()
        self.email = self.txt2.get()
        self.mobile = self.txt3.get()
        self.type = self.txt4.get()
        conn = connection.Connect()
        cr = conn.cursor()
        q = 'delete from hospitalcamp where Name="{}"'.format(self.Name)
        cr.execute(q)
        conn.commit()
        showinfo('','Deleted Successfully')
        self.root1.destroy()
        self.getValues()

#main()
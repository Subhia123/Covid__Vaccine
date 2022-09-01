from tkinter import*
from tkinter.ttk import*
from tkinter.messagebox import*
import connection

class main:

    def __init__(self):
        self.root = Tk()
        self.root.title('View Admin')
        self.root.state('zoomed')
        Label(self.root, text='View Admins', font=('arial', 32, 'bold', 'underline')).pack(ipady=20)

        col = ('email', 'role')
        self.obj = Treeview(self.root, column=col)
        for i in col:
            self.obj.heading(i, text=i.capitalize())
        self.obj['show'] = 'headings'
        self.obj.bind('<Double-1>', self.updateAdmin)
        self.obj.pack()
        self.getValues()
        self.root.mainloop()

    def getValues(self):
        conn = connection.Connect()
        cr = conn.cursor()
        q = 'select email,role from admin'
        cr.execute(q)
        result = cr.fetchall()
        print(result)
        count = 0
        for i in self.obj.get_children():
            self.obj.delete(i)
        for i in result:
            self.obj.insert('',index=count,value=i)
            count += 1
    def updateAdmin(self,event):
        self.items = self.obj.item(self.obj.focus())['values']
        self.root1 = Toplevel()
        self.root1.title('Update Admin')
        self.root1.geometry('500x500')

        Label(self.root1, text='Update Admin', font=('arial',30,'bold','underline')).pack(pady=20)

        Label(self.root1, text='Email :').pack(pady=10)
        self.txt1 = Entry(self.root1, width=50)
        self.txt1.pack()
        self.txt1.insert(0,self.items[0])
        self.txt1.config(state='readonly')

        Label(self.root1, text='Select Role').pack(pady=10)
        col = ['Super Admin', 'Admin']
        current = col.index(self.items[1])
        print(current)
        self.txt2 = Combobox(self.root1, value=col, width=47, state='readonly')
        self.txt2.current(current)
        self.txt2.pack()

        Button(self.root1, text='Update',command=self.editAdmin).pack(pady=5)
        Button(self.root1, text='Delete', command=self.deleteAdmin).pack(pady=5)
        self.root1.mainloop()

    def editAdmin(self):
        self.email = self.txt1.get()
        self.role = self.txt2.get()
        q = 'update admin set role="{}" where email="{}"'.format(self.role, self.email)
        conn = connection.Connect()
        cr = conn.cursor()
        cr.execute(q)
        conn.commit()
        showinfo('','Admin Updated Successfully')
        self.getValues()
        self.root1.destroy()

    def deleteAdmin(self):
        self.email = self.txt1.get()
        conn = connection.Connect()
        cr = conn.cursor()
        q = 'delete from admin where email="{}"'.format(self.email)
        cr.execute(q)
        conn.commit()
        showinfo('','Deleted Successfully')
        self.root1.destroy()
        self.getValues()

#main()
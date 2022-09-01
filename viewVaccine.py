from tkinter import*
from tkinter.ttk import *
from tkinter.messagebox import *
import connection

class main:

    def __init__(self):
        self.root = Tk()
        self.root.title('View Vaccine')
        self.root.state('zoomed')
        Label(self.root, text='View Vaccine', font=('arial', 32, 'bold', 'underline')).pack(ipady=20)

        col = ('id', 'vaccineName','companyName','alternateName','description','noOfDoses','gap')
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
        q = 'select id, vaccineName, companyName, alternateName, description, noOfDoses, gap from vaccinename'
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
        print(self.items)
        self.root1 = Toplevel()
        self.root1.title('Update Vaccine')
        self.root1.geometry('500x500')

        Label(self.root1, text='Update vaccine', font=('arial',30,'bold','underline')).pack(pady=20)

        Label(self.root1, text='id :').pack(pady=10)
        self.txt1 = Entry(self.root1, width=50)
        self.txt1.pack()
        self.txt1.insert(0,self.items[0])
        self.txt1.config(state='readonly')

        Label(self.root1, text='vaccine Name').pack(pady=10)
        self.txt2 = Entry(self.root1, width=50)
        self.txt2.pack()
        self.txt2.insert(1, self.items[1])

        Label(self.root1, text='company Name :').pack(pady=10)
        self.txt3 = Entry(self.root1, width=50)
        self.txt3.pack()
        self.txt3.insert(2, self.items[2])

        Label(self.root1, text='alternate Name :').pack(pady=10)
        self.txt4 = Entry(self.root1, width=50)
        self.txt4.pack()
        self.txt4.insert(3, self.items[3])

        Label(self.root1, text='description :').pack(pady=10)
        self.txt5 = Entry(self.root1, width=50)
        self.txt5.pack()
        self.txt5.insert(4, self.items[4])

        Label(self.root1, text='noOfDoses :').pack(pady=10)
        self.txt6 = Entry(self.root1, width=50)
        self.txt6.pack()
        self.txt6.insert(5, self.items[5])

        Label(self.root1, text='gap :').pack(pady=10)
        self.txt7 = Entry(self.root1, width=50)
        self.txt7.pack()
        self.txt7.insert(6, self.items[6])

        Button(self.root1, text='Update',command=self.editvaccine).pack(pady=5)
        Button(self.root1, text='Delete', command=self.deletevaccine).pack(pady=5)
        self.root1.mainloop()

    def editvaccine(self):
        self.id=self.txt1.get()
        self.vaccineName = self.txt2.get()
        self.companyName = self.txt3.get()
        self.alternateName = self.txt4.get()
        self.description = self.txt5.get()
        self.noOfDoses = self.txt6.get()
        self.gap = self.txt7.get()
        q = 'update vaccinename set vaccineName="{}" , companyName="{}", alternateName="{}", description="{}", noOfDoses="{}", gap="{}" where id="{}"'.format(self.vaccineName,self.companyName,self.alternateName,self.description,self.noOfDoses,self.gap, self.id)
        conn = connection.Connect()
        cr = conn.cursor()
        cr.execute(q)
        conn.commit()
        showinfo('','Vaccine Updated Successfully')
        self.getValues()
        self.root1.destroy()

    def deletevaccine(self):
        self.id = self.txt1.get()
        self.vaccineName = self.txt2.get()
        self.companyName = self.txt3.get()
        self.alternateName = self.txt4.get()
        self.description = self.txt5.get()
        self.noOfDoses = self.txt6.get()
        self.gap = self.txt7.get()

        conn = connection.Connect()
        cr = conn.cursor()
        q = 'delete from vaccinename where id="{}"'.format(self.id)
        cr.execute(q)
        conn.commit()
        showinfo('','Deleted Successfully')
        self.root1.destroy()
        self.getValues()

#main()
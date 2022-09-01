from tkinter import*
from tkinter.ttk import *
from tkinter.messagebox import *
import connection

class main:

    def __init__(self,name):
        self.name=name
        self.root = Tk()
        self.root.title('View Vaccination')
        self.root.state('zoomed')
        self.f1= Frame(self.root)
        Label(self.f1,text="Search").grid(row=0,column=0)
        self.text=Entry(self.f1,width=40)
        self.text.grid(row=0,column=1,padx=10)
        self.text2=Combobox(self.f1,value=('ID','Name','Aadhaar'),state='readonly')
        self.text2.grid(row=0,column=2)
        Button(self.f1,text='Search',command=self.searchVaccination).grid(row=0,column=3)
        Button(self.f1, text='Refresh', command=self.getValues).grid(row=0, column=4,padx=10)
        Label(self.root, text='View Vaccination', font=('arial', 32, 'bold', 'underline')).pack(ipady=20)
        self.text.delete(0,END)
        self.text2.set('')

        col = ('id', 'name','age','gender','email','mobile','date','dose','hospitalName','vaccineID')
        self.obj = Treeview(self.root, column=col)
        for i in col:
            self.obj.heading(i, text=i.capitalize())
        self.obj['show'] = 'headings'
        self.obj.bind('<Double-1>', self.updatevaccine)
        self.f1.pack(pady=20)
        self.obj.pack()
        self.getValues()
        self.root.mainloop()

    def getValues(self):
        conn = connection.Connect()
        cr = conn.cursor()
        q = 'select id, name,age, gender, email, mobile, date, dose,hospitalName,vaccineID from vaccination where hospitalName="{}"'.format(self.name)
        cr.execute(q)
        result = cr.fetchall()
        print(result)
        count = 0
        for i in self.obj.get_children():
            self.obj.delete(i)
        for i in result:
            self.obj.insert('',index=count,value=i)
            count += 1

    def searchVaccination(self):
        self.s=self.text.get()
        self.c=self.text2.get()
        self.text.delete(0,END)
        self.text2.set('')
        if self.s =='' and self.c=='':
            showerror('','Please Enter Data')
        else:
            if self.s=='ID':
                q='select * from vaccination where id like "{}"'.format(self.s)
            elif self.c=='Name':
                q='select * from vaccination where name like "{}"'.format(self.s)
            else:
                q='select * from vaccination where aadhaar like "{}"'.format(self.s)
            conn=connection.Connect()
            cr=conn.cursor()
            cr.execute(q)
            result=cr.fetchall()
            print(result)
            for i in self.obj.get_children():
                self.obj.delete(i)
            if len(result)>=1:
                count=0
                for i in result:
                    self.obj.insert('',index=count,value=i)
                    count+=1
            else:
                showinfo('','No results Found')



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

        self.root1.mainloop()



#main()
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from tkcalendar import DateEntry
import connection
class main:

    def __init__(self,name):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title('Vaccination Form')
        self.p1 = Panedwindow(self.root)

        Label(self.root, text='Vaccination Form', font=('arial', 30, 'bold', 'underline')).pack()

        Label(self.p1, text='Enter name').grid(row=1, column=0,padx=10,pady=10)
        self.txt1 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt1.grid(row=1, column=1, pady=10)

        Label(self.p1, text='Enter age').grid(row=2, column=0, padx=10, pady=10)
        self.txt2 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt2.grid(row=2, column=1, pady=10)

        Label(self.p1, text='Enter gender').grid(row=3, column=0, padx=10, pady=10)
        self.txt3 = Combobox(self.p1, value=('Male', 'Female', 'Other'), width=50, state='readonly')
        self.p1.pack(pady=10)
        self.txt3.grid(row=3, column=1, pady=10)

        Label(self.p1, text='Enter email').grid(row=4, column=0, padx=10, pady=10)
        self.txt4 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt4.grid(row=4, column=1, pady=10)

        Label(self.p1, text='Enter mobile').grid(row=5, column=0, padx=10, pady=10)
        self.txt5 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt5.grid(row=5, column=1, pady=10)

        Label(self.p1, text='Enter aadhaar').grid(row=6, column=0, padx=10, pady=10)
        self.txt6 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt6.grid(row=6, column=1, pady=10)

        Label(self.p1, text='Enter date').grid(row=7, column=0, padx=10, pady=10)
        self.txt7 = DateEntry(self.p1, width=47)
        self.p1.pack(pady=10)
        self.txt7.grid(row=7, column=1, pady=10)

        Label(self.p1, text='Enter dose').grid(row=8, column=0, padx=10, pady=10)
        self.txt8 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt8.grid(row=8, column=1, pady=10)

        Label(self.p1, text='Enter Hospital Name').grid(row=9, column=0, padx=10, pady=10)
        self.txt9 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt9.grid(row=9, column=1, pady=10)
        self.txt9.insert(0,name)
        self.txt9.config(state='readonly')
        val=self.getVaccineNames()

        Label(self.p1, text='Enter Vaccine Name').grid(row=10, column=0, padx=10, pady=10)
        self.txt10 = Combobox(self.p1, width=50,state='readonly',value=val)
        self.p1.pack(pady=10)
        self.txt10.grid(row=10, column=1, pady=10)

        Button(self.root, text='Submit',command=self.vaccinationForm).pack()
        self.root.mainloop()

    def getVaccineNames(self):
        conn=connection.Connect()
        cr=conn.cursor()
        q='select vaccineName from vaccinename'
        cr.execute(q)
        result=cr.fetchall()
        print(result)
        x=[]
        for i in result:
            x.append(i[0])
        print(x)
        return x

    def vaccinationForm(self):
        self.name = self.txt1.get()
        self.age = self.txt2.get()
        self.gender = self.txt3.get()
        self.email = self.txt4.get()
        self.mobile = self.txt5.get()
        self. aadhaar = self.txt6.get()
        self.date = self.txt7.get()
        self.dose = self.txt8.get()
        self.hospitalName = self.txt9.get()
        self.vaccineName = self.txt10.get()

        conn = connection.Connect()
        cr = conn.cursor()
        q='select id from vaccinename where vaccineName="{}"'.format(self.vaccineName)
        cr.execute(q)
        result=cr.fetchone()
        print(result)
        if self.name == '' and self.age == '' and self.gender== '' and self.email== '' and self.mobile== '' and self.aadhaar== '' and self.date== '' and self.dose== '' and self.hospitalName== '' and self.vaccineName== '':
            showerror('','Please Enter all values')
        else:
            if len(self.mobile)>10 or len(self.aadhaar)> 12:
                showerror('','Invalid Details')
            elif len(self.mobile)<10 or len(self.aadhaar)<12:
                showerror('','Invalid Details')
            else:
                q = 'insert into vaccination values (NULL,"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(self.name,self.age,self.gender,self.email,self.mobile, self.aadhaar, self.date, self.dose, self.hospitalName, result[0])
                print(q)
                cr.execute(q)
                conn.commit()
                connection.createPDF(name=self.name,age=self.age,gender=self.gender,aadhaar=self.aadhaar,vaccineName=self.vaccineName,date=self.date,hospitalName=self.hospitalName,email=self.email)
                showinfo('', 'Information added successfully')

#main(name='subhia')

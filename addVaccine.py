from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import connection
class main:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title('Add Vaccine')
        self.p1 = Panedwindow(self.root)

        Label(self.root, text='Add Vaccine', font=('arial', 30, 'bold', 'underline')).pack()
        Label(self.p1, text='Enter vaccineName').grid(row=0,column=0,padx=10,pady=10)
        self.txt1=Entry(self.p1,width=50)
        self.p1.pack(pady=10)
        self.txt1.grid(row=0, column=1,pady=10)
        Label(self.p1, text='Enter companyName').grid(row=1, column=0,padx=10,pady=10)
        self.txt2 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt2.grid(row=1, column=1, pady=10)
        Label(self.p1, text='Enter alternateName').grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt3.grid(row=2, column=1, pady=10)
        Label(self.p1, text='Enter description').grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt4.grid(row=3, column=1, pady=10)
        Label(self.p1, text='Enter noOfDose').grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt5.grid(row=4, column=1, pady=10)
        Label(self.p1, text='Enter gap').grid(row=5, column=0, padx=10, pady=10)
        self.txt6 = Entry(self.p1, width=50)
        self.p1.pack(pady=10)
        self.txt6.grid(row=5, column=1, pady=10)
        Button(self.root, text='Submit', command=self.addVaccine).pack()
        self.root.mainloop()


    def addVaccine(self):
        self.vaccineName = self.txt1.get()
        self.companyName = self.txt2.get()
        self.alternateName = self.txt3.get()
        self.description = self.txt4.get()
        self.noOfDoses = self.txt5.get()
        self. gap = self.txt6.get()
        conn = connection.Connect()
        cr = conn.cursor()
        if self.vaccineName == '' and self.companyName == '' and self.alternateName== '' and self.description== '' and self.noOfDoses== '' and self.gap== '':
            showerror('','Please Enter all values')
        else:
            q = 'insert into vaccinename values (NULL,"{}","{}","{}","{}","{}","{}")'.format(self.vaccineName, self.companyName, self.alternateName, self.description, self.noOfDoses, self.gap)
            cr.execute(q)
            conn.commit()
            showinfo('', 'Information added successfully')

#main()

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
import addVaccine
import viewVaccine
import viewVaccination1
import addAdmin
import viewAdmin
import changeAdminpass

class main:
    def __init__(self,email):
        self.root = Tk()
        self.root.title('Dashboard')
        self.root.state('zoomed')
        # self.root.geometry("1080x650")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        # self.root.resizable(0,0)
        self.img = Image.open("Covid-19-vaccine-002.jpg")
        self.resized_image = self.img.resize((self.width,self.height-50),Image.ANTIALIAS)
        self.new_img = ImageTk.PhotoImage(self.resized_image)
        self.canvas = Canvas(self.root)
        self.canvas.pack(expand=True,fill="both")
        self.canvas.create_image(0,0,image = self.new_img,anchor='nw')
        self.rootMenu = Menu(self.root)
        self.root.config(menu=self.rootMenu)
        self.userMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='User Management', menu=self.userMenu)
        self.userMenu.add_command(label='Add Admin',command=lambda:addAdmin.main())
        self.userMenu.add_command(label='View Admin', command=lambda: viewAdmin.main())

        self.profileMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='Profile', menu=self.profileMenu)
        self.profileMenu.add_command(label='Change Password',command=lambda:changeAdminpass.changePass(email))
        self.profileMenu.add_command(label='Logout', command=lambda: self.root.destroy())

        self.vaccineMenu= Menu(self.rootMenu,tearoff=0)
        self.rootMenu.add_cascade(label='Vaccine',menu=self.vaccineMenu)
        self.vaccineMenu.add_command(label='Add Vaccine', command=lambda:addVaccine.main())
        self.vaccineMenu.add_command(label='View Vaccine', command=lambda :viewVaccine.main())

        self.viewVaccinationMenu=Menu(self.rootMenu,tearoff=0)
        self.rootMenu.add_command(label='View Vaccination Form',command=lambda:viewVaccination1.main())

        # Label(self.root, text='Welcome to Dashboard', font=('arial', 32, 'bold', 'underline')).pack()
        self.canvas.create_text(self.width/2,50,text='Welcome to Dashboard',font=('arial', 32, 'bold'),fill='red')
        self.root.mainloop()
#main()
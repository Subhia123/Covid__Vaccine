from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import vaccinationForm
import viewVaccination
import changePassword
from PIL import Image,ImageTk
class main:
    def __init__(self,email,name):
        self.root = Tk()
        self.root.title('hospitalMain')
        self.root.state('zoomed')
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        # self.root.resizable(0,0)
        self.img = Image.open("Covid-19-vaccine-003.jpg")
        self.resized_image = self.img.resize((self.width, self.height - 50), Image.ANTIALIAS)
        self.new_img = ImageTk.PhotoImage(self.resized_image)
        self.canvas = Canvas(self.root)
        self.canvas.pack(expand=True, fill="both")
        self.canvas.create_image(0, 0, image=self.new_img, anchor='nw')
        self.rootMenu = Menu(self.root)
        self.root.config(menu=self.rootMenu)
        self.profileMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='Profile', menu=self.profileMenu)
        self.profileMenu.add_command(label='Change Password',command=lambda:changePassword.changePass(email))
        self.profileMenu.add_command(label='Logout',command=lambda:self.root.destroy())

        self.vaccineMenu = Menu(self.rootMenu, tearoff=0)
        #self.rootMenu.add_cascade(label='Vaccination', menu=self.vaccineMenu)
        self.rootMenu.add_command(label='Vaccination Form',command=lambda:vaccinationForm.main(name=name))

        self.viewvaccineFormMenu= Menu(self.rootMenu,tearoff=0)
        self.rootMenu.add_command(label='View Vaccination Form',command=lambda:viewVaccination.main(name=name))
        #Label(self.root, text='Welcome to Dashboard', font=('arial', 32, 'bold', 'underline')).pack()
        self.root.mainloop()
#main()
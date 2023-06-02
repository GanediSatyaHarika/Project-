from tkinter import *
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self .root.geometry("500x400")
        self.root.resizable(False,False)

        title = Label(text="Login Here",font=("Impact",25,"bold"),fg="#6162FF",bg="white").place(x=90,y = 30)
        lbl_name = Label(text="Name",font=("Goudy old style",15,"bold"),fg="#1d1d1d").place(x=90,y = 100)
        self.Name = Entry(font=("Goudy old style",15),bg="#E7E6E6")
        self.Name.place(x=90,y=140,width=200,height=25)

        lbl_id = Label(text="ID", font=("Goudy old style", 15, "bold"), fg="#1d1d1d").place(x=90, y=170)
        self.ID = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
        self.ID.place(x=90, y=210, width=200, height=25)

        lbl_password = Label(text="Password", font=("Goudy old style", 15, "bold"), fg="#1d1d1d").place(x=90, y=240)
        self.Password = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
        self.Password.place(x=90, y=270, width=200, height=25)

        forget = Button(text="Forget Password?", bd=0,cursor="hand2", font=("Goudy old style", 12, "bold"), fg="#1d1d1d").place(x=90, y=300)
        submit = Button(command=self.check_function,cursor="hand2",text="Login?", bd=0, font=("Goudy old style", 15), bg="#6162FF",fg="white").place(x=90, y=330)
    def check_function(self):
        if self.ID.get()=="" or self.Password.get()=="" or self.Name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.ID.get()!="Tech2etc" or self.Password.get()!="123456":
            messagebox.showerror("Error","Invalid ID or Password",parent=self.root)
        else :
            messagebox.showinfo("Welcome",f"Welcome{self.ID.get()}")

root = Tk()
obj = Login(root)
root.mainloop()

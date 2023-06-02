
from tkinter import *
root = Tk()
root.geometry("500x300")
def getvals():
    print("Accepted")

Label(root, text="Library Registration Form", font="ar 15 bold").grid(row=0,column=3)
name = Label(root, text="Name")
idnumber = Label(root, text="ID Number")
contactnumber = Label(root, text="Contact Number")
password = Label(root, text="Password")
name.grid(row=1, column=2)
idnumber.grid(row=2, column=2)
contactnumber.grid(row=4, column=2)
password.grid(row=3, column=2)


namevalue = StringVar
idnumbervalue = StringVar
contactnumbervalue = StringVar
passwordvalue = StringVar
checkvalue = IntVar
nameentry = Entry(root, textvariable=namevalue)
idnumberentry = Entry(root, textvariable=idnumbervalue)
contactnumberentry = Entry(root, textvariable=contactnumbervalue)
passwordentry = Entry(root, textvariable=passwordvalue)
nameentry.grid(row=1, column=3)
idnumberentry.grid(row=2, column=3)
contactnumberentry.grid(row=4, column=3)
passwordentry.grid(row=3, column=3)
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=5, column=3)
Button(text="Submit", command=getvals).grid(row=6, column=3)


















root.mainloop()

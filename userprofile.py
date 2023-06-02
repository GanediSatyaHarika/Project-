from tkinter import *
root = Tk()
root.geometry("500x300")
Label(root, text="User Profile", font="ar 15 bold").grid(row=0,column=3)
name = Label(root, text="name")
id = Label(root, text="ID")
contactnumber = Label(root, text="Contact Number")
numberofbooksborrowed = Label(root, text="Number Of Books Borrowed")
finepending = Label(root, text="Fine Pending")

name.grid(row=1, column=2)
id.grid(row=2, column=2)
contactnumber.grid(row=3, column=2)
numberofbooksborrowed.grid(row=4, column=2)
finepending.grid(row=5, column=2)

namevalue = StringVar
idvalue = StringVar
contactnumbervalue = StringVar
numberofbooksborrowedvalue = StringVar
finependingvalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable =namevalue)
identry = Entry(root, textvariable =idvalue)
contactnumberentry = Entry(root, textvariable =contactnumbervalue)
numberofbooksborrowedentry = Entry(root, textvariable =numberofbooksborrowedvalue)
finependingentry = Entry(root, textvariable =finependingvalue)

nameentry.grid(row=1, column=3)
identry.grid(row=2, column=3)
contactnumberentry.grid(row=3, column=3)
numberofbooksborrowedentry.grid(row=4, column=3)
finependingentry.grid(row=5, column=3)














root.mainloop()






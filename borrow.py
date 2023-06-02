from tkinter import*
from tkinter import ttk
root = Tk()
root.title("Borrow")
root.geometry("600x470")
root.resizable(False,False)
Label(text="Enter a book name:",font=23).place(x=50,y=100)
ttk.Combobox(font=("times new roman",13)).place(x=250,y=100)
Label(text="Book name",font=23).place(x=50,y=150)
Label(text="Book_ID",font=23).place(x=50,y=200)
Label(text="status",font=23).place(x=50,y=250)
Entry(font=("times new roman",15)).place(x=250,y=150)
Entry(font=("times new roman",15)).place(x=250,y=200)
Entry(font=("times new roman",15)).place(x=250,y=250)
Button(text="Borrow",font=20,width=11,height=2).place(x=210,y=350)

root.mainloop()
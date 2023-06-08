import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import date, timedelta
current_date = date.today()
new_date = current_date + timedelta(days=30)
new_date_string = new_date.strftime("%Y-%m-%d")

cnx = pymysql.connect(user='root', password='Ramana110$',
                              host='127.0.0.1', database='library')
cursor = cnx.cursor()


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        title = Label(text="Login Here", font=("Comic Sans", 25, "bold"), fg="#6162FF", bg="light gray")
        title.place(x=90, y=30)

        lbl_name = Label(text="Name", font=("Goudy old style", 15, "bold"), fg="#1d1d1d")
        lbl_name.place(x=90, y=100)
        self.Name = Entry(font=("Goudy old style", 15), bg="#E7E6E6", bd=4)
        self.Name.place(x=90, y=140, width=200, height=25)

        lbl_id = Label(text="ID", font=("Goudy old style", 15, "bold"), fg="#1d1d1d")
        lbl_id.place(x=90, y=170)
        self.ID = Entry(font=("Goudy old style", 15), bg="#E7E6E6", bd=4)
        self.ID.place(x=90, y=210, width=200, height=25)

        lbl_password = Label(text="Password", font=("Goudy old style", 15, "bold"), fg="#1d1d1d")
        lbl_password.place(x=90, y=240)
        self.Password = Entry(font=("Goudy old style", 15), bg="#E7E6E6", show='*', bd=4)
        self.Password.place(x=90, y=270, width=200, height=25)

        create_acc = Button(command=self.create_account, text="Create Account", bd=0, cursor="hand2",
                            font=("Goudy old style", 12, "bold"), fg="#1d1d1d")
        create_acc.place(x=90, y=300)

        submit = Button(command=self.check_function, cursor="hand2", text="Login", bd=0,
                        font=("Goudy old style", 15), bg="#6162FF", fg="white")
        submit.place(x=90, y=330)

    def check_function(self):
        cursor.execute(f"select student_name, student_id, student_passwordl, student_contact_number, no_book_borrowed, fine_pending from library.student_users")
        detail_list = cursor.fetchall()
        count = 0
        for i in range(len(detail_list)):
            count += 1
            if self.ID.get() == "" or self.Password.get() == "" or self.Name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                break
            elif not self.ID.get().isdigit():
                messagebox.showerror("Error", "Enter numbers in ID", parent=self.root)
                break
            elif not self.Name.get().isalpha():
                messagebox.showerror("Error", "Enter names in Name", parent=self.root)
                break
            elif self.ID.get() == str(detail_list[i][1]) and self.Password.get() == detail_list[i][2] and self.Name.get() == detail_list[i][0]:
                count = 1
                messagebox.showinfo("Welcome", f"Welcome {self.Name.get()} to IIT PALAKKAD library")
                main_window(self.ID.get())
                break
            elif count == len(detail_list):
                messagebox.showerror("Error", "Invalid Name or ID or Password", parent=self.root)
                break

    def create_account(self):
        create_account_root = Toplevel(self.root)
        create_account_root.geometry("500x300")
        create_account_root.title("Create Account")
        Label(create_account_root, text="Library Registration Form", font="ar 15 bold").grid(row=0, column=3)
        name = Label(create_account_root, text="Name")
        id_number = Label(create_account_root, text="ID Number")
        contact_number = Label(create_account_root, text="Contact Number")
        password = Label(create_account_root, text="Password")

        name.grid(row=1, column=2)
        id_number.grid(row=2, column=2)
        contact_number.grid(row=4, column=2)
        password.grid(row=3, column=2)

        name_value = StringVar()
        id_number_value = StringVar()
        contact_number_value = StringVar()
        password_value = StringVar()

        name_entry = Entry(create_account_root, textvariable=name_value)
        id_number_entry = Entry(create_account_root, textvariable=id_number_value)
        contact_number_entry = Entry(create_account_root, textvariable=contact_number_value)
        password_entry = Entry(create_account_root, textvariable=password_value)

        name_entry.grid(row=1, column=3)
        id_number_entry.grid(row=2, column=3)
        contact_number_entry.grid(row=4, column=3)
        password_entry.grid(row=3, column=3)

        submit1 = Button(create_account_root, text="Submit",
                         command=lambda: (self.getvals(name_entry.get(), id_number_entry.get(),
                                                       password_value.get(), contact_number_value.get()),
                                          root.destroy()))
        submit1.grid(row=6, column=3)

    def getvals(self, stu_name, stu_id, stu_pass, stu_con_num):
        try:
            if stu_name == "" and stu_id == "" and stu_pass == "" and stu_con_num == "":
                messagebox.showerror("Error!", "All fields are required")
            elif stu_name == "":
                messagebox.showerror("Error!", "Enter name")
            elif stu_id == "":
                messagebox.showerror("Error!", "Enter id")
            elif stu_pass == "":
                messagebox.showerror("Error!", "Enter password")
            elif stu_con_num == "":
                messagebox.showerror("Error!", "Enter contact number")
            else:
                values = (stu_name, int(stu_id), stu_pass, int(stu_con_num))
                sql1 = "INSERT INTO library.student_users (student_name, student_id, student_passwordl, student_contact_number) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql1, values)
                cnx.commit()
                cursor.execute('SELECT * FROM library.student_users')
                user = cursor.fetchall()
                for i in user:
                    if values == i[0:4]:
                        messagebox.showinfo("Thank You!!", "Your account is created")
                        homepage()

        except pymysql.connector.errors.IntegrityError as err:
            def list_detail():
                cursor.execute("SELECT student_name, student_id, student_passwordl, student_contact_number, no_book_borrowed, fine_pending FROM library.student_users")
                detail_list = cursor.fetchall()
                return detail_list


def user_page(root, id_num):
    cursor.execute(f"SELECT student_name, student_id, student_contact_number, no_book_borrowed, fine_pending FROM library.student_users WHERE student_id = {id_num}")
    detail_list = cursor.fetchall()

    root.title("User Details")
    root.geometry("500x400")
    Label(root, text="User Profile", font="ar 15 bold").grid(row=0, column=3)
    name = Label(root, text="Name")
    id1 = Label(root, text="ID")
    contactnumber = Label(root, text="Contact Number")
    numberofbooksborrowed = Label(root, text="Number Of Books Borrowed")
    finepending = Label(root, text="Fine Pending")

    name.grid(row=1, column=2)
    id1.grid(row=2, column=2)
    contactnumber.grid(row=3, column=2)
    numberofbooksborrowed.grid(row=4, column=2)
    finepending.grid(row=5, column=2)

    namevalue = StringVar()
    id1value = StringVar()
    contactnumbervalue = StringVar()
    numberofbooksborrowedvalue = StringVar()
    finependingvalue = StringVar()

    nameentry = Label(root, text=detail_list[0][0])
    id1entry = Label(root, text=detail_list[0][1])
    contactnumberentry = Label(root, text=detail_list[0][2])
    numberofbooksborrowedentry = Label(root, text=detail_list[0][3])
    finependingentry = Label(root, text=detail_list[0][4])

    nameentry.grid(row=1, column=3)
    id1entry.grid(row=2, column=3)
    contactnumberentry.grid(row=3, column=3)
    numberofbooksborrowedentry.grid(row=4, column=3)
    finependingentry.grid(row=5, column=3)
    cursor.execute(f"SELECT book_name FROM library.borrower_table WHERE borrower_id = {id_num}")
    book_list = cursor.fetchall()
    book = []
    book_na = []
    if book_list != []:
        for i in range(len(book_list)):
            book.append(Label(root, text=f"book {i+1} : "))
            book[i].grid(row=6+i, column=2)
            book_na.append(Label(root, text=book_list[i]))
            book_na[i].grid(row=6+i, column=3)
    back = Button(root, text="Back", command=lambda: (root.destroy(), main_window(id_num)))
    back.grid(row=8 + len(book_list), column=2)
    root.mainloop()


def homepage():
    messagebox.showinfo("Exit", "Exiting from the server")


def open_details_window(func1, id_num):
    cursor.execute(f"SELECT no_book_borrowed FROM library.student_users WHERE student_id = {id_num}")
    res1 = cursor.fetchone()
    if func1 == user_page:
        # Create a new window for details
        details_window = Toplevel(root)

        # Execute the passed function in the details window
        func1(details_window, id_num)
    elif func1 == borrow:
        if res1[0] < 4:
            # Create a new window for details
            details_window = Toplevel(root)

            # Execute the passed function in the details window
            func1(details_window, id_num)
            # Create the main window
        else:
            messagebox.showinfo("Maximum Reached", "You already borrowed your maximum limit books. Please return any books to borrow")
            homepage()
    elif func1 == return_main:
        if res1[0] > 0:
            # Create a new window for details
            details_window = Toplevel(root)

            # Execute the passed function in the details window
            func1(details_window, id_num)
            # Create the main window
        else:
            messagebox.showinfo("Manimum Reached", "You don't have any books to return. Please borrow any books")


def get_names():
    global names
    cursor.execute("SELECT distinct Book_Name FROM library.books")
    res = cursor.fetchall()
    names = [row[0] for row in res]
    return names


def insert_names(id_num, name_listBox, root):
    select_indices = name_listBox.curselection()
    if select_indices and name_user != '':
        select_index = select_indices[0]
        select_name = name_listBox.get(select_index)
        name_entry.delete(0, END)
        name_entry.insert(END, select_name)
        name_listBox.delete(0, END)
        search_books(select_name, id_num, root)
    elif name_user != '':
        name_entry.delete(0, END)
        name_listBox.delete(0, END)
        search_books(name_user, id_num, root)


def headings(root, deta, id_num):
    for widget in root.winfo_children():
        if widget not in [name_listBox, name_entry, search_button]:
            widget.destroy()
        else:
            name = Label(root, text="Name")
            idnumber = Label(root, text="ID Number")
            author = Label(root, text="Author")
            ana = Label(root, text="Available/Non-Available")
            name.grid(row=1, column=2)
            idnumber.grid(row=1, column=4)
            author.grid(row=1, column=6)
            ana.grid(row=1, column=8)

            for i in range(len(deta)):
                nameentry = Label(root, text=deta[i][1])
                idnumberentry = Label(root, text=deta[i][0])
                authorentry = Label(root, text=deta[i][2])
                anaentry = Label(root, text=deta[i][3])
                nameentry.grid(row=i + 2, column=2)
                idnumberentry.grid(row=i + 2, column=4)
                authorentry.grid(row=i + 2, column=6)
                anaentry.grid(row=i + 2, column=8)

                borrow_buttons = []
                borrow_button = Button(root, text="Borrow", state=DISABLED)
                borrow_button.grid(row=i + 2, column=10, padx=5, pady=5)

                if deta[i][3] == "available":
                    borrow_button.configure(state=NORMAL)
                    borrow_button.configure(command=lambda i=i: (root.destroy(), borrow_bk_button(id_num, deta[i][1], deta[i][0])))

                borrow_buttons.append(borrow_button)
            books_borrowed = Label(root, text="No. of books borrowed:")
            books_borrowed.grid(row=len(deta) + 3, column=2)

            cursor.execute(f"select no_book_borrowed from library.student_users where student_id = {id_num}")
            res2 = cursor.fetchone()

            books_borrowed_entry = Label(root, text=res2)
            books_borrowed_entry.grid(row=len(deta) + 3, column=3)

            bck_go = Button(root, text='Back', command=lambda: (root.destroy(), main_window(id_num)))
            bck_go.grid(row=len(deta) + 2, column=2)


def borrow_bk_button(id_num, bk_nm, bk_id):
    cursor.execute("select `s.no` from library.borrower_table")
    k_list = cursor.fetchall()
    k_list = [i[0] for i in k_list]
    k_list.append(0)
    k = max(k_list)
    k += 1
    cursor.execute(f"select student_name, no_book_borrowed from library.student_users where student_id = {id_num}")
    res3 = cursor.fetchall()
    cursor.execute("INSERT INTO library.borrower_table(`s.no`, book_name, book_id, borrower_name, borrower_id, date_of_borrowing, due_date) VALUES(%s, %s, %s, %s, %s, %s, %s)", (k, bk_nm, bk_id, res3[0][0], id_num, current_date, new_date))
    cnx.commit()
    sta = "non-available"
    sql12 = f"update library.books set `available/non-available` = '{sta}' where Book_id = {bk_id}"
    cursor.execute(sql12)
    cnx.commit()
    cursor.execute(f"UPDATE library.student_users set `no_book_borrowed` = {res3[0][1] + 1} where student_id = {id_num}")
    cnx.commit()
    messagebox.showinfo("Thanks", f"You had borrowed the book {bk_nm} with id: {bk_id} successfully on {current_date}")
    main_window(id_num)


def search_books(book_name, id_num, root):
    try:
        cursor.execute("SELECT Book_id, Book_Name, Book_Author, `available/non-available` FROM library.books WHERE Book_Name = %s", (book_name,))
        res = cursor.fetchall()
        if book_name.lower() in res[0][1].lower():
            headings(root, res, id_num)
        else:
            messagebox.showinfo("Error!", "Enter correct book_name")
    except IndexError:
        messagebox.showinfo("Availability", f"The book {book_name} is not available with us")


def searchBooks(root, id_num):
    global name_user
    name_user = name_entry.get().lower()
    if name_user:
        insert_names(id_num, name_listBox, root)
    elif name_user == '':
        messagebox.showinfo("Error", "Enter the name of book.")
    else:
        name_listBox.delete(0, END)
        name_listBox.grid_forget()


def suggest_details(name_entry, names, name_listBox):
    name_user = name_entry.get().lower()
    name_list = [name for name in names if name_user in name.lower()]
    name_listBox.delete(0, END)
    for name in name_list:
        name_listBox.insert(END, name)


def update_suggestion(event):
    global name_user
    name_user = name_entry.get().lower()

    name_listBox.delete(0, END)

    if name_user:
        name_listBox.grid(row=3, column=0)
        name_list = [name for name in names if name_user in name.lower()]
        for name in name_list:
            name_listBox.insert(END, name)
    else:
        name_listBox.delete(0, END)
        name_listBox.pack_forget()


def borrow(root, id_num):
    root.geometry("650x400")
    root.resizable(False, False)
    root.title("Name Search")
    global name_entry, name_listBox, book_details_frame, search_button
    roll_no = Label(root, text="Student ID")
    roll_no.grid(row=0, column=0)
    roll_no_entry = Label(root, text=id_num)
    roll_no_entry.grid(row=0, column=1)
    info_bar = Label(root, text="Enter the name of\n the book you need", wraplength=200)
    info_bar.grid(row=1, column=0)

    name_entry = Entry(root)
    name_entry.grid(row=2, column=0, padx=5, pady=5)

    name_listBox = Listbox(root)
    name_listBox.grid(row=3, column=0, padx=5, pady=5)

    search_button = Button(root, text="Search", command=lambda: searchBooks(root, id_num))
    search_button.grid(row=2, column=1, padx=5, pady=5)

    back_button = Button(root, text="Back", command=lambda: (root.destroy(), main_window(id_num)))
    back_button.grid(row=8, column=2, padx=10, pady=10)

    name_entry.bind('<KeyRelease>', update_suggestion)
    name_entry.bind('<FocusOut>', lambda event: name_listBox.grid_forget())  # Hide the listbox when focus is lost
    name_listBox.bind('<<ListboxSelect>>', lambda event: insert_names(id_num, name_listBox, root))
    names = get_names()
    root.mainloop()


def return_list(root, combobox, id_num):
    selected_book = combobox.get()
    j = 0
    book_id = []
    book_name = []
    borrowed_date = []
    due_date = []
    return_date = []
    fine_amount = []
    return_button = []
    val = []

    for widget in root.winfo_children():
        if widget not in [roll_label, name_label, back_button, combobox, enter_button]:
            widget.destroy()

    for i in range(len(res1)):
        if selected_book in res1[i][0]:
            res2 = res1[i]
            fn = 0 if (current_date - res2[5]) < timedelta(days=0) else (current_date - res2[5]).days * 1
            val.append((res2[0], res2[1], res2[2], res2[3], res2[4], res2[5], current_date, fn))
            book_id.append(Label(root, text="Book ID :"))
            book_id[j].grid(row=3 + j, column=0, padx=10, pady=10)
            book_name.append(Label(root, text="Book Name :"))
            book_name[j].grid(row=3 + j, column=1, padx=10, pady=10)
            borrowed_date.append(Label(root, text="Borrowed Date :"))
            borrowed_date[j].grid(row=3 + j, column=2, padx=10, pady=10)
            due_date.append(Label(root, text="Due Date :"))
            due_date[j].grid(row=3 + j, column=3, padx=10, pady=10)
            return_date.append(Label(root, text="Today Date :"))
            return_date[j].grid(row=3 + j, column=4, padx=10, pady=10)
            fine_amount.append(Label(root, text="Fine Amount :"))
            fine_amount[j].grid(row=3 + j, column=5, padx=10, pady=10)
            book_id[j].config(text=f"Book ID : {res2[1]}")
            book_name[j].config(text=f"Book Name : {res2[0]}")
            borr_date = res2[4].strftime("%Y-%m-%d")
            du_date = res2[5].strftime("%Y-%m-%d")
            curr_date = current_date.strftime("%Y-%m-%d")
            borrowed_date[j].config(text=f"Borrowed Date : {borr_date}")
            due_date[j].config(text=f"Due Date : {du_date}")
            return_date[j].config(text=f"Today Date : {current_date}")
            fine_amount[j].config(text=f"Fine Amount : {fn}")
            # Return button
            return_button.append(Button(root, text="Return", command=lambda j=j: (
                root.destroy(), return_book(val[j], id_num, j), main_window(id_num))))
            return_button[j].grid(row=3 + j, column=6, padx=10, pady=10)
            j += 1


def return_book(val, id_num, j):
    cursor.execute("select `s.no` from library.check_out")
    k_list = cursor.fetchall()
    k_list = [i[0] for i in k_list]
    k_list.append(0)
    k = max(k_list)
    k += 1
    val = list(val)
    sta = 'available'
    sql12 = f"update library.books set `available/non-available`= '{sta}' where Book_id= {val[1]}"
    cursor.execute(sql12)
    cnx.commit()
    cursor.execute(f"select `no_book_borrowed` from library.student_users where student_id= {id_num}")
    resnbb = cursor.fetchone()
    cursor.execute(
        f"UPDATE library.student_users set `no_book_borrowed`= {resnbb[0] - 1} where student_id= {id_num}")
    cnx.commit()
    val.append(k)
    cursor.execute(
        f"insert into library.check_out (chk_book_name, ch_book_id, chk_borrower_name, chk_borrower_id, borrowed_date, due_date, date_of_return, fine_amount, `s.no`)"
        "values(%s, %s, %s, %s, %s, %s, %s, %s, %s)", val)
    cnx.commit()
    condition1 = "borrower_id= %s"
    condition2 = "book_id = %s"
    value1 = id_num
    value2 = val[1]
    cursor.execute(f"delete from library.borrower_table where {condition1} and {condition2}", (value1, value2))
    cnx.commit()
    messagebox.showinfo("Returned", f"{val[2]} successfully returned the book {val[0]} with id {val[1]}")


def return_main(root, id_num):
    cursor.execute(f"select book_name, book_id, borrower_name, borrower_id, date_of_borrowing, due_date from library.borrower_table where borrower_id = {id_num}")
    global res1
    res1 = cursor.fetchall()
    book_options = list(set([res1[i][0] for i in range(len(res1))]))
    combobox = Combobox(root, values=book_options)
    combobox.grid(row=1, column=0)

    global roll_label, name_label, enter_button, back_button

    roll_label = Label(root, text="Roll No:")
    roll_label.grid(row=0, column=0, padx=10, pady=10)

    name_label = Label(root, text="Name:")
    name_label.grid(row=0, column=1, padx=10, pady=10)
    roll_no = res1[0][3]
    name = res1[0][2]

    enter_button = Button(root, text="Enter", command=lambda: return_list(root, combobox, id_num))
    enter_button.grid(row=1, column=1)

    roll_label.config(text=f"Roll No: {roll_no}")
    name_label.config(text=f"Name: {name}")

    back_button = Button(root, text="Back", command=lambda: (root.destroy(), main_window(id_num)))
    back_button.grid(row=4 + len(res1), column=0, columnspan=2)

    root.mainloop()


selected_book = None


def main_window(id_num):
    root = Tk()
    button1 = Button(root, text="User Profile", command=lambda: (root.destroy(), open_details_window(user_page, id_num)))
    button1.pack(side='left', padx=20, pady=100)
    button2 = Button(root, text="Borrow", command=lambda: (root.destroy(), open_details_window(borrow, id_num)))
    button2.pack(side='left', padx=20, pady=100)
    button3 = Button(root, text="Return", command=lambda: (root.destroy(), open_details_window(return_main, id_num)))
    button3.pack(side='left', padx=20, pady=100)
    button4 = Button(root, text="Log Out", command=lambda: (root.destroy(), homepage()))
    button4.pack(side='left', padx=20, pady=100)
    root.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()

cnx.close()

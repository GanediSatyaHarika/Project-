from tkinter import *
from tkinter.ttk import Combobox
from datetime import date, timedelta
current_date = date.today()
new_date = current_date + timedelta(days=30)
new_date_string = new_date.strftime("%Y-%m-%d")
import mysql.connector
cnx=mysql.connector.connect(user='root',password='Ramana110$',
                            host='127.0.0.1',database='library')
cursor=cnx.cursor()

def return_book(root,combobox):

    selected_book = combobox.get()
    print(selected_book)

    book_id = Label(root, text="Book ID:")
    book_id.grid(row=3, column=0)

    book_name = Label(root, text="Book Name:")
    book_name.grid(row=3, column=0)
    
    borrowed_date = Label(root, text="Borrowed date")
    borrowed_date.grid(row=3, column=0)

    due_date = Label(root, text="Due date")
    due_date.grid(row=3, column=0)

    today_date = Label(root, text="today_date:")
    today_date.grid(row=3, column=0)

    fine_amount = Label(root, text="Fine Amount:")
    fine_amount.grid(row=3, column=0)

    print(selected_book)
    

    for i in range(len(res1)):
                if res1[i][0]==selected_book:
                    res2=res1[i]
                    fn = 0 if (current_date - res2[5]) < timedelta(days=0) else (current_date - res2[5]).days * 1
                    val=(res2[0],res2[1],res2[2],res2[3],res2[4],res2[5],current_date,fn)
                    cursor.execute(f"insert library.check_out (chk_book_name, ch_book_id, chk_borrower_name, chk_borrower_id, borrowed_date, due_date, date_of_return, fine_amount)"
                                      "values(%s,%s,%s,%s,%s,%s,%s,%s)",val)
                    cnx.commit
                    print(res2)
        

    # Return button
    return_button = Button(root, text="Return")
    return_button.grid(row=3, column=3)

# Create the main window
def return_main(id_num):
        
    root = Tk()

    # Create the combobox with book options
    cursor.execute(f"select book_name, book_id, borrower_name, borrower_id, date_of_borrowing, due_date from library.borrower_table where borrower_id={id_num}")
    global res1
    res1=cursor.fetchall()
    print(res1)
    book_options=[res1[i][0] for i in range(len(res1))]
    combobox = Combobox(root, values=book_options)
    combobox.grid(row=1, column=0)

    # Labels to display roll number, name, and book details
    roll_label = Label(root, text="Roll No:")
    roll_label.grid(row=0, column=0)

    name_label = Label(root, text="Name:")
    name_label.grid(row=0, column=1)

    roll_no = res1[0][3]
    name = res1[2][2]

    # Enter button
    enter_button = Button(root, text="Enter", command=lambda:return_book(root,combobox))
    enter_button.grid(row=1, column=1)



    # Displaying roll number and name
    roll_label.config(text=f"Roll No: {roll_no}")
    name_label.config(text=f"Name: {name}")

    # Back button
    back_button = Button(root, text="Back")
    back_button.grid(row=4, column=0, columnspan=2)

    # Start the main event loop
    root.mainloop()
selected_book=None
return_main(123)



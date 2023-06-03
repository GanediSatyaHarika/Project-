from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import date, timedelta
current_date = date.today()
new_date = current_date + timedelta(days=30)
new_date_string = new_date.strftime("%Y-%m-%d")
import mysql.connector
cnx=mysql.connector.connect(user='root',password='Ramana110$',
                            host='127.0.0.1',database='library')
cursor=cnx.cursor()


def return_list(root,combobox):

    selected_book = combobox.get()
    print(selected_book)
    
    j=0
    book_id=[]
    book_name=[]
    borrowed_date=[]
    due_date=[]
    return_date=[]
    fine_amount=[]
    return_button=[]    
    val=[]
    for widget in root.winfo_children():
        if widget not in [roll_label,name_label,back_button,combobox,enter_button]: 
            widget.destroy()
    for i in range(len(res1)):
                print(i,j)
                if selected_book in res1[i][0] :
                    print("1",res1[i])
                    res2=res1[i]
                    fn = 0 if (current_date - res2[5]) < timedelta(days=0) else (current_date - res2[5]).days * 1
                    print(fn)
                    val.append((res2[0],res2[1],res2[2],res2[3],res2[4],res2[5],current_date,fn))
                    print(res2)
                    
                    book_id.append(Label(root, text="Book ID :"))
                    print(len(book_id))
                    book_id[j].grid(row=3+j, column=0,padx=10,pady=10)

                    book_name.append(Label(root, text="Book Name :"))
                    book_name[j].grid(row=3+j, column=1,padx=10,pady=10)
                    
                    borrowed_date.append(Label(root, text="Borrowed Date :"))
                    borrowed_date[j].grid(row=3+j, column=2,padx=10,pady=10)

                    due_date.append(Label(root, text="Due Date :"))
                    due_date[j].grid(row=3+j, column=3,padx=10,pady=10)

                    return_date.append(Label(root, text="Today Date :"))
                    return_date[j].grid(row=3+j, column=4,padx=10,pady=10)

                    fine_amount.append(Label(root, text="Fine Amount :"))
                    fine_amount[j].grid(row=3+j, column=5,padx=10,pady=10)

                    
                    book_id[j].config(text=f"Book ID : {res2[1]}")

                    book_name[j].config(text=f"Book Name : {res2[0]}")

                    borr_date = res2[4].strftime("%Y-%m-%d")
                    du_date = res2[5].strftime("%Y-%m-%d")
                    curr_date=current_date.strftime("%Y-%m-%d")

                    
                    borrowed_date[j].config(text=f"Borrowed Date : {borr_date}")

                    due_date[j].config(text=f"Due Date : {du_date}")

                    return_date[j].config(text=f"Today Date : {current_date}")

                    fn=str(fn)
                    fine_amount[j].config(text="Fine Amount : {fn}")

                    # Return button
                    return_button.append(Button(root, text="Return",command=lambda j=j:return_book(val[j],id_num)))
                    return_button[j].grid(row=3+j, column=6,padx=10,pady=10)
                    j+=1
def return_book(val,id_num):
    cursor.execute("select `s.no` from library.check_out")
    k_list=cursor.fetchall()
    k_list=[i[0] for i in k_list]
    k_list.append(0)
    print(k_list)
    k=max(k_list)
    k+=1
    val=list(val)
    print(val)
    sta='available'
    sql12=f"update library.books set `available/non-available` ='{sta}' where Book_id={val[1]}"
    cursor.execute(sql12)
    cnx.commit()

    cursor.execute(f"select `no_book_borrowed` from library.student_users where student_id={id_num}")
    resnbb=cursor.fetchone()
    cursor.execute(f"UPDATE library.student_users set `no_book_borrowed`={resnbb[0]-1} where student_id={id_num}")
    cnx.commit()
    #messagebox.showinfo("Thanks",f"You had borrowed the book {bk_nm} with id: {bk_id} successfully on {current_date}")

    val.append(k)
    cursor.execute(f"insert into library.check_out (chk_book_name, ch_book_id, chk_borrower_name, chk_borrower_id, borrowed_date, due_date, date_of_return, fine_amount,`s.no`)"
                                   "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",val)
    cnx.commit()
    condition1="borrower_id=%s"
    condition2="book_id=%s"
    value1=id_num
    value2=val[1]
    cursor.execute(f"delete from library.borrower_table where {condition1} and {condition2}",(value1,value2))
    cnx.commit()
    

# Create the main window
def return_main(id_num):
        
    root = Tk()

    # Create the combobox with book options
    cursor.execute(f"select book_name, book_id, borrower_name, borrower_id, date_of_borrowing, due_date from library.borrower_table where borrower_id={id_num}")
    global res1
    res1=cursor.fetchall()
    print(res1)
    book_options=list(set([res1[i][0] for i in range(len(res1))]))
    combobox = Combobox(root, values=book_options)
    combobox.grid(row=1, column=0)

    global roll_label,name_label,enter_button,back_button

    # Labels to display roll number, name, and book details
    roll_label = Label(root, text="Roll No:")
    roll_label.grid(row=0, column=0,padx=10,pady=10)

    name_label = Label(root, text="Name:")
    name_label.grid(row=0, column=1,padx=10,pady=10)

    roll_no = res1[0][3]
    name = res1[2][2]

    # Enter button
    enter_button = Button(root, text="Enter", command=lambda:return_list(root,combobox))
    enter_button.grid(row=1, column=1)



    # Displaying roll number and name
    roll_label.config(text=f"Roll No: {roll_no}") #need to check what is config?
    name_label.config(text=f"Name: {name}") #need to check what is config?

    # Back button
    back_button = Button(root, text="Back",command=return_main(id_num))
    back_button.grid(row=4+len(res1), column=0, columnspan=2)

    # Start the main event loop
    root.mainloop()
selected_book=None
id_num=123
return_main(id_num)


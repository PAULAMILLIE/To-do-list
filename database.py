import tkinter as tk
from tkinter import *
import _sqlite3
from tkinter import messagebox
import os




root=Tk()
root.title('my database')
root.geometry('400x400')

conn = _sqlite3.connect('HMM.db')

cur=conn.cursor()

cur.execute('''CREATE TABLE if not exists active(
  task_list text,
  deadline date)
''')


my_frame = tk.Frame(root)
my_frame.pack(pady=10)
def submit():
  conn = _sqlite3.connect('HMM.db')

cur=conn.cursor()

my_entry = tk.Entry(my_frame, font=('Times New Roman', 15), width=25)
my_entry.grid(row=0, column=1, padx=12, pady=5)

date_entry = tk.Entry(my_frame, font=('Times New Roman', 15), width=25)
date_entry.grid(row=1, column=1, padx=12, pady=5)


cur.execute('''INSERT INTO active VALUES(:my_entry, :date_entry)''',
    
           {
               'my_entry':my_entry.get(),
               'date_entry':my_entry.get()
           })

conn.commit()
conn.close()

my_entry.delete(0, END)
date_entry.delete(0,END)

def query():
     conn = _sqlite3.connect('HMM.db')

     cur=conn.cursor()

     cur.execute("SELECT *, oid FROM active")
     records = cur.fetchall()
     print(records)

     print_records=''
     for record in records:
         print_records += str(record[0]) +" "+str(record[1]) + "\n"
     query_label = tk.Label(root, text= print_records)
     query_label.grid(row=2, column=0, padx=12, pady=5)







     conn.commit()
     conn.close()





my_entry_label = tk.Label(my_frame, text='Enter Task:', font=('Arial', 12))
my_entry_label.grid(row=0, column=0, padx=12, pady=5)
date_entry_label = tk.Label(my_frame, text='Deadline:', font=('Arial', 12))
date_entry_label.grid(row=1, column=0, padx=12, pady=5)

my_list = tk.Listbox(root, font=('Times New Roman', 15),
                    height=5, width=80, bg='#FFFAF4', bd=0,
                    fg='#000000', highlightthickness=0,
                    selectbackground="#73777B", activestyle='none')
my_list.pack(fill='both', padx=20, pady=10)



def delete_item():
    selected_item = my_list.curselection()
    if selected_item:
        task_id =  selected_item[0] + 1  #index to adjust in db
        my_list.delete(selected_item)

    else:
        messagebox.showwarning('Warning', 'No selected item')

def add_item():
    task = my_entry.get()
    if task:
        deadline = date_entry.get()
        task_with_deadline = f"{task} (deadline: {deadline})"
        my_list.insert('end', task_with_deadline)
        my_entry.delete(0, 'end')
        date_entry.delete(0, 'end')

        #add task to db

    else:
        messagebox.showwarning('Warning', 'Please enter a task.')

def clear_item():
    confirmed = messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all tasks?")
    if confirmed:
        my_list.delete(0, 'end')




# Add tasks to the list with deadline dates
tasks = []
for item in tasks:
    my_list.insert('end', item)


delete_button = tk.Button(root, text='DEL TASK', font=('Arial', 12), bg='#F1F0E8', command=delete_item)
add_button = tk.Button(root, text='ADD TASK', font=('Arial', 12), bg='#F1F0E8', command=add_item)
clear_button = tk.Button(root, text='CLEAR', font=('Arial', 12), bg='#F1F0E8', command=clear_item)
submit_button= tk.Button(root, text='TO DB', font=('Arial',12), bg='#F1F0E8', command=submit)
query_button= tk.Button(root, text='SHOW RECORDS', font=('Arial',12), bg='#F1F0E8', command=query)

add_button.pack(side='top')
delete_button.pack(side='top')
clear_button.pack(side='top')
submit_button.pack(side='top')
query_button.pack(side='top')






conn.commit()
conn.close()




root.mainloop()




import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

#Initialize the sqlite database
conn=sqlite3.connect('todo_list.db')
#create cursor
cursor=conn.cursor()
cursor.execute('''CREATE TABLE tasks(
id INTEGER PRIMARY KEY,
        task_name text,
        deadline DATE)
''')
#commit changes to our db
conn.commit()

# Print the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

script_directory = os.path.dirname(os.path.abspath(__file__))

print("Script directory:", script_directory)




window = tk.Tk()
window.geometry('600x400')
window.title('before-tomorrow')
window.configure(bg='#EEE0C9')
window.resizable(True,True)
label = tk.Label(window, text='My To-Do List', font=('Castellar', 20))
label.pack(pady=20)

my_frame = tk.Frame(window)
my_frame.pack(pady=10)

my_entry_label = tk.Label(my_frame, text='Enter Task:', font=('Arial', 12))
my_entry_label.grid(row=0, column=0, padx=12, pady=5)

date_entry_label = tk.Label(my_frame, text='Deadline:', font=('Arial', 12))
date_entry_label.grid(row=1, column=0, padx=12, pady=5)

my_entry = tk.Entry(my_frame, font=('Times New Roman', 15), width=25)
my_entry.grid(row=0, column=1, padx=12, pady=5)

date_entry = tk.Entry(my_frame, font=('Times New Roman', 15), width=25)
date_entry.grid(row=1, column=1, padx=12, pady=5)

my_list = tk.Listbox(window, font=('Times New Roman', 15),
                    height=5, width=80, bg='#FFFAF4', bd=0,
                    fg='#000000', highlightthickness=0,
                    selectbackground="#73777B", activestyle='none')
my_list.pack(fill='both', padx=20, pady=10)

# Add tasks to the list with deadline dates
tasks = []
for item in tasks:
    my_list.insert('end', item)

def delete_item():
    selected_item = my_list.curselection()
    if selected_item:
        task_id =  selected_item[0] + 1  #index to adjust in db
        my_list.delete(selected_item)
        delete_task_from_db(task_id)
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
        add_to_database(task,deadline)
    else:
        messagebox.showwarning('Warning', 'Please enter a task.')

#function to add tasks to database
def add_to_database(tasks,Deadline):
    cursor.execute('''
          INSERT INTO tasks(tasks, deadline,status)
          VALUE(?,?,?)
          ''', (tasks, Deadline, 'not done'))
    conn.commit()

#FUNCTION TO FETCH DATA FROM THE DATABASE
def fetch_task_from_db():
    cursor.execute('SELECT * FROM tasks')
    tasks=cursor.fetchall()
    return tasks

#function to update tasks in the database
def update_task_to_db(task_id):
    cursor.execute('''
    UPDATE task
    SET status=?
    WHERE id=?
    ''',('Complete', task_id))
    conn.commit()

# Function to delete a task from the database
def delete_task_from_db(task_id):
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()

def clear_item():
    confirmed = messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all tasks?")
    if confirmed:
        my_list.delete(0, 'end')
    clear_from_db()

#finction deleting all from db
def clear_from_db():
    cursor.execute('DELETE FROM tasks')
    conn.commit()






delete_button = tk.Button(window, text='DEL TASK', font=('Arial', 12), bg='#F1F0E8', command=delete_item)
add_button = tk.Button(window, text='ADD TASK', font=('Arial', 12), bg='#F1F0E8', command=add_item)
clear_button = tk.Button(window, text='CLEAR', font=('Arial', 12), bg='#F1F0E8', command=clear_item)

add_button.pack(side='top')
delete_button.pack(side='top' )
clear_button.pack(side='top')

conn.close()  # Close the database connection when GUI is closed





window.mainloop()





import tkinter as tk
from tkinter import messagebox
import _sqlite3

root = tk.Tk()
root.geometry('600x400')
root.title('before-tomorrow')
root.configure(bg='#EEE0C9')
root.resizable(True,True)

conn=_sqlite3.connect('todo_list.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
id INTEGER PRIMARY KEY,
        task_name TEXT,
        due_date DATE,
        status TEXT)
''')
conn.commit()


label = tk.Label(root, text='My To-Do List', font=('Castellar', 19))
label.pack(pady=20)

my_frame = tk.Frame(root)
my_frame.pack(pady=10)

my_entry_label = tk.Label(my_frame, text='Enter Task:', font=('Arial', 12))
my_entry_label.grid(row=0, column=0, padx=12, pady=5)

date_entry_label = tk.Label(my_frame, text='Deadline:', font=('Arial', 12))
date_entry_label.grid(row=1, column=0, padx=12, pady=5)

my_entry = tk.Entry(my_frame, font=('Times New Roman', 15), width=25)
my_entry.grid(row=0, column=1, padx=12, pady=5)

date_entry = tk.Entry(my_frame, font=('Times New Roman', 15), width=25)
date_entry.grid(row=1, column=1, padx=12, pady=5)

my_list = tk.Listbox(root, font=('Times New Roman', 15),
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
        cursor.execute("DELETE FROM tasks WHERE task_name=?", (tasks,))
        conn.commit()
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
        add_to_database(tasks,deadline)

    else:
        messagebox.showwarning('Warning', 'Please enter a task.')

#function to add tasks to database
def add_to_database(tasks,Deadline):
    cursor.execute('''
          INSERT INTO tasks(tasks, deadline,status)
          VALUE(?,?,?)
          ''', (tasks, Deadline, 'not done'))
    conn.commit()

def saveList():
    cursor.execute("DELETE FROM tasks")
    for task in my_list.get(0,tk.END):
        cursor.execute("INSERT INTO tasks (task_name) VALUES (?)", (task,))
        conn.commit()

    my_list.delete(0, tk.END)
    grabAll()


def clear_item():
    confirmed = messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all tasks?")
    if confirmed:
        my_list.delete(0, 'end')




delete_button = tk.Button(root, text='DEL TASK', font=('Arial', 12), bg='#F1F0E8', command=delete_item)
add_button = tk.Button(root, text='ADD TASK', font=('Arial', 12), bg='#F1F0E8', command=add_item)
clear_button = tk.Button(root, text='CLEAR', font=('Arial', 12), bg='#F1F0E8', command=clear_item)
save_button = tk.Button(root, text='save', font=('Arial', 12), bg='#F1F0E8', command=saveList)

add_button.pack(side='top')
delete_button.pack(side='top' )
clear_button.pack(side='top')
save_button.pack(side='top')

# Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)


def on_closing():
    saveList()
    conn.close()  # Close the database connection when GUI is closed
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

def grabAll():
    cursor.execute("SELECT task_name FROM tasks")
    fetched_tasks= cursor.fetchall()
    for task in fetched_tasks:
        my_list.insert(tk.END, task[0])

grabAll()
root.mainloop()


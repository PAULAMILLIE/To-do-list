import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('600x600')
window.title('before-tomorrow')
window.configure(bg='#EEE0C9')
window.resizable(True,True)
label = tk.Label(window, text='My To-Do List', font=('Forte', 20))
label.pack(pady=20)

my_frame = tk.Frame(window)
my_frame.pack(pady=10)

my_entry_label = tk.Label(my_frame, text='Enter Task:', font=('Consolas', 12))
my_entry_label.grid(row=0, column=0, padx=12, pady=5)

date_entry_label = tk.Label(my_frame, text='Deadline:', font=('Consolas', 12))
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
        my_list.delete(selected_item)
    else:
        messagebox.showwarning('Warning', 'No selected item')

def add_item():
    task = my_entry.get()
    if task:
        deadline = date_entry.get()
        task_with_deadline = f"{task} (Deadline: {deadline})"
        my_list.insert('end', task_with_deadline)
        my_entry.delete(0, 'end')
        date_entry.delete(0, 'end')
    else:
        messagebox.showwarning('Warning', 'Please enter a task.')

def clear_item():
    confirmed = messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all tasks?")
    if confirmed:
        my_list.delete(0, 'end')
        with open("tasks.txt", "w") as file:
            pass



delete_button = tk.Button(window, text='DEL TASK', font=('Arial', 12), bg='#ED7B7B', command=delete_item)
add_button = tk.Button(window, text='ADD TASK', font=('Arial', 12), bg='#F1F0E8', command=add_item)
clear_button = tk.Button(window, text='CLEAR', font=('Arial', 12), bg='#F1F0E8', command=clear_item)

add_button.pack(side='top')
clear_button.pack(side='top')
delete_button.pack(side='top' )

window.mainloop()

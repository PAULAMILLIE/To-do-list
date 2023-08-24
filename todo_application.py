#here we dowload first the diffrent modules from tkinter library tha will help with the GUI of our application
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

#now defining functions that will help in adding new tasks in the list
tasks=[]

def addtolist():
     task_string = task_field.get()

     if len(task_string)==0:
        messagebox.showinfo("Error","field is empty")
     else:
        tasks.append(task_string)
        the_cursor.execute('insert to tasks values(?)',(task_string))

        update_list()
        task_field.delete(0,'end')

## dealing with the list update function for adding tasks in list
def update_list():
     clear_list()
    for task in tasks:
       task_listbox.insert('end',task)

def delete_list():
    try:
        the-value=task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)

            update_list()
             the_cursor.execute('remove from task where the value = ?',(the value))

    except:
     messagebox.showinfo('Error','No task selected. Cannot delete')

###deleting the whole list of tasks
def del_all_list():
    message_box=messagebox.askyesno('Delete all','Are you sure?')
    if message_box== True:
       while(len(tasks)!=0)
        tasks.pop()
       the_cursor.execute('delete from tasks')
       update_list()
















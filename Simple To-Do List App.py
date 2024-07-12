#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox, simpledialog

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def edit(self, new_description):
        self.description = new_description

tasks = []

def add_task(description):
    task = Task(description)
    tasks.append(task)
    refresh_task_list()

def edit_task(index, new_description):
    if 0 <= index < len(tasks):
        tasks[index].edit(new_description)
        refresh_task_list()

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index].mark_completed()
        refresh_task_list()

def delete_completed_tasks():
    global tasks
    tasks = [task for task in tasks if not task.completed]
    refresh_task_list()

def refresh_task_list():
    for widget in task_frame.winfo_children():
        widget.destroy()
    for i, task in enumerate(tasks):
        status = "✓" if task.completed else "✗"
        task_label = tk.Label(task_frame, text=f"{i}. [{status}] {task.description}")
        task_label.pack()

def add_task_gui():
    description = simpledialog.askstring("Add Task", "Enter the task description:")
    if description:
        add_task(description)

def edit_task_gui():
    index = simpledialog.askinteger("Edit Task", "Enter the task number to edit:")
    if index is not None and 0 <= index < len(tasks):
        new_description = simpledialog.askstring("Edit Task", "Enter the new task description:")
        if new_description:
            edit_task(index, new_description)
    else:
        messagebox.showerror("Error", "Invalid task number")

def complete_task_gui():
    index = simpledialog.askinteger("Complete Task", "Enter the task number to mark as completed:")
    if index is not None and 0 <= index < len(tasks):
        complete_task(index)
    else:
        messagebox.showerror("Error", "Invalid task number")

def delete_completed_tasks_gui():
    delete_completed_tasks()

app = tk.Tk()
app.title("To-Do List")

menu_frame = tk.Frame(app)
menu_frame.pack(pady=10)

task_frame = tk.Frame(app)
task_frame.pack(pady=10)

add_button = tk.Button(menu_frame, text="Add Task", command=add_task_gui)
edit_button = tk.Button(menu_frame, text="Edit Task", command=edit_task_gui)
complete_button = tk.Button(menu_frame, text="Complete Task", command=complete_task_gui)
delete_button = tk.Button(menu_frame, text="Delete Completed Tasks", command=delete_completed_tasks_gui)

add_button.grid(row=0, column=0, padx=5)
edit_button.grid(row=0, column=1, padx=5)
complete_button.grid(row=0, column=2, padx=5)
delete_button.grid(row=0, column=3, padx=5)

refresh_task_list()

app.mainloop()


# In[ ]:





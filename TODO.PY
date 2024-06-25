import tkinter as tk
from tkinter import messagebox, simpledialog

class TODOGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do list")
        
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, height=18, width=60, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.listbox.bind("<Double-Button-1>", self.update_task)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.task_entry = tk.Entry(root, width = 50)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", width=50, command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", width=50, command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning(" Task should be entered ")
        
    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
        except:
            messagebox.showwarning(" Task needs to be deleted/erased ")
    
    def update_task(self, event):
        try:
            selected_task_index = self.listbox.curselection()[0]
            old_task = self.tasks[selected_task_index]
            new_task = simpledialog.askstring("Update Task", "Edit Task:", initialvalue=old_task)
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, new_task)
        except:
            messagebox.showwarning(" New task must be selected to update ")

if __name__ == "__main__":
    root = tk.Tk()
    app = TODOGUI(root)
    root.mainloop()


import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List Application")
        self.master.geometry("400x400")
        self.master.configure(bg="#424242")

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.master, bg="#424242")
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame, width=50, height=10, bd=0, selectmode=tk.SINGLE,
            font=("Verdana", 12), bg="#616161", fg="#ffffff",
            selectbackground="#757575", selectforeground="#ffffff"
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(self.master, width=50, font=("Verdana", 12), bg="#757575", fg="#ffffff")
        self.entry.pack(pady=10)

        self.add_button = tk.Button(
            self.master, text="Add Task", command=self.add_task, 
            bg="#00bcd4", fg="#ffffff", font=("Verdana", 12), bd=0, 
            activebackground="#0097a7"
        )
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(
            self.master, text="Delete Task", command=self.delete_task, 
            bg="#e91e63", fg="#ffffff", font=("Verdana", 12), bd=0, 
            activebackground="#c2185b"
        )
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(
            self.master, text="Clear All Tasks", command=self.clear_tasks, 
            bg="#ff9800", fg="#ffffff", font=("Verdana", 12), bd=0, 
            activebackground="#f57c00"
        )
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_tasks(self):
        self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

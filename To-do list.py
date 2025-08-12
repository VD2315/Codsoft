import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg="#f7f7f7")

        self.tasks = []

        self.title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#f7f7f7", fg="#333")
        self.title_label.pack(pady=10)

        self.frame = tk.Frame(root, bg="#f7f7f7")
        self.frame.pack(pady=5)

        self.task_entry = tk.Entry(self.frame, font=("Helvetica", 14), width=22, bd=2, relief="groove")
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_button = tk.Button(self.frame, text="Add Task", font=("Helvetica", 12), bg="#4CAF50", fg="white",
                                    relief="flat", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5)

        self.listbox = tk.Listbox(root, font=("Helvetica", 14), width=30, height=15, bd=2, relief="groove",
                                  selectbackground="#FFB347", activestyle="none")
        self.listbox.pack(pady=10)

        self.button_frame = tk.Frame(root, bg="#f7f7f7")
        self.button_frame.pack()

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", font=("Helvetica", 12), bg="#E53935",
                                       fg="white", relief="flat", command=self.delete_task)
        self.delete_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(self.button_frame, text="Mark Complete", font=("Helvetica", 12),
                                         bg="#1E88E5", fg="white", relief="flat", command=self.mark_complete)
        self.complete_button.grid(row=0, column=1, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_complete(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.tasks[selected_index] = f"✔ {self.tasks[selected_index]}"
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

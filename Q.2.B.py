import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def insert(self, item, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Invalid Position")
        self.items.insert(position, item)

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid Position")
        return self.items.pop(position)

    def peek(self):
        if not self.items:
            raise IndexError("Stack is Empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def traverse(self):
        if self.is_empty():
            return "Stack is Empty"
        return " <- ".join(self.items)


class StackGUI:
    def __init__(self, root):
        self.stack = Stack()

        root.title("Stack Operations")
        root.geometry("500x550")
        root.configure(bg="lightblue")

        tk.Label(root, text="STACK OPERATIONS",
                 font=("Arial", 18, "bold"),
                 bg="lightblue", fg="darkblue").pack(pady=10)

        tk.Label(root, text="Item", bg="lightblue",
                 font=("Arial", 12)).pack()
        self.item_entry = tk.Entry(root, font=("Arial", 12))
        self.item_entry.pack(pady=5)

        tk.Label(root, text="Position (0-based)", bg="lightblue",
                 font=("Arial", 12)).pack()
        self.position_entry = tk.Entry(root, font=("Arial", 12))
        self.position_entry.pack(pady=5)

        tk.Button(root, text="Insert", width=20,
                  bg="green", fg="white",
                  command=self.insert).pack(pady=5)

        tk.Button(root, text="Delete", width=20,
                  bg="red", fg="white",
                  command=self.delete).pack(pady=5)

        tk.Button(root, text="Peek", width=20,
                  bg="orange",
                  command=self.peek).pack(pady=5)

        tk.Button(root, text="Is Empty?", width=20,
                  bg="purple", fg="white",
                  command=self.is_empty).pack(pady=5)

        tk.Button(root, text="Stack Size", width=20,
                  bg="blue", fg="white",
                  command=self.size).pack(pady=5)

        tk.Button(root, text="Traverse", width=20,
                  bg="brown", fg="white",
                  command=self.traverse).pack(pady=5)

        tk.Label(root, text="Current Stack",
                 bg="lightblue",
                 font=("Arial", 14, "bold")).pack(pady=10)

        self.listbox = tk.Listbox(root, width=35, height=10,
                                  font=("Arial", 12))
        self.listbox.pack()

    def update_stack(self):
        self.listbox.delete(0, tk.END)
        for item in reversed(self.stack.items):
            self.listbox.insert(tk.END, item)

    def insert(self):
        item = self.item_entry.get()
        pos = self.position_entry.get()

        if item == "" or pos == "":
            messagebox.showwarning("Warning", "Enter Item and Position")
            return

        try:
            self.stack.insert(item, int(pos))
            self.update_stack()
            self.item_entry.delete(0, tk.END)
            self.position_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Item Inserted Successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete(self):
        pos = self.position_entry.get()

        if pos == "":
            messagebox.showwarning("Warning", "Enter Position")
            return

        try:
            item = self.stack.delete(int(pos))
            self.update_stack()
            self.position_entry.delete(0, tk.END)
            messagebox.showinfo("Deleted", f"{item} Deleted Successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def peek(self):
        try:
            messagebox.showinfo("Top Item", self.stack.peek())
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def is_empty(self):
        if self.stack.is_empty():
            messagebox.showinfo("Stack", "Stack is Empty")
        else:
            messagebox.showinfo("Stack", "Stack is Not Empty")

    def size(self):
        messagebox.showinfo("Size", f"Stack Size = {self.stack.size()}")

    def traverse(self):
        messagebox.showinfo("Stack Contents", self.stack.traverse())


root = tk.Tk()
app = StackGUI(root)
root.mainloop()

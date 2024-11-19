import tkinter as tk

class Breadcrumb(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.path_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.path_label.pack(side=tk.LEFT)

    def update_path(self, path):
        self.path_label.config(text=path)

def navigate_to(section):
    breadcrumb.update_path(section)

def create_gui():
    global breadcrumb
    root = tk.Tk()
    root.geometry("400x200")
    breadcrumb = Breadcrumb(root, bg="lightgray", height=30)
    breadcrumb.pack(fill=tk.X)

    # Example buttons to simulate navigation
    button1 = tk.Button(root, text="Section 1", command=lambda: navigate_to("Section 1"))
    button2 = tk.Button(root, text="Section 2", command=lambda: navigate_to("Section 2"))
    button3 = tk.Button(root, text="Section 3", command=lambda: navigate_to("Section 3"))

    button1.pack()
    button2.pack()
    button3.pack()

    root.mainloop()

# Call the function to create the GUI
create_gui()
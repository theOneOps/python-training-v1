import string
from tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry

def quitWindow(window):
    window.destroy()

def add_value():
    value = InviteesEntry.get()
    if value:
        text_widget.insert(tk.END, value + "\n")
        InviteesEntry.delete(0, tk.END)

def remove_selected():
    selected_index = text_widget.index(tk.SEL_FIRST)
    if not(selected_index):
        return
    if selected_index:
        text_widget.delete(selected_index, tk.SEL_LAST)

def on_click(event):
    remove_selected()

def on_date_change():
    selected_date = cal.get_date()
    entry_date_var.set(selected_date)

def on_time_change(*args):
    selected_time = f"{hour_var.get()}:{minute_var.get()} {ampm_var.get()}"
    entry_time_var.set(selected_time)


class AppTab(tk.Frame):
    def __init__(self, master=None, title="Tab", **kwargs):
        super().__init__(master, **kwargs)
        self.title = title
        self.label = tk.Label(self, text=f"Content for {title}", font=("Helvetica", 12))
        self.label.pack(padx=10, pady=10)


def createFstWindow():
    rootwindow = tk.Tk()
    rootwindow.geometry("300x500")

    # Create a notebook (tabbed interface)
    notebook = ttk.Notebook(rootwindow)
    notebook.pack(expand=True, fill=tk.BOTH)

    # Create tabs for details, food, locations, and invitees
    tab_details = AppTab(notebook, title="Details")
    tab_food = AppTab(notebook, title="Food")
    tab_locations = AppTab(notebook, title="Locations")
    tab_invitees = AppTab(notebook, title="Invitees")
    tabReservations = AppTab(notebook, title="Reservations")

    # Add tabs to the notebook
    notebook.add(tab_details, text="Details")
    notebook.add(tab_food, text="Food")
    notebook.add(tab_locations, text="Locations")
    notebook.add(tab_invitees, text="Invitees")

    # menu part start
    # Menu belongs to menubar created below
    menubar = tk.Menu(rootwindow)
    rootwindow.config(menu=menubar)

    # Create a new frame for the menu options
    menuFrame = tk.Menu(menubar, tearoff=0)

    menubar.add_command(label="Profil")
    menubar.add_command(label="Deconnect", command=lambda: quitWindow(rootwindow))
    menubar.add_cascade(label="Reservation", menu=menuFrame)

    menuFrame.add_command(label="Details")
    menuFrame.add_command(label="Food", command=lambda: notebook.select(tab_food))
    menuFrame.add_command(label="Locations", command=lambda: notebook.select(tab_locations))
    menuFrame.add_command(label="Invitees", command=lambda: notebook.select(tab_invitees))
    # menu part end

    # Update AppTab to hold other widgets instead of just a label
    tab_details.label.destroy()

    # Create a frame to hold the details reservation details
    # label_details = tk.Label(tab_details, text="Details Frame Content", font=("Helvetica", 12))
    label_details = tk.Label(tab_details, text="Details Section", font=("Helvetica", 12))
    label_details.pack(padx=10, pady=10)
    DetailsFrame = tk.Frame(tab_details)
    DetailsFrame.pack(fill=tk.X) # very important this part...
    TypeEventFrame = tk.Frame(DetailsFrame)
    NameFrame = tk.Frame(DetailsFrame)

    NameFrame.grid(row=0, column=0)
    TypeEventFrame.grid(row=1, column=0)

    TypeEventLabel = tk.Label(TypeEventFrame, text="Type of Event")
    NameLabel = tk.Label(NameFrame, text="Name")
    TypeEventEntry = tk.Entry(TypeEventFrame, width=30)
    NameEntry = tk.Entry(NameFrame, width=30)

    TypeEventLabel.grid(row=0, column=0)
    TypeEventEntry.grid(row=0, column=1)

    NameLabel.grid(row=0, column=0)
    NameEntry.grid(row=0, column=1)

    ButtonNext = tk.Button(DetailsFrame, text="Next", command=lambda: notebook.select(tab_food))

    ButtonNext.grid(row=2, column=1)

    tab_food.label.destroy()
    label_food = tk.Label(tab_food, text="Food Frame Content", font=("Helvetica", 12))
    label_food.pack(padx=10, pady=10)

    tab_locations.label.destroy()
    label_locations = tk.Label(tab_locations, text="Locations Section", font=("Helvetica", 12))
    label_locations.pack(padx=10, pady=10)

    # Create a frame to hold the reservation date & locations

    Date_locationsFrame = tk.Frame(tab_locations)
    Date_locationsFrame.pack(fill=tk.X)  # very important this part...
    LocationLabel = tk.Label(Date_locationsFrame, text="Location")
    DateLabel = tk.Label(Date_locationsFrame, text="Choose your date")
    LocationEntry = tk.Entry(Date_locationsFrame, textvariable=string, width=30)

    # Create a DateEntry widget
    global cal
    cal = DateEntry(Date_locationsFrame, width=12, background='darkblue', foreground='white', borderwidth=2,
                    date_pattern='yyyy-mm-dd')
    cal.grid(row=0, column=0, padx=10, pady=10)

    # Create an Entry widget to display the selected date
    global entry_date_var
    entry_date_var = tk.StringVar()
    entry_date = tk.Entry(Date_locationsFrame, textvariable=entry_date_var, state='readonly')
    entry_date.grid(row=1, column=0, padx=10, pady=10)

    # Link the calendar to the entry widget
    cal.bind("<<DateEntrySelected>>", lambda event: on_date_change())

    # Create Spinboxes for time selection
    global hour_var, minute_var, ampm_var
    hour_var = tk.StringVar()
    minute_var = tk.StringVar()
    ampm_var = tk.StringVar()

    hour_spinbox = tk.Spinbox(Date_locationsFrame, from_=1, to=12, width=2, textvariable=hour_var, command=on_time_change)
    minute_spinbox = tk.Spinbox(Date_locationsFrame, from_=0, to=59, width=2, textvariable=minute_var,
                                command=on_time_change)
    ampm_spinbox = tk.Spinbox(Date_locationsFrame, values=("AM", "PM"), width=3, textvariable=ampm_var,
                              command=on_time_change)

    hour_spinbox.grid(row=0, column=1, padx=10, pady=10)
    minute_spinbox.grid(row=0, column=2, padx=10, pady=10)
    ampm_spinbox.grid(row=0, column=3, padx=10, pady=10)

    # Create an Entry widget to display the selected time
    global entry_time_var
    entry_time_var = tk.StringVar()
    entry_time = tk.Entry(Date_locationsFrame, textvariable=entry_time_var, state='readonly')
    entry_time.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

    BtnNextinviteForLoc = tk.Button(Date_locationsFrame, text="Next", command=lambda: notebook.select(tab_invitees))
    BtnNextinviteForLoc.grid(row=2, column=3)
    BtnPrevinviteForLoc = tk.Button(Date_locationsFrame, text="Previous", command=lambda: notebook.select(tab_food))
    BtnPrevinviteForLoc.grid(row=2, column=0)

    # Create a frame to hold the reservation invitees

    tab_invitees.label.destroy()
    label_invitees = tk.Label(tab_invitees, text="Who will join you ? ", font=("Helvetica", 12))
    label_invitees.pack(padx=10, pady=10)

    global text_widget
    global InviteesEntry

    # Create a frame to hold the reservation invitees
    Invitees_Frame = tk.Frame(tab_invitees)
    Invitees_Frame.pack(fill=tk.X)  # very important this part...
    InviteesEntry = tk.Entry(Invitees_Frame, textvariable=string, width=30)
    InviteesEntry.pack(pady=10)

    # Button to add value
    add_button = tk.Button(Invitees_Frame, text="Add", command=add_value)
    add_button.pack()

    # Text widget to display entered values
    text_widget = tk.Text(Invitees_Frame, height=10, width=30)
    text_widget.pack(pady=10)

    # Button to remove selected value
    remove_button = tk.Button(Invitees_Frame, text="Remove Selected", command=remove_selected)
    remove_button.pack(pady=20)

    # Bind the click event to remove_selected function
    text_widget.bind("<ButtonRelease-1>", on_click)

    BtnPrevLocForInvite = tk.Button(Invitees_Frame, text="Back", command=lambda: notebook.select(tab_locations))
    BtnPrevLocForInvite.pack(pady=10)

    rootwindow.mainloop()

# Call the function to create the window
createFstWindow()

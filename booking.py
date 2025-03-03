from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
def db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="travels"
    )
user_id = None
def login_window():
    global user_id
    w = Tk()
    w.title("Login")
    w.geometry("1000x500")
    w.configure(bg="#E3F2FD")
    Label(w, text="Skyline Travels", font=("Arial", 20, "bold"), fg="#0D47A1", bg="#E3F2FD").pack(pady=20)
    frame = Frame(w, bg="#1565C0", padx=20, pady=20)
    frame.pack(pady=30)
    Label(frame, text="Login", font=("Arial", 18, "bold"), fg="white", bg="#1565C0").pack(pady=10)
    Label(frame, text="Username", fg="white", bg="#1565C0", font=("Arial", 12)).pack()
    entry_user = Entry(frame, width=30)
    entry_user.pack(pady=5)
    Label(frame, text="Password", fg="white", bg="#1565C0", font=("Arial", 12)).pack()
    entry_pass = Entry(frame, width=30, show="*")
    entry_pass.pack(pady=5)
    def login():
        global user_id
        conn = db()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s",
                       (entry_user.get(), entry_pass.get()))
        user = cursor.fetchone()
        conn.close()
        if user:
            user_id = user[0]
            messagebox.showinfo("Success", "Login Successful!")
            w.destroy()
            home_window()
        else:
            messagebox.showerror("Error", "Invalid credentials!")
    Button(frame, text="Login", command=login, bg="#64B5F6", fg="white", font=("Arial", 12, "bold"), padx=10,
           pady=5).pack(pady=10)
    def open_signup():
        w.destroy()
        signup_window()
    Label(w, text="Don't have an account?", bg="#E3F2FD", font=("Arial", 10)).pack()
    Button(w, text="Signup", command=open_signup, fg="#0D47A1", font=("Arial", 10, "bold"), relief=FLAT).pack()
    w.mainloop()
def signup_window():
    w = Tk()
    w.title("Signup")
    w.geometry("1000x500")
    w.configure(bg="#E3F2FD")
    Label(w, text="Skyline Travels", font=("Arial", 20, "bold"), fg="#0D47A1", bg="#E3F2FD").pack(pady=20)
    frame = Frame(w, bg="#1565C0", padx=20, pady=20)
    frame.pack(pady=30)
    Label(frame, text="Signup", font=("Arial", 18, "bold"), fg="white", bg="#1565C0").pack(pady=10)
    Label(frame, text="Username", fg="white", bg="#1565C0", font=("Arial", 12)).pack()
    entry_user = Entry(frame, width=30)
    entry_user.pack(pady=5)
    Label(frame, text="Password", fg="white", bg="#1565C0", font=("Arial", 12)).pack()
    entry_pass = Entry(frame, width=30, show="*")
    entry_pass.pack(pady=5)
    def signup():
        conn = db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                           (entry_user.get(), entry_pass.get()))
            conn.commit()
            messagebox.showinfo("Success", "Signup Successful! Please Login.")
            w.destroy()
            login_window()
        except:
            messagebox.showerror("Error", "Username already exists!")
        finally:
            conn.close()
    Button(frame, text="Signup", command=signup, bg="#64B5F6", fg="white", font=("Arial", 12, "bold"), padx=10,
           pady=5).pack(pady=10)
    w.mainloop()
def home_window():
    w = Tk()
    w.title("Skyline Travels - Home")
    w.geometry("1000x500")
    w.configure(bg="#87CEEB")
    Label(w, text="Skyline Travels", font=("Arial", 20, "bold"), fg="#0D47A1", bg="#87CEEB").pack(pady=10)
    Label(w, text="Your Trusted Travel Partner", font=("Arial", 18, "bold"), fg="black", bg="#87CEEB").pack()
    Label(w,
          text="Explore the beauty of new destinations with comfort and reliability.\nWe ensure a seamless travel experience with top-notch service.",
          font=("Arial", 18), fg="black", bg="#87CEEB").pack(pady=10)
    frame = Frame(w, bg="#1565C0", padx=20, pady=20)
    frame.pack(pady=20)
    Button(frame, text="Book Tickets", command=bookticket, bg="#64B5F6", fg="white", font=("Arial", 12, "bold"),
           padx=10, pady=5).pack(pady=5, fill=X)
    Button(frame, text="View Tickets", command=viewtickets, bg="#64B5F6", fg="white",
           font=("Arial", 12, "bold"), padx=10, pady=5).pack(pady=5, fill=X)
    Button(frame, text="Modify Ticket", command=modifyticket, bg="#64B5F6", fg="white",
           font=("Arial", 12, "bold"), padx=10, pady=5).pack(pady=5, fill=X)
    Button(frame, text="Delete Ticket", command=deleteticket, bg="#FF3D00", fg="white",
           font=("Arial", 12, "bold"), padx=10, pady=5).pack(pady=5, fill=X)
    w.mainloop()
tn = ["Chennai", "Madurai", "Theni"]
fc = {
    ("Chennai", "Madurai"): 1300,
    ("Chennai", "Theni"): 1500,
    ("Theni", "Chennai"): 1500,
    ("Madurai", "Chennai"): 1300,
}
def calculate_fare(source, destination):
    if source == destination:
        return 0
    return fc.get((source, destination)) or fc.get((destination, source), 1200)
def bookticket():
    global user_id
    w = Tk()
    w.title("Book Ticket")
    w.geometry("1000x500")
    w.configure(bg="#E3F2FD")
    frame = Frame(w, bg="#1565C0", padx=20, pady=20)
    frame.pack(pady=20)
    Label(frame, text="Book Your Ticket", font=("Arial", 14, "bold"), fg="white", bg="#1565C0").pack(pady=10)
    Label(frame, text="Name", fg="white", bg="#1565C0").pack()
    entry_name = Entry(frame, width=30)
    entry_name.pack(pady=5)
    Label(frame, text="Age", fg="white", bg="#1565C0").pack()
    entry_age = Entry(frame, width=30)
    entry_age.pack(pady=5)
    Label(frame, text="Sex", fg="white", bg="#1565C0").pack()
    entry_sex = ttk.Combobox(frame, values=["Male", "Female", "Other"], width=27)
    entry_sex.pack(pady=5)
    Label(frame, text="Source", fg="white", bg="#1565C0").pack()
    entry_source = ttk.Combobox(frame, values=tn, width=27)
    entry_source.pack(pady=5)
    Label(frame, text="Destination", fg="white", bg="#1565C0").pack()
    entry_dest = ttk.Combobox(frame, values=tn, width=27)
    entry_dest.pack(pady=5)
    Label(frame, text="Fare", fg="white", bg="#1565C0").pack()
    entry_fare = Entry(frame, width=30, state="readonly")
    entry_fare.pack(pady=5)
    def update_fare(*args):
        source = entry_source.get()
        destination = entry_dest.get()
        if source and destination:
            fare = calculate_fare(source, destination)
            entry_fare.config(state="normal")
            entry_fare.delete(0, END)
            entry_fare.insert(0, str(fare))
            entry_fare.config(state="readonly")
    entry_source.bind("<<ComboboxSelected>>", update_fare)
    entry_dest.bind("<<ComboboxSelected>>", update_fare)
    def book_ticket():
        if user_id is None:
            messagebox.showerror("Error", "User not logged in!")
            return
        conn = db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tickets (user_id, name, age, sex, source, destination, fare) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (
            user_id, entry_name.get(), entry_age.get(), entry_sex.get(), entry_source.get(), entry_dest.get(),
            entry_fare.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Ticket Booked!")
        w.destroy()
    Button(frame, text="Book", command=book_ticket, bg="#64B5F6", fg="white", font=("Arial", 12, "bold"), padx=10,
           pady=5).pack(pady=10)
    w.mainloop()
def viewtickets():
    global user_id
    if user_id is None:
        messagebox.showerror("Error", "User not logged in!")
        return
    w = Tk()
    w.title("Your Tickets")
    w.geometry("1000x500")
    w.configure(bg="#E3F2FD")
    frame = Frame(w, bg="#1565C0", padx=20, pady=20)
    frame.pack(pady=20)
    Label(frame, text="Your Tickets", font=("Arial", 16, "bold"), fg="white", bg="#1565C0").pack(pady=10)
    conn = db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, sex, source, destination, fare FROM tickets WHERE user_id=%s",
                   (user_id,))
    tickets = cursor.fetchall()
    conn.close()
    if not tickets:
        Label(frame, text="No tickets found!", fg="white", bg="#1565C0", font=("Arial", 12)).pack(pady=5)
    else:
        for ticket in tickets:
            ticket_frame = Frame(frame, bg="#FFFFFF", padx=10, pady=10, relief=RAISED, borderwidth=3)
            ticket_frame.pack(pady=10, fill=X)
            Label(ticket_frame, text=f"Ticket ID: {ticket[0]}", font=("Arial", 12, "bold"), fg="#1565C0",
                  bg="#FFFFFF").pack(anchor=W)
            Label(ticket_frame, text=f"Passenger: {ticket[1]}, Age: {ticket[2]}, Sex: {ticket[3]}", font=("Arial", 10),
                  fg="#000000", bg="#FFFFFF").pack(anchor=W)
            Label(ticket_frame, text=f"From: {ticket[4]}  ➝  To: {ticket[5]}", font=("Arial", 10, "bold"), fg="#1565C0",
                  bg="#FFFFFF").pack(anchor=W)
            Label(ticket_frame, text=f"Fare: ₹{ticket[6]}", font=("Arial", 10, "bold"), fg="green", bg="#FFFFFF").pack(
                anchor=W)
    w.mainloop()
def modifyticket():
    global user_id
    if user_id is None:
        messagebox.showerror("Error", "User not logged in!")
        return
    w = Tk()
    w.title("Modify Ticket")
    w.geometry("1000x500")
    w.configure(bg="#E3F2FD")
    frame = Frame(w, bg="#1565C0", padx=20, pady=20)
    frame.pack(pady=20)
    Label(frame, text="Modify Your Ticket", font=("Arial", 14, "bold"), fg="white", bg="#1565C0").pack(pady=10)
    Label(frame, text="New Destination", fg="white", bg="#1565C0").pack()
    entry_dest = ttk.Combobox(frame, values=["Chennai", "Madurai", "Theni"], width=27)
    entry_dest.pack(pady=5)
    Label(frame, text="Fare", fg="white", bg="#1565C0").pack()
    entry_fare = Entry(frame, width=30, state="readonly")
    entry_fare.pack(pady=5)
    def update_fare(*args):
        destination = entry_dest.get()
        source = "Chennai"
        fare = fc.get((source, destination)) or fc.get((destination, source), 1200)
        entry_fare.config(state="normal")
        entry_fare.delete(0, END)
        entry_fare.insert(0, str(fare))
        entry_fare.config(state="readonly")
    entry_dest.bind("<<ComboboxSelected>>", update_fare)
    def modify_ticket():
        conn = db()
        cursor = conn.cursor()
        cursor.execute("UPDATE tickets SET destination=%s, fare=%s WHERE user_id=%s",
                       (entry_dest.get(), entry_fare.get(), user_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Your tickets have been updated!")
        w.destroy()
    Button(frame, text="Modify", command=modify_ticket, bg="#64B5F6", fg="white", font=("Arial", 12, "bold"), padx=10,
           pady=5).pack(pady=10)
    w.mainloop()
def deleteticket():
    global user_id
    if user_id is None:
        messagebox.showerror("Error", "User not logged in!")
        return
    w = Tk()
    w.title("Delete Ticket")
    w.geometry("1000x500")
    w.configure(bg="#E3F2FD")
    frame = Frame(w, bg="#1565C0", padx=20, pady=20)
    frame.pack(pady=20)
    Label(frame, text="Delete Your Ticket", font=("Arial", 14, "bold"), fg="white", bg="#1565C0").pack(pady=10)
    Label(frame, text="Enter Ticket ID to Delete", fg="white", bg="#1565C0", font=("Arial", 12)).pack(pady=5)
    entry_ticket_id = Entry(frame, width=30)
    entry_ticket_id.pack(pady=5)
    def delete_ticket():
        ticket_id = entry_ticket_id.get()
        if not ticket_id:
            messagebox.showerror("Error", "Please enter a Ticket ID!")
            return
        conn = db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tickets WHERE id=%s AND user_id=%s", (ticket_id, user_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Ticket Deleted Successfully!")
        w.destroy()
    Button(frame, text="Delete", command=delete_ticket, bg="#FF3D00", fg="white", font=("Arial", 12, "bold"), padx=10,
           pady=5).pack(pady=10)
    w.mainloop()
login_window()
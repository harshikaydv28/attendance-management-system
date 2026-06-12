import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
from datetime import datetime
import socket
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("")

    return os.path.join(base_path, relative_path)

ALLOWED_WIFI_IP = "192.168."
ATTENDANCE_FILE = "attendance.txt"


root = tk.Tk()
root.title("Zillionsoftech Attendance System")


root.geometry("1200x700")
root.configure(bg="#f4f6f9")
root.resizable(True, True)


def connected_to_institute_wifi():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        if ip.startswith(ALLOWED_WIFI_IP):
            return True
        return False

    except:
        return False


def save_attendance(student_id, status):
    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")

    with open(ATTENDANCE_FILE, "a") as file:
        file.write(f"{student_id} | {status} | {date} | {time}\n")


def mark_entry():

    student_id = student_entry.get()

    if student_id == "":
        messagebox.showerror("Error", "Please Enter Student ID")
        return

    if not connected_to_institute_wifi():
        messagebox.showerror("WiFi Error", "Connect to Institute WiFi")
        return

    save_attendance(student_id, "ENTRY")

    messagebox.showinfo("Success", "Entry Marked Successfully")

    student_entry.delete(0, tk.END)


def mark_exit():

    student_id = student_entry.get()

    if student_id == "":
        messagebox.showerror("Error", "Please Enter Student ID")
        return

    if not connected_to_institute_wifi():
        messagebox.showerror("WiFi Error", "Connect to Institute WiFi")
        return

    save_attendance(student_id, "EXIT")

    messagebox.showinfo("Success", "Exit Marked Successfully")

    student_entry.delete(0, tk.END)


def view_attendance():

    attendance_box.delete("1.0", tk.END)

    attendance_box.insert(
        tk.END,
        "\n"
        "=====================================\n"
        "     ZILLIONSOFTECH INSTITUTE\n"
        "        ATTENDANCE RECORD\n"
        "=====================================\n\n"
    )

    if not os.path.exists(ATTENDANCE_FILE):
        attendance_box.insert(tk.END, "No attendance records found.")
        return

    with open(ATTENDANCE_FILE, "r") as file:

        data = file.read()

        if data.strip() == "":
            attendance_box.insert(tk.END, "No attendance records found.")
        else:
            attendance_box.insert(tk.END, data)


def update_time():

    now = datetime.now()

    current_time = now.strftime("%B %d, %Y | %I:%M:%S %p")

    date_label.config(text=current_time)

    root.after(1000, update_time)


header = tk.Frame(root, bg="white", height=160)
header.pack(fill="x")


logo_img = Image.open(resource_path("logo.png"))

logo_img = logo_img.resize((130, 130))

logo = ImageTk.PhotoImage(logo_img)

logo_label = tk.Label(
    header,
    image=logo,
    bg="white"
)

logo_label.place(x=30, y=15)

divider = tk.Frame(
    header,
    bg="#d1d5db",
    width=2,
    height=120
)

divider.place(x=210, y=20)

title = tk.Label(
    header,
    text="ZILLIONSOFTECH INSTITUTE",
    font=("Arial", 28, "bold"),
    fg="#002b7f",
    bg="white"
)

title.place(x=250, y=35)

subtitle = tk.Label(
    header,
    text="Smart WiFi Attendance Management System",
    font=("Arial", 16),
    fg="#4b5563",
    bg="white"
)

subtitle.place(x=255, y=90)

navbar = tk.Frame(
    root,
    bg="#002060",
    height=50
)

navbar.pack(fill="x")

home_label = tk.Label(
    navbar,
    text="🏠 HOME",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#002060"
)

home_label.place(x=50, y=12)

portal_label = tk.Label(
    navbar,
    text="👤 ATTENDANCE PORTAL",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#002060"
)

portal_label.place(x=180, y=12)

wifi_label = tk.Label(
    navbar,
    text="📶 Connected to Institute WiFi",
    font=("Arial", 12),
    fg="white",
    bg="#002060"
)

wifi_label.place(x=880, y=12)

main_card = tk.Frame(
    root,
    bg="white",
    bd=1,
    relief="solid"
)

main_card.place(x=30, y=240, width=1140, height=240)

left_title = tk.Label(
    main_card,
    text="Enter Student ID",
    font=("Arial", 16, "bold"),
    fg="#001f5b",
    bg="white"
)

left_title.place(x=30, y=20)

student_entry = tk.Entry(
    main_card,
    font=("Arial", 15),
    bd=2,
    relief="solid"
)

student_entry.place(x=30, y=60, width=580, height=40)

entry_btn = tk.Button(
    main_card,
    text="MARK ENTRY",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#16a34a",
    activebackground="#15803d",
    cursor="hand2",
    bd=0,
    command=mark_entry
)

entry_btn.place(x=30, y=120, width=270, height=45)

exit_btn = tk.Button(
    main_card,
    text="MARK EXIT",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#dc2626",
    activebackground="#b91c1c",
    cursor="hand2",
    bd=0,
    command=mark_exit
)

exit_btn.place(x=340, y=120, width=270, height=45)

view_btn = tk.Button(
    main_card,
    text="VIEW ATTENDANCE",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#2563eb",
    activebackground="#1d4ed8",
    cursor="hand2",
    bd=0,
    command=view_attendance
)

view_btn.place(x=30, y=180, width=580, height=40)

divider2 = tk.Frame(
    main_card,
    bg="#d1d5db",
    width=2,
    height=190
)

divider2.place(x=660, y=20)

wifi_card = tk.Frame(
    main_card,
    bg="#f5f9ff",
    bd=1,
    relief="solid"
)

wifi_card.place(x=710, y=20, width=390, height=110)

wifi_title = tk.Label(
    wifi_card,
    text="Institute WiFi Required",
    font=("Arial", 14, "bold"),
    fg="#001f5b",
    bg="#f5f9ff"
)

wifi_title.place(x=20, y=15)

wifi_text = tk.Label(
    wifi_card,
    text="Please connect to institute WiFi\nbefore marking attendance.",
    font=("Arial", 11),
    fg="#4b5563",
    bg="#f5f9ff",
    justify="left"
)

wifi_text.place(x=20, y=50)

today_label = tk.Label(
    main_card,
    text="Today",
    font=("Arial", 14, "bold"),
    fg="#001f5b",
    bg="white"
)

today_label.place(x=710, y=150)

date_box = tk.Frame(
    main_card,
    bg="white",
    bd=1,
    relief="solid"
)

date_box.place(x=710, y=180, width=280, height=40)

date_label = tk.Label(
    date_box,
    text="",
    font=("Arial", 11),
    fg="#001f5b",
    bg="white"
)

date_label.pack(pady=8)

record_frame = tk.Frame(
    root,
    bg="white",
    bd=1,
    relief="solid"
)

record_frame.place(x=30, y=500, width=1140, height=160)

record_title = tk.Label(
    record_frame,
    text="Attendance Records",
    font=("Arial", 16, "bold"),
    fg="#001f5b",
    bg="white"
)

record_title.place(x=20, y=10)

attendance_box = ScrolledText(
    record_frame,
    font=("Courier New", 11),
    bg="white",
    fg="black",
    bd=1
)

attendance_box.place(x=15, y=45, width=1105, height=95)

attendance_box.insert(
    tk.END,
    "\n"
    "=====================================\n"
    "     ZILLIONSOFTECH INSTITUTE\n"
    "        ATTENDANCE RECORD\n"
    "=====================================\n\n"
    'Enter Student ID and click "View Attendance".'
)

footer = tk.Frame(
    root,
    bg="#002060",
    height=45
)

footer.pack(side="bottom", fill="x")

footer_label = tk.Label(
    footer,
    text="© 2026 Zillionsoftech Institute | Smart Attendance Portal",
    font=("Arial", 11),
    fg="white",
    bg="#002060"
)

footer_label.pack(pady=10)

update_time()
root.mainloop()
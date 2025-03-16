import tkinter as tk
from tkinter import messagebox
import random

# Function to generate a 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to verify the OTP entered by the user
def verify_otp():
    entered_otp = otp_entry.get()  # Get the entered OTP from the user
    if entered_otp == otp:
        messagebox.showinfo("Success", "OTP Verified Successfully!")
    else:
        messagebox.showerror("Error", "Incorrect OTP. Please try again.")

# Function to handle OTP generation
def generate_and_send_otp():
    global otp
    otp = generate_otp()  # Generate a new OTP
    messagebox.showinfo("OTP Sent", f"OTP has been sent! Your OTP is: {otp}")
    print(f"Generated OTP: {otp}")  # You can remove this in production

# Set up the Tkinter window
window = tk.Tk()
window.title("OTP Verification System")

# Label for email input (just for simulation in this example)
email_label = tk.Label(window, text="Enter your email:")
email_label.pack(pady=10)

email_entry = tk.Entry(window)
email_entry.pack(pady=5)

# Button to generate OTP
generate_button = tk.Button(window, text="Generate OTP", command=generate_and_send_otp)
generate_button.pack(pady=10)

# Label for OTP entry
otp_label = tk.Label(window, text="Enter OTP:")
otp_label.pack(pady=10)

# Entry widget for the user to enter OTP
otp_entry = tk.Entry(window)
otp_entry.pack(pady=5)

# Button to verify OTP
verify_button = tk.Button(window, text="Verify OTP", command=verify_otp)
verify_button.pack(pady=20)

# Start the Tkinter main loop
window.mainloop()

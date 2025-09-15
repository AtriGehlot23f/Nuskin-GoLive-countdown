import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk

# Path to Nuskin logo. Update the filename if you rename the image.
logo_path = "nuskin_logo.jpg"
target_time = datetime(2025, 11, 14, 0, 0, 0)  # Go Live date

def update_timer():
    now = datetime.now()
    delta = target_time - now
    days = delta.days
    seconds = delta.seconds if delta.days >= 0 else 0
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if delta.days < 0:
        day_str = "Go Live Complete!"
        timer_str = "00:00:00"
    else:
        day_str = f"T-{days}"
        timer_str = f"{hours:02d}:{minutes:02d}:{secs:02d}"
    title_label.config(text="India MVP-1 Business Go Live - 14-Nov-2025")
    day_label.config(text=f"Day remaining: {day_str}")
    timer_label.config(text=f"Timer: {timer_str}")
    root.after(1000, update_timer)

root = tk.Tk()
root.title("India MVP-1 Go Live Countdown")

# Load and display Nuskin logo image
logo_img = Image.open(logo_path)
logo_img = logo_img.resize((120, 120))  # Adjust as needed
logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack(pady=10)

title_label = tk.Label(root, font=("Arial", 14))
title_label.pack()
day_label = tk.Label(root, font=("Arial", 24))
day_label.pack()
timer_label = tk.Label(root, font=("Arial", 24), fg="blue")
timer_label.pack()

update_timer()
root.mainloop()

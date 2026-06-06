import customtkinter as ctk
import pyautogui
import os
import json
import time

from datetime import datetime
from tkinter import messagebox
from plyer import notification



BASE_FOLDER = "Screenshots"
HISTORY_FILE = "history.json"

os.makedirs(BASE_FOLDER, exist_ok=True)



def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_history(data):
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)




def take_screenshot():

    filename = filename_entry.get().strip()

    if filename == "":
        filename = datetime.now().strftime("%Y%m%d_%H%M%S")

    delay = int(delay_menu.get())

    status_label.configure(text=f"Capturing in {delay} second(s)...")
    app.update()

    # Hide window
    app.withdraw()
    app.update()

    # Extra 0.5 sec ensures app disappears
    time.sleep(delay + 0.5)

    today_folder = datetime.now().strftime("%Y-%m-%d")

    save_folder = os.path.join(BASE_FOLDER, today_folder)
    os.makedirs(save_folder, exist_ok=True)

    full_path = os.path.join(save_folder, f"{filename}.png")

    screenshot = pyautogui.screenshot()
    screenshot.save(full_path)

    # Restore window
    app.deiconify()
    app.lift()
    app.focus_force()

    history = load_history()

    history.append({
        "filename": filename,
        "path": full_path,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })

    save_history(history)

    update_history()

    notification.notify(
        title="Screenshot Saved",
        message=f"{filename}.png",
        timeout=3
    )

    status_label.configure(text="Screenshot Saved Successfully")

    messagebox.showinfo(
        "Success",
        f"Screenshot saved successfully!\n\n{full_path}"
    )



def update_history():

    history_box.delete("0.0", "end")

    history = load_history()

    for item in reversed(history[-10:]):

        history_box.insert(
            "end",
            f"{item['timestamp']} | {item['filename']}\n"
        )




def open_folder():
    os.startfile(BASE_FOLDER)



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("SnapShot Pro")
app.geometry("700x550")
app.resizable(False, False)

title = ctk.CTkLabel(
    app,
    text="📸 SnapShot Pro",
    font=("Arial", 32, "bold")
)
title.pack(pady=20)

filename_entry = ctk.CTkEntry(
    app,
    width=400,
    placeholder_text="Enter screenshot filename"
)
filename_entry.pack(pady=10)

delay_menu = ctk.CTkOptionMenu(
    app,
    values=["0", "3", "5", "10"]
)
delay_menu.pack(pady=10)

capture_btn = ctk.CTkButton(
    app,
    text="Take Screenshot",
    width=320,
    height=45,
    command=take_screenshot
)
capture_btn.pack(pady=15)

folder_btn = ctk.CTkButton(
    app,
    text="Open Screenshots Folder",
    width=320,
    height=45,
    command=open_folder
)
folder_btn.pack(pady=5)

status_label = ctk.CTkLabel(
    app,
    text="Ready",
    font=("Arial", 14)
)
status_label.pack(pady=15)

history_title = ctk.CTkLabel(
    app,
    text="Recent Screenshots",
    font=("Arial", 24, "bold")
)
history_title.pack(pady=10)

history_box = ctk.CTkTextbox(
    app,
    width=600,
    height=180
)
history_box.pack(pady=10)

update_history()

app.mainloop()
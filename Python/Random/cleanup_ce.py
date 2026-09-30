import os
import time
import threading
import keyboard
import tkinter as tk
from tkinter import ttk

folder_path = r"C:\Users\jjdom\OneDrive\Desktop\mods stuff\random\ac4-steam"

deleted_count = 0
stop_flag = False
running = False

# GUI Setup
root = tk.Tk()
root.title("File Cleanup Tracker")
root.geometry("300x100")
root.resizable(False, False)

count_label = ttk.Label(root, text="Files deleted: 0", font=("Segoe UI", 14))
count_label.pack(expand=True)

def update_gui():
    count_label.config(text=f"Files deleted: {deleted_count}")
    root.after(1000, update_gui)

def delete_files():
    global deleted_count, stop_flag, running
    deleted_count = 0
    stop_flag = False
    running = True

    print("Cleanup started...")

    for root_dir, _, files in os.walk(folder_path):
        for file in files:
            if stop_flag:
                print("\nStopped by user.")
                print(f"Total files deleted: {deleted_count}")
                running = False
                return

            # Strict case-sensitive full substring match
            if "Hero Upgrades_2" in file:
                full_path = os.path.join(root_dir, file)
                try:
                    os.remove(full_path)
                    deleted_count += 1
                except Exception as e:
                    print(f"Failed to delete {full_path}: {e}")

    print("\nCleanup complete.")
    print(f"Total files deleted: {deleted_count}")
    running = False

def on_start():
    if not running:
        threading.Thread(target=delete_files, daemon=True).start()
    else:
        print("Already running...")

def on_stop():
    global stop_flag
    print("Stop requested...")
    stop_flag = True

# Hotkeys
keyboard.add_hotkey('num 1', on_start)
keyboard.add_hotkey('num 2', on_stop)

# Start UI
update_gui()

print("Press Numpad 1 to start cleanup.")
print("Press Numpad 2 to stop cleanup.")
root.mainloop()

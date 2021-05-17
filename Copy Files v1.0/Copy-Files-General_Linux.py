# Imported modules

import shutil
import tkinter as tk
import sys
from tkinter import filedialog
from tkinter import *


# Variables

source = ""
destination = ""


# Self-defined functions

def source_label_command():
    global source
    source = str(filedialog.askdirectory())
    source_label_command = tk.Label(frame, text=("Copy from: " + source))
    source_label_command.place(relx=0.11, rely=0.35, relwidth=0.8, relheight=0.06)

def destination_label_command():
    global destination
    destination = str(filedialog.askdirectory())
    destination_label_command = tk.Label(frame, text=("Copy to: " + destination))
    destination_label_command.place(relx=0.11, rely=0.53, relwidth=0.8, relheight=0.06)

def start_button_command():
    destination_entry_input = (destination_entry.get())
    if not "/" in destination_entry_input:
        save_location = destination + "/" + destination_entry_input
        shutil.copytree(source, save_location)

        destination_entry.delete(0, END)

        success_label = tk.Label(frame, text="Copied successfully!")
        success_label.place(relx=0.01, rely=0.93, relwidth=1, relheight=0.06)
        success_label.after(3000, success_label.destroy)
    else:
        print("Error: Folder names cannot contain the character '/'.")
        error_label = tk.Label(frame, text="Error: Folder names cannot contain the character '/'.")
        error_label.place(relx=0.01, rely=0.93, relwidth=1, relheight=0.06)
        error_label.after(3000, error_label.destroy)


# TKinter GUI

root = tk.Tk()

root.title("Copy Files by DD")

canvas = tk.Canvas(root, height=500, width=400)
canvas.pack()

frame = tk.Frame(canvas)
frame.place(relx=0.05, rely=-0.02, relwidth=0.875, relheight=1)

title = tk.Label(frame, text="Copy Files", font=("", 24))
title.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

source_button = tk.Button(frame, text="Select source", command=source_label_command)
source_button.place(relx=0.35, rely=0.275, relwidth=0.3, relheight=0.06)

destination_button = tk.Button(frame, text="Select destination", command=destination_label_command)
destination_button.place(relx=0.3, rely=0.45, relwidth=0.4, relheight=0.06)

destination_label = tk.Label(frame, text="Enter the new folder's name:")
destination_label.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.1)

destination_entry = tk.Entry(frame, textvariable="Student ID:")
destination_entry.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.06)

start = tk.Button(frame, text="START", command=start_button_command)
start.place(relx=0.25, rely=0.85, relwidth=0.2, relheight=0.06)

cancel = tk.Button(frame, text="CANCEL", command=sys.exit)
cancel.place(relx=0.55, rely=0.85, relwidth=0.2, relheight=0.06)

root.mainloop()
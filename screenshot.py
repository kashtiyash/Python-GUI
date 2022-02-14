import tkinter as tk
import pyautogui as pg
from tkinter import messagebox

root = tk.Tk()
root.title("Screenshot with Tkinter")
root.geometry("330x300")


def screenshot():
    screenshots = pg.screenshot()
    screenshots.save('image.png')
    tk.messagebox.showinfo("Done", "Screenshot Captured ")


# Label
tk.Label(root, text="Screenshot with Tkinter", fg="Red", font="Arial 14 bold").grid(row=0, column=1, padx=40, pady=40)

# Capture Button
capture = tk.Button(root, text="Capture", bd=2, command=screenshot)
capture.grid(row=1, column=1, columnspan=3, pady=20, padx=40)


# Quit Button
button_quit = tk.Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=3, column=1, columnspan=3, pady=20, padx=20)

root.mainloop()

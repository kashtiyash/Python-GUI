from tkinter import *

root = Tk()
root.title("Toggle Switch")
root.geometry("400x600")
root.config(bg="white")

button_mode = True


def customize():
    global button_mode
    if button_mode:
        button.config(image=off, bg="black", activebackground="black")
        root.config(bg="black")
        button_mode = False
    else:
        button.config(image=on, bg="white", activebackground="white")
        root.config(bg="white")
        button_mode = True


on = PhotoImage(file="sun.png")
off = PhotoImage(file="night.png")

button = Button(root, image=on, bd=0, bg="white", activebackground="white", command=customize)
button.pack(padx=50, pady=50)

if __name__ == '__main__':
    root.mainloop()

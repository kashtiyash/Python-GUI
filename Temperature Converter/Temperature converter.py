from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Temperature Converter")
root.geometry("300x250")


def fahrenheit_to_celsius():
    fahrenheit = frt_entry.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    frt_result["text"] = f"{round(celsius, 2)}    \N{DEGREE CELSIUS}"


def celsius_to_fahrenheit():
    celsius = cel_entry.get()
    fahrenheit = ((9 / 5) * (float(celsius))) + 32
    cel_result["text"] = f"{round(fahrenheit, 2)}    \N{DEGREE FAHRENHEIT}"


Label(text="Temperature Converter ").grid(row=0, column=0)
img = ImageTk.PhotoImage(Image.open('converter.png'))
Label(image=img).grid(row=1, column=0)

frame = LabelFrame(root, padx=30, pady=30)
frame.grid(padx=30, pady=30)


# Entry and label for fahrenheit
frt_entry = Entry(frame, width=15, borderwidth=2)
frt_label = Label(frame, text="\N{DEGREE FAHRENHEIT}")
frt_result = Label(frame, text="\N{DEGREE CELSIUS}")

frt_entry.grid(row=2, column=0)
frt_label.grid(row=2, column=1)
frt_result.grid(row=2, column=3)

#  convert Button
btn_convert1 = Button(frame, text=" --> ", command=fahrenheit_to_celsius)
btn_convert2 = Button(frame, text=" --> ", command=celsius_to_fahrenheit)
btn_convert1.grid(row=2, column=2)
btn_convert2.grid(row=3, column=2)

# Entry and label for celsius
cel_entry = Entry(frame, width=15, borderwidth=2)
cel_label = Label(frame, text="\N{DEGREE CELSIUS}")
cel_result = Label(frame, text="\N{DEGREE FAHRENHEIT}")

cel_entry.grid(row=3, column=0)
cel_label.grid(row=3, column=1)
cel_result.grid(row=3, column=3)

root.mainloop()

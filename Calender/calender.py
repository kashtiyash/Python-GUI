from tkinter import *

from PIL import ImageTk, Image
import calendar

root = Tk()
root.geometry('400x300')
root.title('Calender')


def show():
    m = int(month.get())
    y = int(year.get())
    output = calendar.month(y, m)
    cal.insert('end', output)


def clear():
    cal.delete(1.0, 'end')


def exit_program():
    root.destroy()


img = ImageTk.PhotoImage(Image.open('calendar1.png'))
label = Label(image=img)
label.place(x=170, y=3)

m_label = Label(root, text="Month", font=('Roboto', '11', 'bold'))
m_label.place(x=70, y=80)

month = Spinbox(root, from_=1, to=12, width=5,justify=CENTER)
month.place(x=140, y=80)

y_label = Label(root, text="Year", font=('Roboto', '11', 'bold'))
y_label.place(x=210, y=80)

year = Spinbox(root, from_=2000, to=3000, width=8,justify=CENTER)
year.place(x=260, y=80)

cal = Text(root, width=33, height=8, relief=RIDGE, borderwidth=4)
cal.place(x=60, y=110)

show = Button(root, text="Show", font=('Roboto', 10, 'bold'), fg="Green", relief=RIDGE, borderwidth=4, command=show)
show.place(x=100, y=250)

clear = Button(root, text="Clear", font=('Roboto', 10, 'bold'), relief=RIDGE, borderwidth=4, command=clear)
clear.place(x=170, y=250)

exit_button = Button(root, text="Exit", font=('Roboto', 10, 'bold'), fg="Red", relief=RIDGE, borderwidth=4,
                     command=exit_program)
exit_button.place(x=240, y=250)

root.mainloop()

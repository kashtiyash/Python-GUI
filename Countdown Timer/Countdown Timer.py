from tkinter import *
from playsound import playsound
import time

root = Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False, False)

heading = Label(root, text="Timer", font="Arial 30 bold", bg="#000", fg="#ea3548")
heading.pack(pady=10)

Label(root, font=("Arial", 15, "bold"), text="Current Time :  ", bg="black", fg="white").place(x=65, y=70)


# Clock
def clock():
    clock_time = time.strftime(" %h : %M : %S %p")
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = Label(root, font=("arial", 15, "bold"), text="", fg="white", bg="#000")
current_time.place(x=200, y=70)
clock()

# Timer
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font="arial 50", bg="#000", fg="white", borderwidth=0).place(x=30, y=155)
hrs.set("00")

mins = StringVar()
Entry(root, textvariable=mins, width=2, font="arial 50", bg="#000", fg="white", borderwidth=0).place(x=150, y=155)
mins.set("00")

sec = StringVar()
Entry(root, textvariable=sec, width=2, font="arial 50", bg="#000", fg="white", borderwidth=0).place(x=270, y=155)
sec.set("00")


Label(root, text="hours", font="arial 12 ", bg="#000", fg="#fff").place(x=105, y=200)
Label(root, text="mins", font="arial 12 ", bg="#000", fg="#fff").place(x=225, y=200)
Label(root, text="sec", font="arial 12 ", bg="#000", fg="#fff").place(x=345, y=200)


def Timer():
    times = int(hrs.get())*3600 + int(mins.get()) * 60 + int(sec.get())

    while times > -1:
        minute, second = (times//60, times % 60)

        hour = 0
        if minute > 60:
            hour, minute = (minute//60, minute % 60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if times ==0:
            playsound("ring.wav")
            sec.set("00")
            mins.set("00")
            hrs.set("00")

        times -= 1


def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")


def eggs():
    hrs.set("00")
    mins.set("10")
    sec.set("00")


def face():
    hrs.set("00")
    mins.set("15")
    sec.set("00")


button = Button(root, text="Start", bg="#ea3548", bd=0, fg="#fff", width=20, height=2, font="arial 10 bold",
                command=Timer)
button.pack(padx=5, pady=40, side=BOTTOM)


Image1 = PhotoImage(file="FaceMask.png")
button1 = Button(root, image=Image1, bg="#000", bd=0, command=face)
button1.place(x=7, y=300)
Image2 = PhotoImage(file="SteamEggs.png")
button2 = Button(root, image=Image2, bg="#000", bd=0, command=eggs)
button2.place(x=137, y=300)
Image3 = PhotoImage(file="Brush.png")
button3 = Button(root, image=Image3, bg="#000", bd=0, command=brush)
button3.place(x=267, y=300)


if __name__ == '__main__':
    root.mainloop()

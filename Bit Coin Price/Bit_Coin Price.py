from tkinter import *
import requests

root = Tk()
root.title("Bit-Coin Price ")
root.geometry("400x250")

#  api was from coindesk which shows current price of the bitcoin
# many apis are also there which return also other information about cyrptocoins

url = "" # Put your api here

re = requests.get(url)
data = re.json()

time = data["time"]["updated"]
usd = data["bpi"]["USD"]["rate"]
GBP = data["bpi"]["GBP"]["rate"]
EUR = data["bpi"]["EUR"]["rate"]


frame = LabelFrame(root, padx=20, pady=20, bd=10, bg="#E0F2F2", fg="BLACK", relief=SUNKEN)
Label(frame, text="Bitcoin  Rate", bg="#E0F2F2", fg="BLACK").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
Label(frame, text=f"Time -     {time} ", bg="#E0F2F2", fg="BLACK").grid(row=1, column=0, padx=5, pady=5)
Label(frame, text=f"USD  -     {usd}  $", bg="#E0F2F2", fg="BLACK").grid(row=2, column=0, padx=5, pady=5)
Label(frame, text=f"GBP  -     {GBP}  pound", bg="#E0F2F2", fg="BLACK").grid(row=3, column=0, padx=5, pady=5)
Label(frame, text=f"EURO -     {EUR}  euro", bg="#E0F2F2", fg="BLACK").grid(row=4, column=0, padx=5, pady=5)

frame.pack()
root.mainloop()

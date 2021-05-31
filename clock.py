import tkinter as tk
from time import strftime

app=tk.Tk()
app.title("clock")

def time():
    string= strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label=tk.Label(app,font=("Cambria (Headings)",70),background="black",foreground="red")
label.pack(anchor="n")
time()

# label=tk.Label(app,font=("AxlongScreen_Font-Light",50),background="black",foreground="red")
# label.pack(anchor="center")
# time()


app.mainloop()
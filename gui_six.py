from tkinter import *
from tkinter import scrolledtext
import find

window = Tk()
res = Tk()
window.title("Final Project")
window.geometry('350x200')
res.geometry('650x200')
res.withdraw()
lbl = Label(window, text="Type the Name of the Actor")
lbl.grid(column=0, row=0)
txt = Entry(window,width=20)
txt.grid(column=1, row=0)

def clicked():
    window.withdraw()
    res.deiconify()
    actor = txt.get()
    scroll = scrolledtext.ScrolledText(res, width=80, height=10)
    scroll.grid(column=0, row=0)
    #scroll.insert(res.insert, find.find_actor())
    scroll.insert(END, find.find_actor(str(actor)))

btn = Button(window, text="Find Actor", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
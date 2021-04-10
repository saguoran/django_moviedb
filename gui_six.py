from tkinter import *
from tkinter import scrolledtext
import find

window = Tk()
# res = Tk()

window.title("Final Project")
window.geometry('650x300')
# res.geometry('650x200')
# res.withdraw()
Label(window, text="Type the Name of the Actor").grid(column=0, row=0)
txt = Entry(window,width=20)
txt.grid(column=1, row=0)
scroll = scrolledtext.Text(window)
scroll.grid(column=0, row=1, columnspan=3)


def clicked():
    actor = txt.get()
    scroll.delete("1.0","end")
    bacon_distance = find.find_actor(str(actor))
    scroll.insert(END, bacon_distance)


btn = Button(window, text="Find Actor", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
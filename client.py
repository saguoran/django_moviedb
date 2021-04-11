#!/usr/bin/env python3
from tkinter import *
from tkinter import scrolledtext
import find


import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server



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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = actor
        s.sendall(str.encode(data, encoding='utf-8'))
        print('Sent', data)
        received_data= s.recv(1024)
        # bacon_distance = find.find_actor(str(actor))
        scroll.insert(END, received_data.decode('utf-8'))


btn = Button(window, text="Find Actor", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
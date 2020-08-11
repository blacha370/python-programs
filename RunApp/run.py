from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import tkinter
import webbrowser
import json


def run():
    print(filedialog.askopenfile())


run()

root = Tk()
root.title("Run")
root.geometry('800x300')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
urls = StringVar()
http = StringVar()
http_links = StringVar()
http_entry = ttk.Entry(mainframe, width=100, textvariable=http)
http_entry.grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=urls).grid(
    column=1, row=1, rowspan=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=http_links, width=100).grid(
    column=1, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Add Program", command=addProgram).grid(
    column=2, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Remove Program", command=removeProgram).grid(
    column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Add Page", command=addPage).grid(
    column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Remove Page", command=removePage).grid(
    column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Run", command=run).grid(
    column=2, row=5, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
root.bind('<Return>', addProgram, run)


things_to_run = getUserConfig()
print(things_to_run)
root.mainloop()

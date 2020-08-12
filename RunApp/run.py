from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sys
from AppRunner import AppRunner

Runner = AppRunner()


def setUrls():
    urls_value = str()
    for program in enumerate(Runner.program_list):
        if program[0] == 0:
            urls_value = program[1]['path'] + " " + str(program[1]['amount'])
        else:
            urls_value += '\n' + \
                program[1]['path'] + " " + str(program[1]['amount'])
    urls.set(urls_value)


def setHttps():
    https_value = str()
    for page in enumerate(Runner.page_list):
        if page[0] == 0:
            https_value = page[1]
        else:
            https_value += '\n' + page[1]
    http_links.set(https_value)


def addProgram():
    url = filedialog.askopenfile().name
    Runner.addProgram(url)
    setUrls()


def removeProgram():
    url = filedialog.askopenfile().name
    Runner.removeProgram(url)
    setUrls()


def addPage():
    link = http.get()
    if link != '':
        http.set('')
        Runner.addPage(link)
        setHttps()


def removePage():
    link = http.get()
    if link != '':
        http.set('')
        Runner.removePage(link)
        setHttps()


def run():
    Runner.run()


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
root.bind('<Return>')

setUrls()
setHttps()
root.mainloop()

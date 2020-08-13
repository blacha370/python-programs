from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from functools import partial
from AppRunner import AppRunner

Runner = AppRunner()


def setUrls():
    for widget in programs_frame.winfo_children():
        widget.destroy()
    for program in Runner.program_list:
        program_frame = ttk.Frame(programs_frame)
        program_frame.grid()
        label = ttk.Label(program_frame, text=program['path'])
        button = ttk.Button(program_frame, text="Delete",
                            command=partial(removeProgram, program['path']))
        label.grid(column=0, row=0)
        button.grid(column=1, row=0)


def setHttps():
    for widget in pages_frame.winfo_children():
        widget.destroy()
    for page in Runner.page_list:
        page_frame = ttk.Frame(pages_frame, width=100)
        page_frame.grid()
        label = ttk.Label(page_frame, text=page)
        button = ttk.Button(page_frame, text="Delete",
                            command=partial(removePage, page))
        label.grid(column=0, row=0)
        button.grid(column=1, row=0)


def addProgram():
    url = filedialog.askopenfile().name
    Runner.addProgram(url)
    setUrls()


def removeProgram(url):
    Runner.removeProgram(url)
    setUrls()


def addPage():
    link = http.get()
    if link != '':
        http.set('')
        Runner.addPage(link)
        setHttps()


def removePage(link):
    Runner.removePage(link)
    setHttps()


def run():
    Runner.run()


root = Tk()
root.title("Run")
root.geometry('800x300')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.pack()

data_frame = ttk.Frame(main_frame, padding='3 3 12 12')
data_frame.grid(column=0, row=0)

programs_frame = ttk.Frame(data_frame)
programs_frame.grid(column=0, row=1)

http = StringVar()
http_entry = ttk.Entry(data_frame, width=100, textvariable=http)
http_entry.grid(column=0, row=2)

pages_frame = ttk.Frame(data_frame)
pages_frame.grid(column=0, row=3)

buttonsframe = ttk.Frame(main_frame, padding='3 3 12 12')
buttonsframe.grid(column=1, row=0)


http_links = StringVar()


ttk.Button(buttonsframe, text="Add Program",
           command=addProgram).grid(sticky=(E, W))
ttk.Button(buttonsframe, text="Add Page", command=addPage).grid(sticky=(E, W))
ttk.Button(buttonsframe, text="Run", command=run).grid(sticky=(E, W))


root.bind('<Return>')

setUrls()
setHttps()

root.mainloop()

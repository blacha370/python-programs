from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from Observer import Observer
from Component import Component
from AppRunner import AppRunner
import json
import os
import webbrowser


class App():
    def __init__(self):
        self.runner = AppRunner()
        self.observer = Observer(self.runner)
        self.programs = list()
        self.pages = list()

        self.getUserConfig()
        self.updatePrograms()
        self.updatePages()

    def getUserConfig(self):
        try:
            with open('./data.json', 'r', encoding='UTF-8') as file:
                json_data = file.read()
                try:
                    data = json.loads(json_data)
                    self.runner.program_list = data['program_list']
                    self.runner.page_list = set(data['page_list'])
                except:
                    pass
        except FileNotFoundError:
            pass

    def updatePrograms(self):
        self.deleteComponents(programs_frame)
        self.programs = self.runner.program_list
        for program in self.programs:
            Component(programs_frame, program['path'],
                      program['amount'], observer=self.observer)

    def updatePages(self):
        self.deleteComponents(pages_frame)
        self.pages = self.runner.page_list
        for page in self.pages:
            Component(pages_frame, page, observer=self.observer)

    def deleteComponents(self, parent):
        for child in parent.winfo_children():
            child.destroy()

    def run(self):
        with open('./data.json', 'w', encoding='UTF-8') as file:
            data = {"program_list": self.runner.program_list,
                    "page_list": list(self.runner.page_list)}
            json_data = json.dumps(data)
            file.write(json_data)
        for program in self.runner.program_list:
            for _ in range(program['amount']):
                path = program['path']
                os.startfile(path)
        for page in self.runner.page_list:
            webbrowser.open_new_tab(page)


def addProgram():
    url = filedialog.askopenfile().name
    app.runner.addProgram(url)
    app.updatePrograms()


def addPage():
    link = http.get()
    if link != '':
        http.set('')
        app.runner.addPage(link)
        app.updatePages()


def run():
    app.run()
    root.destroy()


root = Tk()
root.title("Run")
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

ttk.Style().configure('darkBtn.TButton',
                      background='black')


main_frame = ttk.Frame(root)
main_frame.pack()


data_frame = ttk.Frame(main_frame, padding='3 3 3 3')
data_frame.grid(column=1, row=1, sticky='nswe')


http = StringVar()
http_entry = ttk.Entry(data_frame, width=60,
                       textvariable=http)
http_entry.grid(column=0, row=1, sticky='ew')

pages_frame = ttk.Frame(data_frame, padding='3 3 3 3')
pages_frame.grid(column=0, row=2, sticky='e')

programs_frame = ttk.Frame(data_frame, padding='3 3 3 3')
programs_frame.grid(column=0, row=3, sticky='e')

buttonsframe = ttk.Frame(main_frame, padding='3 3 3 3')
buttonsframe.grid(column=2, row=1, sticky='nswe')


http_links = StringVar()

ttk.Button(buttonsframe, text="Add Page", command=addPage,
           padding='3 3 3 3').grid(sticky='nswe')
ttk.Button(buttonsframe, text="Add Program", style='darkBtn.TButton',
           command=addProgram, padding='3 3 3 3').grid(sticky='nswe')
ttk.Button(buttonsframe, text="Run", command=run,
           padding='3 3 3 3').grid(sticky='nswe')

app = App()
root.mainloop()

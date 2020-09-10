from tkinter import *
from tkinter import ttk
import win32gui
import pywintypes
from Component import Component
from Window import Window


class MainFrame:
    def __init__(self, root, observer, data):
        self.name = 'main_frame'
        self.observer = observer
        self.data = data
        self.root = root
        self.main_frame = ttk.Frame(self.root)
        self.data_frame = ttk.Frame(self.main_frame)
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.url_entry = ttk.Entry(self.data_frame)
        self.pages_frame = ttk.Frame(self.data_frame)
        self.programs_frame = ttk.Frame(self.data_frame)
        self.add_page_button = ttk.Button(self.buttons_frame, text='Add page', command=self.addPage)
        self.add_program_button = ttk.Button(self.buttons_frame, text='Add program', command=self.addProgram)
        self.place_programs_button = ttk.Button(self.buttons_frame, text='Place programs', command=self.placePrograms)
        self.exit_button = ttk.Button(self.buttons_frame, text='Run', command=self.exitGui)
        self.placeElements()
        self.placeComponents(data)

    def placeElements(self):
        self.main_frame.grid(column=1, row=1)
        self.data_frame.grid(column=1, row=1, sticky='NSWE')
        self.buttons_frame.grid(column=2, row=1, sticky='NSWE')
        self.url_entry.grid(column=1, row=1, sticky='N')
        self.pages_frame.grid(column=1, row=2)
        self.programs_frame.grid(column=1, row=3)
        self.add_page_button.grid(column=1, row=1, sticky='NSWE')
        self.add_program_button.grid(column=1, row=2, sticky='NSWE')
        self.place_programs_button.grid(column=1, row=3, sticky='NSWE')
        self.exit_button.grid(column=1, row=4, sticky='NSWE')

    def placeComponents(self, data):
        self.data = data
        for child in self.pages_frame.winfo_children():
            child.destroy()
        for page in self.data['pages_list']:
            Component(self.pages_frame, page, observer=self.observer)
        for child in self.programs_frame.winfo_children():
            child.destroy()
        for program in self.data['programs_list']:
            Component(self.programs_frame, program['path'], program['positions'], observer=self.observer)

    def addProgram(self):
        try:
            path = win32gui.GetOpenFileNameW()
            self.observer.update(path[0], 'programs_list', 'add')
        except pywintypes.error:
            return

    def addPage(self):
        url = self.url_entry.get()
        self.url_entry.delete(0, END)
        if url:
            self.observer.update(url, 'pages_list', 'add')
        return

    def placePrograms(self, path=''):
        if path == '':
            for program in self.data['programs_list']:
                i = 0
                for position in program['positions']:
                    Window(program['path'], position, i, observer=self.observer)
                    i += 1
        else:
            for program in self.data['programs_list']:
                if program['path'] == path:
                    i = 0
                    for position in program['positions']:
                        Window(program['path'], position, i, observer=self.observer)
                        i += 1
                    break

    def exitGui(self):
        self.observer.run()

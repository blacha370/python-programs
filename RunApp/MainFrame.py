from tkinter import *
from tkinter import ttk
import win32gui
import pywintypes
import copy
from Component import Component


class MainFrame:
    def __init__(self, root, observer, data):
        self.name = 'main_frame'
        self.observer = observer
        self.data = {
            'elements': {'root': root, 'main_frame': None, 'data_frame': None, 'buttons_frame': None},
            'components': copy.deepcopy(data)
        }
        self.gui_structure = {
            'buttons': ({'parent': self.data['elements']['buttons_frame'], 'name': "add_page_button", 'command': self.addPage, "text": 'AddPage', "position": (2, 1)},
                        {'parent': self.data['elements']['buttons_frame'], 'name': "add_program_button", 'command': self.addProgram, "text": 'AddProgram', "position": (2, 2)},
                        {'parent': self.data['elements']['buttons_frame'], 'name': "exit_button", 'command': self.exitGui, "text": "Run", "position": (2, 3)}
                        )
        }
        self.placeElements()
        self.placeComponents(data)

    def placeElements(self):
        main_frame = ttk.Frame(self.data['elements']['root'])
        self.data['elements']['main_frame'] = main_frame
        main_frame.grid(column=1, row=1)

        data_frame = ttk.Frame(self.data['elements']['main_frame'])
        self.data['elements']['data_frame'] = data_frame
        data_frame.grid(column=1, row=1, sticky='NSWE')

        buttons_frame = ttk.Frame(self.data['elements']['main_frame'])
        self.data['elements']['buttons_frame'] = buttons_frame
        buttons_frame.grid(column=2, row=1, sticky='NSWE')

        url_entry = ttk.Entry(self.data['elements']['data_frame'])
        self.data['elements']['url_entry'] = url_entry
        url_entry.grid(column=1, row=1, sticky='N')

        pages_frame = ttk.Frame(self.data['elements']['data_frame'])
        self.data['elements']['pages_frame'] = pages_frame
        pages_frame.grid(column=1, row=2)

        programs_frame = ttk.Frame(self.data['elements']['data_frame'])
        self.data['elements']['programs_frame'] = programs_frame
        programs_frame.grid(column=1, row=3)

        add_page_button = ttk.Button(self.data['elements']['buttons_frame'], text='Add page', command=self.addPage)
        self.data['elements']['add_page_button'] = add_page_button
        add_page_button.grid(column=1, row=1, sticky='NSWE')

        add_program_button = ttk.Button(self.data['elements']['buttons_frame'], text='Add program', command=self.addProgram)
        self.data['elements']['add_program_button'] = add_program_button
        add_program_button.grid(column=1, row=2, sticky='NSWE')

        exit_button = ttk.Button(self.data['elements']['buttons_frame'], text='Run', command=self.exitGui)
        self.data['elements']['exit_button'] = exit_button
        exit_button.grid(column=1, row=3, sticky='NSWE')

    def placeComponents(self, data):
        for child in self.data['elements']['programs_frame'].winfo_children():
            child.destroy()
        for child in self.data['elements']['pages_frame'].winfo_children():
            child.destroy()
        for program in data['programs_list']:
            component = (Component(self.data['elements']['programs_frame'], program['path'], program['positions'], observer=self.observer))
            self.data['components']['programs_list'].append({'path': program['path'], 'component': component})
        for page in data['pages_list']:
            self.data['components']['pages_list'].add(Component(self.data['elements']['pages_frame'], page, observer=self.observer))

    def addProgram(self):
        try:
            path = win32gui.GetOpenFileNameW()
        except pywintypes.error:
            return
        finally:
            self.observer.update(path[0], 'programs_list', 'add')

    def addPage(self):
        url = self.data['elements']['url_entry'].get()
        self.data['elements']['url_entry'].delete(0, END)
        if url:
            self.observer.update(url, 'pages_list', 'add')
        return

    def exitGui(self):
        self.observer.run()
        self.data['elements']['root'].destroy()

    def destroyFrame(self):
        self.data['elements']['main_frame'].destroy()


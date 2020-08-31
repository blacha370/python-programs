from tkinter import *
from tkinter import ttk
from Component import Component
import win32gui
import pywintypes


class Gui:
    def __init__(self, observer):
        self.data = {
            'elements': {
                'root': None, 'main_frame': None, 'data_frame': None, 'buttons_frame': None},
            'components': {'programs_list': list(), 'pages_list': set()}
        }
        self.gui_structure = {
            'elements': ({'widget': ttk.Frame, 'parent': self.data['elements']['root'], 'name': 'main_frame', 'position': (1, 1)},
                         {'widget': ttk.Frame, 'parent': self.data['elements']['main_frame'], 'name': 'data_frame', 'position': (1, 1)},
                         {'widget': ttk.Frame, 'parent': self.data['elements']['main_frame'], 'name': 'buttons_frame', 'position': (2, 1)},
                         {'widget': ttk.Entry, 'parent': self.data['elements']['data_frame'], 'name': 'url_entry', 'position': (1, 1)},
                         {'widget': ttk.Frame, 'parent': self.data['elements']['data_frame'], 'name': 'programs_frame', 'position': (1, 2)},
                         {'widget': ttk.Frame, 'parent': self.data['elements']['data_frame'], 'name': 'pages_frame', 'position': (1, 3)}
                         ),
            'buttons': ({'parent': self.data['elements']['buttons_frame'], 'name': "add_page_button", 'command': self.addPage, "text": 'AddPage', "position": (2, 1)},
                        {'parent': self.data['elements']['buttons_frame'], 'name': "add_program_button", 'command': self.addProgram, "text": 'AddProgram', "position": (2, 2)},
                        {'parent': self.data['elements']['buttons_frame'], 'name': "exit_button", 'command': self.exitGui, "text": "Run", "position": (2, 3)}
                        )
        }
        self.observer = observer
        self.programs = set()
        self.pages = set()
        self.root = Tk()
        self.data['elements']['root'] = self.root
        self.root.columnconfigure(0, weight=1)

    def createGuiElement(self, widget_type, parent, element_name, position=(0, 0)):
        element = widget_type(parent)
        element.grid(column=position[0], row=position[1])
        self.data['elements'][element_name] = element

    def createButton(self, parent, button_name, command, text=str(), position=(0, 0)):
        element = ttk.Button(parent, command=command, text=text)
        element.grid(column=position[0], row=position[1])
        self.data['elements'][button_name] = element

    def placeElements(self):
        for element in self.gui_structure['elements']:
            self.createGuiElement(element['widget'], element['parent'], element['name'], position=element['position'])
        for button in self.gui_structure['buttons']:
            self.createButton(button['parent'], button['name'], button['command'], text=button['text'], position=button['position'])

    def placeComponents(self, data):
        components_to_place = {'programs_list': list(), 'pages_list': set()}
        for program in data['programs_list']:
            if program not in self.data['components']['programs_list']:
                components_to_place['programs_list'].append(program)
        components_to_place['pages_list'] = data['pages_list'] - self.data['components']['pages_list']
        for program in components_to_place['programs_list']:
            self.programs.add(Component(self.data['elements']['programs_frame'], program['path'], program['amount'], observer=self.observer))
        for page in components_to_place['pages_list']:
            self.pages.add(Component(self.data['elements']['pages_frame'], page, observer=self.observer))
        self.data['components'] = components_to_place

    def createGui(self, data):
        self.placeElements()
        self.placeComponents(data)
        self.root.mainloop()

    def addProgram(self):
        try:
            path = win32gui.GetOpenFileNameW()
        except pywintypes.error:
            path = ''
        finally:
            return path

    def addPage(self):
        url = self.data['elements']['url_entry'].get()
        self.data['elements']['url_entry'].delete(0, END)
        if url:
            if not url.startswith('http://' or 'https://'):
                url = 'http://' + url
            return url
        return

    def exitGui(self):
        self.root.destroy()
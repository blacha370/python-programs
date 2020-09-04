from tkinter import *
from tkinter import ttk
import win32gui
import pywintypes
import copy
from Component import Component



class MainFrame():
    def __init__(self, root, observer, data):
        self.observer = observer
        self.root = root
        self.data = {
            'elements': {'root': self.root, 'main_frame': None, 'data_frame': None, 'buttons_frame': None},
            'components': copy.deepcopy(data)
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
        self.placeElements()
        self.placeComponents(data)

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
        for child in self.data['elements']['programs_frame'].winfo_children():
            child.destroy()
        for child in self.data['elements']['pages_frame'].winfo_children():
            child.destroy()
        for program in data['programs_list']:
            print(data['programs_list'])
            print('ok')
            component = (Component(self.data['elements']['programs_frame'], program['path'], program['amount'], observer=self.observer))
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
        self.root.destroy()

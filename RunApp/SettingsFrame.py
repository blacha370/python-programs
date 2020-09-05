from tkinter import ttk
from GuiCreator import GuiCreator


class SettingsFrame:
    def __init__(self, root, observer, data):
        self.name = 'settings_frame'
        self.path = data
        self.observer = observer
        self.data = {
            'elements': {'root': root, 'settings_frame': None, 'settings_notebook': None, 'buttons_frame': None}
        }
        self.gui_structure = {
            'elements': ({'widget': ttk.Frame, 'parent': self.data['elements']['root'], 'name': 'settings_frame', 'position': (1, 1)},
                         {'widget': ttk.Notebook, 'parent': self.data['elements']['settings_frame'], 'name': 'settings_notebook', 'position': (1, 1)},
                         {'widget': ttk.Frame, 'parent': self.data['elements']['settings_frame'], 'name': 'buttons_frame', 'position': (3, 1)},
                         {'widget': ttk.Label, 'parent': self.data['elements']['settings_notebook'], 'name': 'monitor-label', 'position': (1, 1), 'text': 'monitor:'},
                         {'widget': ttk.Label, 'parent': self.data['elements']['settings_notebook'], 'name': 'x-label', 'position': (1, 2), 'text': 'x:'},
                         {'widget': ttk.Label, 'parent': self.data['elements']['settings_notebook'], 'name': 'y-label', 'position': (1, 3), 'text': 'y:'},
                         {'widget': ttk.Label, 'parent': self.data['elements']['settings_notebook'], 'name': 'width-label', 'position': (1, 4), 'text': 'width:'},
                         {'widget': ttk.Label, 'parent': self.data['elements']['settings_notebook'], 'name': 'height-label', 'position': (1, 5), 'text': 'height:'},
                         {'widget': ttk.Combobox, 'parent': self.data['elements']['settings_notebook'], 'name': 'monitor_combobox', 'position': (2, 1)},
                         {'widget': ttk.Spinbox, 'parent': self.data['elements']['settings_notebook'], 'name': 'x_entry', 'position': (2, 2)},
                         {'widget': ttk.Spinbox, 'parent': self.data['elements']['settings_notebook'], 'name': 'y_entry', 'position': (2, 3)},
                         {'widget': ttk.Spinbox, 'parent': self.data['elements']['settings_notebook'], 'name': 'width_entry', 'position': (2, 4)},
                         {'widget': ttk.Spinbox, 'parent': self.data['elements']['settings_notebook'], 'name': 'height_entry', 'position': (2, 5)},
                         {'widget': ttk.Frame, 'parent': self.data['elements']['settings_frame'], 'name': 'programs_frame', 'position': (1, 2)},
                         {'widget': ttk.Frame, 'parent': self.data['elements']['settings_frame'], 'name': 'pages_frame', 'position': (1, 3)}
                         ),
            'buttons': ({'parent': self.data['elements']['buttons_frame'], 'name': "save_button", 'command': self.saveData, "text": "Save", "position": (3, 1)},
                        {'parent': self.data['elements']['buttons_frame'], 'name': "delete_button", 'command': self.delete, "text": "Delete", "position": (3, 2)})
        }
        self.placeElements()

    def placeElements(self):
        for element in self.gui_structure['elements']:
            GuiCreator.createGuiElement(self.data, element['widget'], element['parent'], element['name'], position=element['position'], text=element.get('text'))
        for button in self.gui_structure['buttons']:
            GuiCreator.createButton(self.data, button['parent'], button['name'], button['command'], text=button['text'], position=button['position'])

    def delete(self):
        self.observer.update(self.path, 'programs_list', 'delete')

    def saveData(self):
        self.observer.switchFrame(None)

    def destroyFrame(self):
        GuiCreator.destroyFrame(self.data['elements'])

from tkinter import ttk
from Monitors import Monitors


class SettingsFrame:
    def __init__(self, root, observer, data):
        self.name = 'settings_frame'
        self.path = data['path']
        self.monitors = Monitors.getMonitors()
        self.observer = observer
        self.data = {
            'elements': {'root': root, 'settings_frame': None, 'cards_frame': None, 'settings_notebook': None, 'buttons_frame': None}
        }
        self.placeElements(data['positions'])

    def placeElements(self, positions):
        settings_frame = ttk.Frame(self.data['elements']['root'])
        self.data['elements']['settings_frame'] = settings_frame
        settings_frame.grid(column=1, row=1)

        tabs_frame = ttk.Frame(self.data['elements']['settings_frame'])
        self.data['elements']['tabs_frame'] = tabs_frame
        tabs_frame.grid(column=1, row=1, columnspan=2)

        settings_notebook = ttk.Notebook(self.data['elements']['settings_frame'])
        self.data['elements']['settings_notebook'] = settings_notebook
        settings_notebook.grid(column=1, row=2)

        buttons_frame = ttk.Notebook(self.data['elements']['settings_frame'])
        self.data['elements']['buttons_frame'] = buttons_frame
        buttons_frame.grid(column=2, row=2)

        i = 0
        for position in positions:
            i += 1
            tab_button = ttk.Button(self.data['elements']['tabs_frame'], text='tab')
            self.data['elements'][str(position)] = tab_button
            tab_button.grid(column=i, row=1)

        monitors_label = ttk.Label(self.data['elements']['settings_notebook'], text='Monitor:')
        self.data['elements']['monitors_label'] = monitors_label
        monitors_label.grid(column=1, row=1)

        monitors_combobox = ttk.Combobox(self.data['elements']['settings_notebook'])
        self.data['elements']['monitors_combobox'] = monitors_combobox
        monitors_combobox.grid(column=2, row=1)

        x_label = ttk.Label(self.data['elements']['settings_notebook'], text='X:')
        self.data['elements']['x_label'] = x_label
        x_label.grid(column=1, row=2)

        x_spinbox = ttk.Spinbox(self.data['elements']['settings_notebook'])
        self.data['elements']['x_spinbox'] = x_spinbox
        x_spinbox.grid(column=2, row=2)

        y_label = ttk.Label(self.data['elements']['settings_notebook'], text='Y:')
        self.data['elements']['y_label'] = y_label
        y_label.grid(column=1, row=3)

        y_spinbox = ttk.Spinbox(self.data['elements']['settings_notebook'])
        self.data['elements']['y_spinbox'] = y_spinbox
        y_spinbox.grid(column=2, row=3)

        width_label = ttk.Label(self.data['elements']['settings_notebook'], text='Width:')
        self.data['elements']['width_label'] = width_label
        width_label.grid(column=1, row=4)

        width_spinbox = ttk.Spinbox(self.data['elements']['settings_notebook'])
        self.data['elements']['width_spinbox'] = width_spinbox
        width_spinbox.grid(column=2, row=4)

        height_label = ttk.Label(self.data['elements']['settings_notebook'], text='Height:')
        self.data['elements']['height_label'] = height_label
        height_label.grid(column=1, row=5)

        height_spinbox = ttk.Spinbox(self.data['elements']['settings_notebook'])
        self.data['elements']['height_spinbox'] = height_spinbox
        height_spinbox.grid(column=2, row=5)

        delete_button = ttk.Button(self.data['elements']['buttons_frame'], text='Delete', command=self.delete)
        self.data['elements']['delete_button'] = delete_button
        delete_button.grid(column=1, row=1)

        save_button = ttk.Button(self.data['elements']['buttons_frame'], text='Save', command=self.saveData)
        self.data['elements']['save_button'] = save_button
        save_button.grid(column=1, row=2)

    def delete(self):
        self.observer.update(self.path, 'programs_list', 'delete')

    def saveData(self):
        self.observer.switchFrame(None)

    def destroyFrame(self):
        self.data['elements']['settings_frame'].destroy()

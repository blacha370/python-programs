from tkinter import ttk


class Component:
    def __init__(self, parent, path, positions=0, observer=object):
        self.observer = observer
        self.path = path
        self.positions = positions
        self.component = ttk.Frame(parent)
        self.component.grid(sticky='WE')
        self.component.columnconfigure(1, weight=1)
        if type(self.positions) == int:
            self.button = ttk.Button(
                self.component, text="Delete", command=self.edit)
            self.button.grid(column=2, row=0, sticky='E')
        elif type(self.positions) == list:
            if len(self.positions) > 1:
                self.amount_label = ttk.Label(
                    self.component, text='x' + str(len(self.positions)), foreground="red")
                self.amount_label.grid(column=0, row=0)
            self.button = ttk.Button(
                self.component, text="Edit", command=self.edit)
            self.button.grid(column=2, row=0, sticky='E')
        self.name_label = ttk.Label(self.component, text=self.path)
        self.name_label.grid(column=1, row=0, sticky='W')
    def edit(self):
        if type(self.positions) == int:
            self.observer.update(self.path, 'pages_list', "delete")
        elif type(self.positions) == list:
            self.observer.switchFrame(self.path)

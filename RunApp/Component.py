from tkinter import ttk


class Component():
    def __init__(self, parent, path, amount=0, observer=object):
        self.observer = observer
        self.path = path
        self.amount = amount
        self.component = ttk.Frame(parent)
        self.component.grid(sticky='WE')
        self.component.columnconfigure(1, weight=1)
        if self.amount > 1:
            self.amount_label = ttk.Label(
                self.component, text='x' + str(amount), foreground="red")
            self.amount_label.grid(column=0, row=0)
        self.name_label = ttk.Label(self.component, text=self.path)
        self.button = ttk.Button(
            self.component, text="Delete", command=self.delete)
        self.name_label.grid(column=1, row=0, sticky='W')
        self.button.grid(column=2, row=0, sticky='E')

    def delete(self):
        if self.amount == 0:
            self.observer.update(self.path, 'pages_list')
        elif self.amount > 0:
            self.observer.update(self.path, 'programs_list')

    def __del__(self):
        pass

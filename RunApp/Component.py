from tkinter import *
from tkinter import ttk


class Component():
    def __init__(self, parent, path, amount=0, observer=True):
        self.observer = observer
        self.path = path
        self.amount = amount
        self.component = ttk.Frame(parent)
        self.component.grid(sticky='E')
        if self.amount > 1:
            self.amount_label = ttk.Label(
                self.component, text='x' + str(amount), foreground="red")
            self.amount_label.grid(column=0, row=0)
        self.name_label = ttk.Label(self.component, text=self.path)
        self.button = ttk.Button(
            self.component, text="Delete", command=self.delete)
        self.name_label.grid(column=1, row=0)
        self.button.grid(column=2, row=0, sticky='E')

    def delete(self):
        self.observer.update(self)
        self.component.destroy()

    def __del__(self):
        pass

from tkinter import *


class FileElement:
    def __init__(self, parent, path, observer):
        self.path = path
        self.observer = observer
        self.encoding = self.get_encoding()

        self.file_frame = Frame(master=parent)
        self.file_frame.grid_columnconfigure(1, weight=1)
        self.file_frame.grid(sticky='WE')

        self.label = Label(master=self.file_frame, text=self.path)
        self.label.grid(column=1, row=1, sticky='E')

        self.delete_btn = Button(master=self.file_frame, text='Usuń', command=self.delete_instance)
        self.delete_btn.grid(column=2, row=1, sticky='E')

    def delete_instance(self):
        self.observer.delete_file(self.path)

    def get_encoding(self):
        with open(self.path, 'r') as file:
            return file.encoding

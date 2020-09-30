from tkinter import *
from tkinter import filedialog
from csvEditor.appModules.FileElement import FileElement
from csvEditor.appModules.Observer import Observer
from csvEditor.appModules.CsvConverter import CsvConverter
import gc


class Gui:
    def __init__(self):
        self.files = set()
        self.observer = Observer(self)
        self.root = Tk()

        self.main_frame = Frame(master=self.root)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.grid(column=1, row=1)

        self.files_frame = Frame(master=self.main_frame, bg='gray', bd=2)
        self.files_frame.grid(column=1, row=1, sticky='N')

        self.options_frame = Frame(master=self.main_frame)
        self.options_frame.grid(column=2, row=1, sticky='N')

        self.delimiter_frame = Frame(master=self.options_frame)
        self.delimiter_frame.grid(column=1, row=1)
        self.delimiter = StringVar()
        self.delimiter.set(',')

        self.comma_delimiter = Checkbutton(master=self.delimiter_frame, variable=self.delimiter, text=',', onvalue=',')
        self.comma_delimiter.grid(column=1, row=1)

        self.semicolon_delimiter = Checkbutton(master=self.delimiter_frame, variable=self.delimiter, text=';',
                                               onvalue=';')
        self.semicolon_delimiter.grid(column=2, row=1)

        self.quoting_frame = Frame(master=self.options_frame)
        self.quoting_frame.grid(column=1, row=2)
        self.quoting = IntVar()

        self.minimal_quoting = Checkbutton(master=self.quoting_frame, variable=self.quoting, text='specjalne'
                                           , onvalue=0)
        self.minimal_quoting.grid(sticky='W')

        self.all_quoting = Checkbutton(master=self.quoting_frame, variable=self.quoting, text='wszystko', onvalue=1)
        self.all_quoting.grid(sticky='W')

        self.numeric_quoting = Checkbutton(master=self.quoting_frame, variable=self.quoting, text='liczby', onvalue=2)
        self.numeric_quoting.grid(sticky='W')

        self.none_quoting = Checkbutton(master=self.quoting_frame, variable=self.quoting, text='nic', onvalue=3)
        self.none_quoting.grid(sticky='W')

        self.btn_frame = Frame(master=self.main_frame)
        self.btn_frame.rowconfigure(1, weight=1)
        self.btn_frame.grid(column=3, row=1, sticky='S')

        self.add_btn = Button(master=self.btn_frame, text='Dodaj plik', command=self.add_file)
        self.add_btn.grid(row=1, stick='WE')

        self.add_btn = Button(master=self.btn_frame, text='Konwertuj', command=self.convert_csv)
        self.add_btn.grid(row=2)

    def create_gui(self):
        self.root.mainloop()

    def add_file(self):
        path = filedialog.askopenfilename()
        print(path)
        if path.endswith('.csv'):
            if path not in self.files:
                self.create_file_element(path)
            self.files.add(path)

    def create_file_element(self, path):
        FileElement(self.files_frame, path, self.observer)

    def remove_file(self, path):
        self.files.remove(path)
        for obj in gc.get_objects():
            if isinstance(obj, FileElement):
                if path == obj.path:
                    obj.file_frame.destroy()
                    del obj

    def convert_csv(self):
        for obj in gc.get_objects():
            if isinstance(obj, FileElement):
                self.files.remove(obj.path)
                CsvConverter.edit_file(obj.path, self.delimiter.get(), self.quoting.get(), obj.encoding)
                obj.file_frame.destroy()
                del obj


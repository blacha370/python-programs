from tkinter import *
from tkinter import filedialog
from csvEditor.appModules.FileElement import FileElement
from csvEditor.appModules.Observer import Observer
from csvEditor.appModules.CsvConverter import CsvConverter
import gc


class Gui:
    def __init__(self):
        self.observer = Observer(self)
        self.root = Tk()

        self.files = set()
        self.quoting = IntVar()
        self.delimiter = StringVar()

        self.main_frame = Frame(master=self.root, bd=2)
        self.files_frame = Frame(master=self.main_frame, bd=2, width=300)
        self.options_frame = Frame(master=self.main_frame)
        self.delimiter_frame = Frame(master=self.options_frame)
        self.delimiter_label = Label(master=self.delimiter_frame, text='Separator:')
        self.comma_delimiter = Checkbutton(master=self.delimiter_frame, variable=self.delimiter, text=',', onvalue=',')
        self.semicolon_delimiter = Checkbutton(master=self.delimiter_frame, variable=self.delimiter, text=';',
                                               onvalue=';')
        self.quoting_frame = Frame(master=self.options_frame)
        self.quoting_label = Label(master=self.quoting_frame, text='Cudzysłów:')
        self.minimal_quoting = Checkbutton(master=self.quoting_frame, variable=self.quoting, text='specjalne'
                                           , onvalue=0)
        self.all_quoting = Checkbutton(master=self.quoting_frame, variable=self.quoting, text='wszystko', onvalue=1)
        self.numeric_quoting = Checkbutton(master=self.quoting_frame, variable=self.quoting, text='liczby', onvalue=2)
        self.none_quoting = Checkbutton(master=self.quoting_frame, variable=self.quoting, text='nic', onvalue=3)
        self.btn_frame = Frame(master=self.main_frame)
        self.add_btn = Button(master=self.btn_frame, text='Dodaj plik', command=self.ask_file_name)
        self.add_many_btn = Button(master=self.btn_frame, text='Dodaj pliki', command=self.ask_files_names)
        self.convert_btn = Button(master=self.btn_frame, text='Konwertuj', command=self.convert_csv)

    def create_gui(self):
        self.configure()
        self.place_elements()
        self.set_variables()
        self.root.mainloop()

    def configure(self):
        self.main_frame.rowconfigure(1, weight=1)
        self.options_frame.columnconfigure(1, weight=1)
        self.delimiter_frame.columnconfigure(1, weight=1)
        self.btn_frame.rowconfigure(1, weight=1)

    def place_elements(self):
        self.main_frame.grid(column=1, row=1)
        self.files_frame.grid(column=1, row=1, sticky='N')
        self.options_frame.grid(column=2, row=1, sticky='N')
        self.delimiter_frame.grid(column=1, row=1, sticky='WE')
        self.delimiter_label.grid(column=1, row=1, columnspan=2, sticky='W')
        self.comma_delimiter.grid(column=1, row=2, sticky='N')
        self.semicolon_delimiter.grid(column=2, row=2, sticky='N')
        self.quoting_frame.grid(column=1, row=2)
        self.quoting_label.grid(sticky='W')
        self.minimal_quoting.grid(sticky='W')
        self.all_quoting.grid(sticky='W')
        self.numeric_quoting.grid(sticky='W')
        self.none_quoting.grid(sticky='W')
        self.btn_frame.grid(column=3, row=1, sticky='S')
        self.add_btn.grid(row=1, stick='WE')
        self.add_many_btn.grid(row=2, stick='WE')
        self.convert_btn.grid(row=3, stick='WE')

    def set_variables(self):
        self.quoting.set(0)
        self.delimiter.set(',')

    def add_file(self, path):
        if path.endswith('.csv'):
            if path not in self.files:
                self.create_file_element(path)
            self.files.add(path)

    def ask_file_name(self):
        path = filedialog.askopenfilename()
        self.add_file(path)

    def ask_files_names(self):
        paths = filedialog.askopenfilenames()
        for path in paths:
            self.add_file(path)

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

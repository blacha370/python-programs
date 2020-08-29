from tkinter import *
from tkinter import ttk
# from tkinter import filedialog
# import win32gui


class Gui:
    def __init__(self):
        self.elements = dict()
        self.root = Tk()
        self.elements['root'] = self.root
        self.root.title("Run")
        self.root.columnconfigure(0, weight=1)

        self.createGuiElement(ttk.Frame, self.elements['root'], 'main_frame')
        self.createGuiElement(ttk.Frame, self.elements['main_frame'], 'data_frame')
        self.createGuiElement(ttk.Combobox, self.elements['data_frame'], 'combobox')
        self.createGuiElement(ttk.Frame, self.elements['main_frame'], 'buttons_frame', position=(1, 0))
        self.createGuiElement(ttk.Button, self.elements['buttons_frame'], 'run_button')

    def createGuiElement(self, widget_type, parent, element_name, args=dict(), position=(0, 0)):
        element = widget_type(parent)
        element.grid(column=position[0], row=position[1])
        self.elements[element_name] = element

    def createGui(self):
        self.root.mainloop()

# s = ttk.Scrollbar(data_frame, orient=HORIZONTAL, command=data_frame.xview)
# data_frame.configure(xscrollcommand=s.set)
# s.grid(column=0, sticky='ns')
#
# http = StringVar()
# http_entry = ttk.Entry(data_frame, width=60,
#                        textvariable=http)
#
# http_entry.grid(column=0, row=1, sticky='we')
#
# pages_frame = ttk.Frame(data_frame, padding='3 3 3 3')
# pages_frame.grid(column=0, row=2, sticky='we')
# pages_frame.columnconfigure(0, weight=1)
# programs_frame = ttk.Frame(data_frame, padding='3 3 3 3')
# programs_frame.grid(column=0, row=3, sticky='e')
#
# # Buttons
# buttons_frame = ttk.Frame(main_frame, padding='3 3 3 3', style='BW.TFrame')
# buttons_frame.grid(column=2, row=1, sticky='nswe')
# buttons_frame.rowconfigure(3, weight=1)
#
# http_links = StringVar()
#
# ttk.Button(buttons_frame, text="Add Page", command=addPage,
#            padding='3 3 3 3').grid(row=1, sticky='nswe')
# ttk.Button(buttons_frame, text="Add Program", style='darkBtn.TButton',
#            command=addProgram, padding='3 3 3 3').grid(row=2, sticky='nswe')
# ttk.Button(buttons_frame, text="Run", command=run,
#            padding='3 3 3 3').grid(row=3, sticky='swe')
#
# # Program options
# def setProgramOptions(monitors):
#     buttons_frame.destroy()
#     settings_frame = ttk.Frame(main_frame, padding = '3 3 3 3', style='BW.TFrame')
#     monitors_spinbox = ttk.Combobox(settings_frame, values=monitors, state="readonly")
#     monitors_spinbox.grid()
#     settings_frame.grid(column=2, row=1, sticky='nswe')
#
# setProgramOptions(app.displays.monitors)

a = Gui()
a.createGui()

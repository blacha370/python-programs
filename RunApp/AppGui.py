from MainFrame import MainFrame
from tkinter import *


class Gui:
    def __init__(self, observer):
        self.observer = observer
        self.programs = set()
        self.pages = set()
        self.root = Tk()
        self.frame = None
        self.root.columnconfigure(0, weight=1)

    def createGui(self, data):
        self.frame = MainFrame(self.root, self.observer, data)
        self.root.mainloop()

    def destroyGui(self):
        self.root.destroy()

from tkinter import *
from MainFrame import MainFrame
from SettingsFrame import SettingsFrame
import time


class Gui:
    def __init__(self, observer):
        self.data = {
            'elements': {
                'root': None}
        }
        self.observer = observer
        self.programs = set()
        self.pages = set()
        self.root = Tk()
        self.data['elements']['root'] = self.root
        self.frame = None
        self.root.columnconfigure(0, weight=1)

    def createGui(self, data):
        self.frame = MainFrame(self.root, self.observer, data)
        self.root.mainloop()

    def swapFrames(self, data):
        frame = self.frame.name
        self.frame.destroyFrame()
        if frame == 'main_frame':
            self.frame = SettingsFrame(self.root, self.observer, data)
        if frame == 'settings_frame':
            self.frame = MainFrame(self.root, self.observer, data)

from AppGui import Gui
from Observer import Observer
from Component import Component
from AppRunner import AppRunner
from Monitors import Monitors
import json
import webbrowser


class App:
    def __init__(self):
        self.runner = AppRunner()
        self.observer = Observer(self)
        self.gui = Gui(self.observer)
        self.gui.createGui(self.runner.data)

    def refresh(self, path, resource_to_update):
        self.runner.remove(resource_to_update, path)
        self.gui.placeComponents(self.runner.data)

app = App()

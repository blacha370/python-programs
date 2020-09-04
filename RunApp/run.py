from AppGui import Gui
from Observer import Observer
from AppRunner import AppRunner
from Opener import Opener


class App:
    def __init__(self):
        self.runner = AppRunner()
        self.observer = Observer(self)
        self.gui = Gui(self.observer)
        self.gui.createGui(self.runner.data)

    def refresh(self, path, resource_to_update, operation):
        if operation == 'add':
            self.runner.add(resource_to_update, path)
        elif operation == 'delete':
            self.runner.remove(resource_to_update, path)
        self.gui.frame.placeComponents(self.runner.data)

    def run(self):
        self.runner.saveData()
        Opener.runOpener(self.runner.data)


app = App()

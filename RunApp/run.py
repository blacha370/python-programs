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
            self.gui.frame.placeComponents(self.runner.data)
        elif operation == 'delete':
            self.runner.remove(resource_to_update, path)
            if self.gui.frame.name == 'settings_frame':
                self.switchFrame(self.runner.data)
            self.gui.frame.placeComponents(self.runner.data)

    def switchFrame(self, data):
        if not data:
            data = self.runner.data
        else:
            for program in self.runner.data['programs_list']:
                if program['path'] == data:
                    data = program
                    break
        self.gui.swapFrames(data)


    def run(self):
        self.runner.saveData()
        Opener.runOpener(self.runner.data)


app = App()

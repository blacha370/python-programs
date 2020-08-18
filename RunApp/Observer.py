

class Observer():
    def __init__(self, runner):
        self.runner = runner

    def update(self, component):
        if component.amount >= 1:
            self.runner.removeProgram(component.path)
        else:
            self.runner.removePage(component.path)
        del component

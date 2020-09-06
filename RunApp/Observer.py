

class Observer:
    def __init__(self, parent):
        self.parent = parent

    def update(self, path, resource_to_update, path_operation):
        self.parent.refresh(path, resource_to_update, path_operation)

    def switchFrame(self, path):
        self.parent.switchFrame(path)

    def run(self):
        self.parent.run()

class Observer:
    def __init__(self, parent):
        self.parent = parent

    def update(self, path, resource_to_update, path_operation, position=tuple(), position_index=0):
        self.parent.refresh(path, resource_to_update, path_operation, list(position), position_index)

    def changePosition(self, path):
        self.parent.openPositionWindow(path)

    def run(self):
        self.parent.run()

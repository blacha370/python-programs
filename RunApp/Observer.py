

class Observer():
    def __init__(self, parent):
        self.parent = parent

    def update(self, path, resource_to_update):
        self.parent.refresh(path, resource_to_update)

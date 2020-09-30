class Observer:
    def __init__(self, parent):
        self.parent = parent

    def delete_file(self, path):
        self.parent.remove_file(path)

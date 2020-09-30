from Gui import Gui


class App:
    def __init__(self):
        self.gui = Gui()


if __name__ == '__main__':
    a = App()
    a.gui.create_gui()

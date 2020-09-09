from Gui import Gui
from Observer import Observer
from ImageEditor import ImageEditor
import os


class App:
    def __init__(self):
        self.logo = str()
        self.dir = str()
        self.images = []
        self.observer = Observer(self)
        self.gui = Gui(self.observer)
        self.gui.createGui()

    def enumerateImages(self):
        self.images.clear()
        images = os.listdir(self.dir)
        self.images = images
        self.gui.createCanvas(self.dir + '/' + self.images[0])

    def run(self, position):
        os.makedirs(self.dir + '/withlogo', exist_ok=True)
        ImageEditor.iterateImages(self.images, self.logo, self.dir, position)
        print('done')


a = App()

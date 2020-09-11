from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image


class Gui:
    def __init__(self, observer):
        self.logo = str()
        self.dir = str()
        self.position = [0, 0]
        self.img_size = int()
        self.observer = observer
        self.root = Tk()

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(sticky="NSWE")

        self.logo_button = ttk.Button(self.main_frame, text='Choose Logo', command=self.chooseLogo)
        self.logo_button.grid(column=1, row=1)

        self.dir_button = ttk.Button(self.main_frame, text='Choose Dir', command=self.chooseDir)
        self.dir_button.grid(column=2, row=1)

        self.run_button = ttk.Button(self.main_frame, text='Run', command=self.run)
        self.run_button.grid(column=3, row=1)

        self.canvas_frame = ttk.Frame(self.main_frame)
        self.canvas_frame.grid(column=1, columnspan=3, row=2, sticky="NSWE")

        self.canvas = Canvas(self.canvas_frame, scrollregion=(0, 0, 0, 0), height=600, width=600)
        self.canvas.grid(sticky="NSWE")
        self.hbar = Scrollbar(self.canvas_frame, orient=HORIZONTAL)
        self.hbar.grid(column=1, row=2, sticky='WE')
        self.hbar.config(command=self.canvas.xview)
        self.vbar = Scrollbar(self.canvas_frame, orient=VERTICAL)
        self.vbar.grid(column=2, row=1, sticky='NS')
        self.vbar.config(command=self.canvas.yview)

        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.canvas.grid(column=1, row=1)

    def createGui(self):
        self.root.mainloop()

    def chooseLogo(self):
        try:
            logo = filedialog.askopenfile(filetype=[('images', '.png .jpg .jpeg .jpe .jfif .exif')]).name
            self.observer.update(fd='l', path=logo)
        except AttributeError:
            return

    def chooseDir(self):
        try:
            dir = filedialog.askdirectory()
            self.observer.update(fd='d', path=dir)
        except AttributeError:
            return

    def run(self):
        self.observer.run(self.position)

    def createCanvas(self, path):
        self.canvas.delete("all")
        photo = Image.open(path)
        self.img_size = photo.size
        image = ImageTk.PhotoImage(photo)
        self.canvas.create_image(0, 0, image=image, anchor=NW)
        self.canvas.configure(scrollregion=(0, 0, self.img_size[0], self.img_size[1]))
        self.canvas.bind("<Button-1>", self.getPosition)
        self.canvas.mainloop()

    def getPosition(self, event):
        position = [
            event.x + (int(self.hbar.get()[0] * self.img_size[0])), int(event.y + (self.vbar.get()[0] * self.img_size[1]))]
        self.position = position

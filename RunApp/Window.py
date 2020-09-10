from tkinter import *
from tkinter import ttk
from Monitors import Monitors


class Window:
    def __init__(self, path, position, index, observer):
        self.path = path
        self.position = position
        self.index = index
        self.observer = observer

        self.root = Tk()
        self.root.geometry(str(self.position[2]) + 'x' + str(self.position[3]))
        self.root.geometry('+' + str(self.position[0] - 8) + '+' + str(self.position[1]))
        self.root.bind("<Configure>", self.getCurrentPosition)
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(sticky='NSWE')

        self.topBtn = ttk.Button(self.mainframe, text='T', command=lambda: self.updatePosition('T'))
        self.topBtn.grid(column=2, row=1)

        self.rightBtn = ttk.Button(self.mainframe, text='R', command=lambda: self.updatePosition('R'))
        self.rightBtn.grid(column=3, row=2, rowspan=2)

        self.bottomBtn = ttk.Button(self.mainframe, text='B', command=lambda: self.updatePosition('B'))
        self.bottomBtn.grid(column=2, row=4)

        self.leftBtn = ttk.Button(self.mainframe, text='L', command=lambda: self.updatePosition('L'))
        self.leftBtn.grid(column=1, row=2, rowspan=2)

        self.canvas = Canvas(self.mainframe)
        self.canvas.grid(column=2, row=2)

        self.save_Btn = ttk.Button(self.mainframe, text='Save position', command=self.savePosition)
        self.save_Btn.grid(column=2, row=3)

    def createWindow(self):
        self.root.mainloop()

    def updatePosition(self, direction):
        monitor = Monitors.checkMonitor(self.root.winfo_x() + 8, self.root.winfo_y() + 8)
        if direction == 'T':
            self.position = [int(monitor[0]), int(monitor[1]), int(monitor[2] - monitor[0]),
                             int(monitor[3]/2)]

        elif direction == 'B':
            self.position = [int(monitor[0]), int((monitor[3] - monitor[1])/2), int(monitor[2] - monitor[0]),
                             int(monitor[3]/2)]

        elif direction == 'R':
            self.position = [int((monitor[0] + monitor[2])/2), int(monitor[1]), int((monitor[2] - monitor[0])/2),
                             int(monitor[3] - monitor[1])]

        elif direction == 'L':
            self.position = [int(monitor[0]), int(monitor[1]), int((monitor[2] - monitor[0])/2),
                             int(monitor[3] - monitor[1])]
        self.moveWindow()

    def moveWindow(self):
        self.root.geometry(str(self.position[2]) + 'x' + str(self.position[3]) + '+' + str(self.position[0] - 8) + '+'
                           + str(self.position[1]))

    def getCurrentPosition(self, _=None):
        for item in self.canvas.find_all():
            self.canvas.delete(item)
        if self.root.winfo_y() < 0:
            self.position = [self.root.winfo_x() + 8, 0, self.root.winfo_width(), self.root.winfo_height()]
        else:
            self.position = [self.root.winfo_x() + 8, self.root.winfo_y(), self.root.winfo_width(),
                             self.root.winfo_height()]
        self.canvas.create_text(50, 50, text=(str(self.path.split('\\')[-1]) + '\nX: ' + str(self.position[0]) +
                                              '\nY: ' + str(self.position[1]) + '\nWidth: ' + str(self.position[2]) +
                                              '\nHeight: ' + str(self.position[3])))

    def savePosition(self):
        self.observer.update(self.path, ['programs_list'], 'position', self.position, self.index)
        self.root.destroy()

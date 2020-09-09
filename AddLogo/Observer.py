class Observer:
    def __init__(self, parent):
        self.parent = parent

    def update(self, fd='', path=''):
        if fd == '' or path == '' or not (fd == 'l' or fd == 'd'):
            print('error')
            return
        elif fd == 'l':
            self.parent.logo = path
        elif fd == 'd':
            self.parent.dir = path
            self.parent.enumerateImages()

    def run(self, position):
        if not self.parent.logo == '' and not self.parent.dir == '':
            self.parent.run(position)
        else:
            return

import webbrowser
import win32process
import win32gui


class Opener:
    @staticmethod
    def runOpener(data):
        Opener.runPrograms(data['programs_list'])
        Opener.runPages(data['pages_list'])

    @staticmethod
    def enumWindows(hwnd, hwnd_list):
        hwnd_list.append(win32gui.GetWindowText(hwnd))

    @staticmethod
    def searchWindow(hwnd, hwnd_list):
        if win32gui.GetWindowText(hwnd) not in hwnd_list['current']:
            if hwnd not in hwnd_list['new']:
                hwnd_list['new'].append(hwnd)

    @staticmethod
    def runPrograms(programs):
        windows = {'current': [], 'new': [], 'amount': 0}
        win32gui.EnumWindows(Opener.enumWindows, windows['current'])
        for program in programs:
            for _ in program['positions']:
                startupinfo = win32process.STARTUPINFO()
                win32process.CreateProcess(program['path'], None, None, None, 0, 0, None, None, startupinfo)
                windows['amount'] += 1
            while len(windows['new']) < windows['amount']:
                win32gui.EnumWindows(Opener.searchWindow, windows)
        for _ in windows['new']:
            i = 0
            for program in programs:
                for position in program['positions']:
                    win32gui.MoveWindow(windows['new'][i], position[0], position[1], position[2], position[3], 1)
                    i += 1

    @staticmethod
    def runPages(pages):
        for page in pages:
            webbrowser.open_new_tab(page)


import webbrowser
import win32process


class Opener:
    @staticmethod
    def runOpener(data):
        Opener.runPages(data['pages_list'])
        Opener.runPrograms(data['programs_list'])

    @staticmethod
    def enumWindows(hwnd, hwnd_list: list()):
        hwnd_list.append(win32process.GetWindowThreadProcessId(hwnd))

    @staticmethod
    def runPrograms(programs):
        for program in programs:
            for _ in range(program['amount']):
                startupinfo = win32process.STARTUPINFO()
                win32process.CreateProcess(program['path'], None, None, None, 0, 0, None, None, startupinfo)

    @staticmethod
    def runPages(pages):
        for page in pages:
            webbrowser.open_new_tab(page)


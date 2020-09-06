import win32api


class Monitors:
    @staticmethod
    def getMonitors():
        displays = win32api.EnumDisplayMonitors()
        monitors = list()
        for display in displays:
            monitors.append((display[0], display[2]))
        return monitors

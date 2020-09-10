import win32api


class Monitors:
    @staticmethod
    def getMonitors():
        displays = win32api.EnumDisplayMonitors()
        monitors = list()
        for display in displays:
            monitors.append(win32api.GetMonitorInfo(display[0])['Work'])
        return monitors

    @staticmethod
    def checkMonitor(x, y):
        monitors = Monitors.getMonitors()
        for monitor in monitors:
            if monitor[0] <= x < monitor[2] and monitor[1] <= y < monitor[3]:
                return monitor
            elif x < monitor[0]:
                return monitor
            return monitor[0]

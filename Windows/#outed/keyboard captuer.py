from pyHook import HookManager
from win32gui import PumpMessages, PostQuitMessage

class Keystroke_Watcher(object):
    def __init__(self):
        self.hm = HookManager()
        self.hm.KeyDown = self.on_keyboard_event
        self.hm.HookKeyboard()





watcher = Keystroke_Watcher()
PumpMessages()
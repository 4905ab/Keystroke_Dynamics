import pyHook
from datetime import time
import pythoncom


def OnKeyboardEvent(event):
    start = time.time()
    print('Ascii:', event.Ascii, chr(event.Ascii))
    end = (time.time() - start)
    print(end)

    return True

hooks_manager = pyHook.HookManager()
hooks_manager.Keydown = OnKeyboardEvent
hooks_manager.HookManager()
pythoncom.PumpMessages()

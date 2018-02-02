import pythoncom, pyHook, time

def onkeyboardevent(event):
    start = time.time()
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    end = (time.time() - start)
    print end

    return True

hooks_manager = pyHook.HookManager()
hooks_manager.Keydown = onkeyboardevent()
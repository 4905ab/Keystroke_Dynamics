from pyHook import HookManager
from  win32gui import PumpMessages, PostQuitMessage
import datetime ,time

class wait_untill(object):
        def wait_until(somepredicate, timeout, period=0.0001, *args, **kwargs):
            mustend = time.time() + timeout
            whilst
            time.time() < mustend:
            if somepredicate(*args, **kwargs): return True
            time.sleep(period)
        return False


class Keystroke_Watcher(object):
   def __init__(self):
        #decering keyboard hook and up down key varibles
        self.hm = HookManager()
        self.xkeydowntim = float
        self.xkeyuptim = float
        self.ykeydowntim = float
        self.ykeyuptim = float
        self.hm.HookKeyboad
    def mstime(self):
        #settup time to the Ms
        self.dt = datetime.now()
        # to call time in ms use dt.microsecond

    def areyoukd(self): #are you the kd metric
        for self.hm.KeyDown #looks at the first key pree
            dt.microsecond = self.xkeydowntim
            self.hm.KeyChar = self.xkeydownasci
        for self.hm.KeyUp
            dt.microsecond = self.xkeyuptim
            self.hm.KeyChar = xkeyupasci
        if xkeyuptim < xkeydowntim && xkeydownasci == xkeyupasci:
            xkeyuptim - xkeydowntim = global.kdmetric
        else:break

PumpMessages(ks)
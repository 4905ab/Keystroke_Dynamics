from pyHook import HookManager
import datetime

"""
class Wait_untill(object):
        def wait_until(somepredicate, timeout, period=0.0001, *args, **kwargs):
            mustend = time.time() + timeout
            whilst
            time.time() < mustend:
            if somepredicate(*args, **kwargs): return True
            time.sleep(period)
        return False
"""

def deltatime():
    import datetime as dt
    now = dt.datetime.now()
    delta = dt.timedelta(hours=12)
    t = now.time()
    print(t)
    # 12:39:11.039864

    print((dt.datetime.combine(dt.date(1, 1, 1), t) + delta).time())

    # 00:39:11.039864
    # added the barrkets to the code in this block only see if it does somthing - news it breaks it as not funcations but events


class Keystroke_Watcher(object):
    #decering keyboard hook and up down key varibles
    hm = HookManager()
    hm.HookKeyboad

    #int of the time variable for use in delta time
    x_keydown_tim = float
    x_keyup_tim = float
    y_keydown_tim = float
    y_keyup_tim = float

    # int of the asci varible
    x_key_down_asci = int
    x_keyup_asci = int
    y_keydown_asci = int
    y_keyup_asci = int

    #int time#
    #settup time to the Ms and micro second

    dt_mil = datetime.milliseconds
    dt_mic = datetime.microsecond

    # the if if statements are what calls a key stroke a metric that means if i have an if list i can stop repeting myself and make its simpler
    if hm.KeyDown:  # dk metric
        dt_mil = x_keydown_tim
        hm.KeyChar = x_key_down_asci
        hm.KeyUp
        dt_mil = x_keyup_tim
        hm.KeyChar = x_keyup_asci
        if x_keyup_tim < x_keydown_tim and x_key_down_asci == x_keyup_asci:  # if for kd
           kd_metric =(x_keyup_tim - x_keydown_tim)
           print kd_metric

    elif hm.KeyDown: # ddkl metric
        dt_mil = x_keydown_tim
        hm.KeyChar = x_key_down_asci
        hm.KeyDown
        dt_mil = y_keydown_tim
        hm.KeyChar = y_keydown_asci
        if y_keydown_tim < x_keydown_tim and x_key_down_asci != y_keydown_asci:
            ddkl_metric = (x_keydown_tim - y_keydown_tim)
            print ddkl_metric

    elif hm.KeyDown: # dukl metric
        dt_mil = x_keydown_tim
        hm.KeyChar = x_key_down_asci
        hm.KeyUp
        dt_mil = y_keyup_tim
        hm.KeyChar = y_keyup_asci
        if y_keyup_tim < x_keydown_tim and x_key_down_asci != y_keyup_asci:
           dukl_metric = (x_keyup_tim - y_keydown_tim)
           print dukl_metric

    elif hm.KeyUp:  # are you the udkl metric
        dt_mil = x_keyup_tim
        hm.KeyChar = x_keyup_asci
        hm.KeyDown
        dt_mil = y_keydown_tim
        hm.KeyChar = y_keydown_asci
        if y_keydown_tim < x_keyup_tim and x_key_down_asci != y_keyup_asci:
            udl_metric =(x_keyup_tim - y_keydown_tim)
            print udl_metric

    elif hm.KeyUp: # are you the uukl metric - might break
        dt_mil = x_keyup_tim
        hm.KeyChar = x_keyup_asci
        hm.KeyUp
        dt_mil = y_keyup_tim
        hm.KeyChar = y_keyup_asci
        if x_keyup_tim < y_keyup_tim and x_keyup_asci == y_keyup_asci:
            uukl_metric= (x_keyup_tim - y_keyup_tim)
            print uukl_metric





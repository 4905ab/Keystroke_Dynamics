import keyboard
import zope
#here for the documents  http://zopeevent.readthedocs.io/en/latest/
from datetime import datetime
from keyboard import KeyboardEvent


# making empty dicts for use outside of defs
kdown_dict = {}
kup_dict = {}

# making global variables
scancode_keydown = int
scancode_keyup = int
DDKL = float
KD = float
DUKL = float
UDKL = float
UUKL = float


"""" adding the the key name and the key time to a dict with a split on weather it was a """
def on_keyboard_first_press(event):
    try:
        if event.keyboard.KEY_DOWN():
            scancode = KeyboardEvent.scan_code
            #dt = datetime.microsecond
            keyboardtime = KeyboardEvent.time
            kdown_dict[scancode: keyboardtime]
        if event.keyboard.KEY_UP():
            scancode = KeyboardEvent.scan_code
            #dt = datetime.microsecond
            keyboardtime = KeyboardEvent.time
            kup_dict[scancode: keyboardtime]
    finally:
        return True


"""looking in the dict after its been pressed"""
def on_keyboard_second_press_down(event):
        if event.keyboard.KEY_DOWN() != kdown_dict.get(scancode_keydown):
            DDKL = 'return kdown_dict.get(scancode_keydown) - datetime.microsecond'
            x = kdown_dict.get('scancode_keydown', kdown_dict.get('DDKL',))
            #filename = open(filename, 'a')
            #filename.write(x + '\n')
            #filename.close()
            print(x)
"""
        if event.keyboard.KEY_UP(): == kdown_dict.get(scancode_keydown) :
            return kdown_dict.get(scancode_keydown) - datetime.microsecond = KD
            for key, in kdown_dict.iteritems(scancode_keydown):
                file.write(key, KD\n)

        if event.keyboard.KEY_UP(): != kdown_dict.get(scancode_keydown) :
            return kdown_dict.get(scancode_keydown) - datetime.microsecond = DUKL
            for key, in kdown_dict.iteritems(scancode_keydown):
                file.write(key, DUKL\n)

        

def on_keyboard_second_press_up(event):
    try:
        if event.keyboard.KEY_DOWN() != kdown_dict.get(scancode_keyup) :
            return kdown_dict.get(scancode_keyup) - datetime.microsecond = UDKL
            for key, in kdown_dict.iteritems(scancode_keyup):
                file.write(key, UDKL\n)
        if event.keyboard.KEY_UP(): != kdown_dict.get(scancode_keyup) :
            return kdown_dict.get(scancode_keyup) - datetime.microsecond = UUKL
            for key, in kdown_dict.iteritems(scancode_keyup):
                file.write(key, UUKL\n)
    finally:
        return True
"""




if __name__ == '__main__':
    keyboard.hook(callback=on_keyboard_first_press(event))
    print(DDKL)

def shutdown(self):
    PostQuitMessage(0)
    UnhookKeyboard()


# Assisted By KnowNexus
import time
import keyboard
from datetime import datetime

# making global variables

# scancode = int
# keyboardtime = float
# DDKL = float
# KD = float
# DUKL = float
# UDKL = float
# UUKL = float

# function for first key press
# def first_key_down(event):
# print("hello idiot")

# keyboard.hook(callback=get_event_data)

# looking in the dict after its been pressed
"""
    if (KEY_DOWN == 'down' and (get_scan_code_time(scancode) != kdown_dict.get('scancode'))):
        # KEY_DOWN = Down arrow key
        DDKL = kdown_dict.get('scancodekey') - datetime.microsecond
        #filename = open(filename, 'a')
        #filename.write(x + '\n')
        #filename.close()s
        print("DDKL " + DDKL)

    if (KEY_UP == 'up' and (get_scan_code_time(scancode) == kdown_dict.get('scancodekey'))):
        KD = kdown_dict.get('scancodekey') - datetime.microsecond
        #for key, in kdown_dict.iteritems(scancode_keydown):
           # file.write(key, KD\n)
        print("KD " + KD)

    if (KEY_UP == 'up' and (get_scan_code_time(scancode) != kdown_dict.get('scancodekey'))):
        DUKL = kdown_dict.get('scancodekey') - datetime.microsecond
        # for key, in kdown_dict.iteritems(scancode_keydown):
        #file.write(key, DUKL\n)
        print("DUKL " + DUKL)
"""

"""
def first_key_up(event):        
    print("hello idiot")
    keyboard.hook(callback=get_scan_code)
    keyboardtime = event.time
    kup_dict[scancode: keyboardtime]
    print(scancode)
    scancode = 0

#looking in the dict for the second relace

    if event.KEY_DOWN() != kup_dict.get(scancode) :
            UDKL = kdown_dict.get('scancodeevent) - datetime.microsecond
            #for key, in kdown_dict.iteritems(scancode_keyup):
                #file.write(key, UDKL\n)
            print(UDKL)
            
    if event.KEY_UP() != kup_dict.get(scancode_keyup) :
        UUKL = kdown_dict.get(scancode_keyup) - datetime.microsecond
        #for key, in kdown_dict.iteritems(scancode_keyup):
            #file.write(key, UUKL\n)
        print(UUKL)


"""


def test(event):
    print()
    # print(event)
    # print(event.scan_code)
    # print(event.keyboard.KEY_DOWN)
    # print(event.KEY_DOWN)
    # print(keyboard.KeyboardEvent)
    # print(event.event_type)

def menu():
    ans = True
    while ans:
        global which_word
        print("""Welcome to the alex benett keystroke dynamics program
        
        Press y if you agree for the data provided in this survey to be used for the purpose of final year project
        
        Press n if you don't want to take part of this survey
        """)
        ans = input("y/n")
        if ans == "y":
            print("\n Thank you")
            global name
            global age
            global computer_literate
            global which_word
            name = input("\n Whats your name")
            age =  input("\n whats your age")
            computer_literate = input("\n on a scale of 1 to 10 how computer literate do you consider yourself to be")
            print("\n please type out the first word then press enter")
            which_word = 0
            ans = False
        elif ans == "n":
            print("\n Goodbye")
        elif ans != "":
            print("\n Not Valid Choice Try again")

def get_event_data(event):
    scan_code = event.scan_code
    keyboard_time = event.time
    event_type = event.event_type
    global kdown_dict
    global which_word
    # add keydown event to dict
    # If key down and not already down
    if (event_type == "down") and not kdown_dict.get(scan_code):
        # sudo       if(dict is not empty):
        # sudo           ddkl
        kdown_dict.update({scan_code: keyboard_time})

    # If key up and in dict
    # Create metric KD
    # Remove entry from dict
    if event_type == "up":
        # dukl section
        # sudo       if (key up and dict contains more than 1 thing):
        # sudo           dukl
        # kd section
        KD = (kdown_dict.get(scan_code) - datetime.now().microsecond)
        #print("KD: {}".format(KD))
        # locates output dir
        # opens file
        # writes KD metric to file
        path = 'OutputData/KD.txt'
        with open(path, 'a') as KD_file:
            #make the vars smaller so they fit in the line
            n = name
            a = age
            c = computer_literate
            w = which_word
            KD_file.write("n: {} a: {} c: {} w: {} KD: {}\n".format(n, a, c, w, KD))
            #"name: {} age: {} computer_literate: {} which_word:{} KD: {}\n"
            KD_file.close()
        # del scancode from dict
        del kdown_dict[scan_code]
    if event.scan_code == 28 and event_type == "up":
        which_word += 1
        print("\n Please type out the next work on the list")



if __name__ == '__main__':
    menu()
    kdown_dict = {}
    #keyboard.hook(callback=test)
    keyboard.hook(callback=get_event_data)
    keyboard.wait()

    # keyboard.unhook_all()

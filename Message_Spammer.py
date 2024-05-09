import pyautogui as pt
import time
import keyboard as key


rmodetoggle = False


def def_factors():
    if pt.confirm('Select mode:', buttons=['Rant', 'Normal']) == 'Rant':
        return rantmode()
    else:
        pass
    global amount
    amount = pt.prompt('Enter the limit:')
    if amount is not None:
        pass
    else:
        exit()
    global paste_clip
    paste_clip = pt.confirm('Do you want to paste the most recently copied item?(Ctrl + V) It is recommended to use '
                            'this option for faster and more reliable spamming.')
    if paste_clip == 'OK':
        return confirmprompt()
    else:
        pass
    global message
    message = pt.prompt('Enter the message:')
    if message is not None:
        confirmprompt()
    else:
        exit()


def rantmode():
    global rmodetoggle
    rmodetoggle = True
    rant = pt.prompt('Enter your rant:')
    if rant is not None:
        pass
    else:
        exit()
    global splitrant
    splitrant = rant.split()
    confirmpromptrmode()


def confirmprompt():
    if paste_clip != 'OK':
        prompt = pt.confirm(
            'Please make sure that when you press enter the message is sent before continuing. NOTE: This '
            'will move your mouse back and forth to optimize input. YOU CAN '
            'STOP AT ANY TIME BY MOVING '
            'YOUR MOUSE TO ANY CORNER OF YOUR SCREEN.')
    else:
        prompt = pt.confirm(
            'Please make sure that when you press enter the message is sent before continuing. YOU CAN '
            'STOP AT ANY TIME BY MOVING '
            'YOUR MOUSE TO ANY CORNER OF YOUR SCREEN.')
    if prompt == 'OK':
        spam_init()
    else:
        exit()


def confirmpromptrmode():
    prompt = pt.confirm('Please make sure that when you press enter the message is sent before continuing. NOTE: This '
                        'will move your mouse back and forth to optimize input. YOU CAN STOP AT ANY TIME BY MOVING '
                        'YOUR MOUSE TO ANY CORNER OF YOUR SCREEN.')
    if prompt == 'OK':
        rmode_init()
    else:
        exit()


def spam_init():
    i = 0
    if paste_clip != 'OK':
        b = 0
        time.sleep(2)
        while i < int(amount):
            if len(message) <= 10:
                if b == 0:
                    pt.moveTo(806, 554, 0.3)
                    pt.typewrite(message)
                    pt.press('enter')
                    i += 1
                    b = 1
                    continue
                else:
                    pt.moveTo(1139, 437, 0.3)
                    pt.typewrite(message)
                    pt.press('enter')
                    i += 1
                    b = 0
                    continue
            else:
                if b == 0:
                    pt.moveTo(806, 554, 0.5)
                    pt.typewrite(message)
                    pt.press('enter')
                    i += 1
                    b = 1
                    continue
                else:
                    pt.moveTo(1139, 437, 0.5)
                    pt.typewrite(message)
                    pt.press('enter')
                    i += 1
                    b = 0
                    continue
        pt.moveTo(900, 600, 0.3)
    else:
        time.sleep(2)
        while i < int(amount):
            pt.hotkey('ctrl', 'v')
            pt.press('enter')
            i = i + 1


def rmode_init():
    time.sleep(2)
    a = 0
    try:
        global splitrant
        for words in splitrant:
            if a == 0:
                a = 1
                pt.moveTo(806, 554, 0.3)
                key.write(words)
                key.press('enter')
                continue
            else:
                a = 0
                pt.moveTo(1139, 437, 0.3)
                key.write(words)
                key.press('enter')
                continue
    except:
        pt.alert("An error has ocurred. this also shows up when you move your mouse to the corner.")
        exit()
    pt.moveTo(900, 600, 0.3)


def_factors()
while True:
    prompt2 = pt.confirm('Rerun with current parameters?')
    if prompt2 == 'OK':
        if rmodetoggle:
            confirmpromptrmode()
        else:
            confirmprompt()
    else:
        exit()

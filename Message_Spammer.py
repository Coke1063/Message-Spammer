import pyautogui as pt
import time
import keyboard as key


def def_factors():
    if pt.confirm('Would you like to enable rant mode?') == 'OK':
        rantmode()
        return
    else:
        pass
    global amount
    amount = pt.prompt('Enter the limit:')
    if amount is not None:
        pass
    else:
        exit()
    global paste_clip
    paste_clip = pt.confirm('Do you want to paste the most recently copied item?(ctrl + v)')
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
    rant = pt.prompt('Enter your rant:')
    if rant is not None:
        pass
    else:
        exit()
    global splitrant
    splitrant = rant.split()
    confirmpromptrmode()


def confirmprompt():
    prompt = pt.confirm('Please make sure that when you press enter the message is sent before continuing.')
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
        time.sleep(2)
        while i < int(amount):
            pt.typewrite(message)
            pt.press('enter')
            i += 1
    else:
        time.sleep(2)
        while i < int(amount):
            pt.hotkey('ctrl', 'v')
            pt.press('enter')
            i = i + 1


def rmode_init():
    time.sleep(2)
    global a
    a = 0
    for words in splitrant:
        if a == 0:
            a = 1
            pt.moveTo(806, 554, 0.5)
            key.write(words)
            key.press('enter')
            continue
        else:
            a = 0
            pt.moveTo(1139, 437, 0.5)
            key.write(words)
            key.press('enter')
            continue


def_factors()
while True:
    prompt2 = pt.confirm('Rerun with current parameters? Only works in non-rant mode.')
    if prompt2 == 'OK':
        spam_init()
    else:
        exit()
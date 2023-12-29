import pyautogui as pt
import time


def def_factors():
    global amount
    amount = pt.prompt('Enter the limit:')
    if amount is not None:
        pass
    else:
        exit()
    global paste_clip
    paste_clip = pt.confirm('Do you want to paste the most recently copied item?')
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


def confirmprompt():
    prompt = pt.confirm('Please make sure that when you press enter the message is sent before continuing. YOU CAN '
                        'STOP SPAMMING BY MOVING THE CURSOR TO ANY CORNER OF YOUR SCREEN.')
    if prompt == 'OK':
        spam_init()
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


def_factors()
while True:
    prompt2 = pt.confirm('Rerun with current parameters?')
    if prompt2 == 'OK':
        spam_init()
    else:
        def_factors()

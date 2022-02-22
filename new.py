import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)


def random_response(list):
    position=pt.locateOnScreen('type_message.png', confidence=.9)
    x=position[0]
    y=position[1]
    pt.moveTo(x,y)
    pt.click()
    for word in list:
        message=f'Your message:{word}'
        pt.typewrite(message)
        pt.typewrite('\n')
        sleep(0.4)
    message='This is a python script in testing mode...'
    pt.typewrite(message)
    pt.typewrite('\n')
    sleep(.2)
    x-=500
    pt.moveTo(x,y)
    pt.click()


def get_new_message():
    position=pt.locateCenterOnScreen('unread_messages.png', confidence=.5)
    sleep(0.1)
    x=position[0]
    y=position[1]
    pt.moveTo(x,y)
    y+=48
    x-=384
    list=[]
    while y<652:
        pt.moveTo(x,y)
        sleep(0.1)
        pt.tripleClick()
        sleep(0.1)
        pt.hotkey('ctrl', 'c')
        sleep(0.1)
        if pyperclip.paste():
            list.append(pyperclip.paste())
            sleep(0.1)
        y+=32
    return list

         


def get_green_circle():
    position=pt.locateOnScreen('message.png', confidence=.7)
    pt.moveTo(position[0],position[1])
    pt.click()
    sleep(0.4)



while True:
    try:
        get_green_circle()
        message=get_new_message()
        random_response(message)


    except:
        print('No new messages!')
    sleep(4)  

import sys
import os
import math
from pynput import mouse
from pynput import keyboard
import pyautogui

sys.path.append("./real-hacks")
import doMath

gridByCount = []

pyautogui.PAUSE = 0.020

clix = 0
topLeft, topRight, bottomLeft, bottomRight = [], [], [], []

def start():
    global gridByCount
    gridByCount = doMath.gridMath(topLeft, topRight, bottomLeft, bottomRight)[0]
    print(gridByCount)
    pyautogui.press("1")
    pyautogui.press("T")
    for pos in gridByCount:
        print("place")
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click()
    os._exit(0)

def on_press(key):
    if key == keyboard.Key.esc:
        print("ESC pressed! Exitting...")
        os._exit(0)

print("cotl")
clix = 0
def on_click(x, y, button, pressed):
    global clix
    global topLeft
    global topRight
    global bottomLeft
    global bottomRight
    if button == mouse.Button.left:
        if clix == 0:
            topLeft = (x, y)
            print("cotr")
        elif clix == 2:
            topRight = (x, y)
            print("cobl")
        elif clix == 4:
            bottomLeft = (x, y)
            print("cobr")
        elif clix == 6:
            bottomRight = (x, y)
            print("starting")
            start()
    clix += 1

with mouse.Listener(on_click=on_click) as listener:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


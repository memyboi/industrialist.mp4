import sys
import os
import math
import cv2
import numpy
from pynput import mouse
from pynput import keyboard
import pyautogui
import time

# clearFrame() wasn't working lol
# had to debug *somehow*

sys.path.append("./real-hacks")
import doMath

gridByCount = []

pyautogui.PAUSE = 0.020
pyautogui.FAILSAFE = False

clix = 0
topLeft, topRight, bottomLeft, bottomRight = [], [], [], []

def removeTool():
    pyautogui.PAUSE = 0.02
    pyautogui.press("4")

#def clearFrame():
#    removeTool()
#    pyautogui.PAUSE = 0.2
#    pyautogui.move(topLeft[0]+3, topLeft[1]+3)
#    pyautogui.doubleClick()
#    time.sleep(0.025)
#    pyautogui.mouseDown()
#    pyautogui.move(bottomRight[0]-3, bottomRight[1]-3)
#    pyautogui.mouseUp()
#    time.sleep(1)

def clearFrame():
    removeTool()
    pyautogui.PAUSE = 0.1
    pyautogui.moveTo(topLeft[0]+3, topLeft[1]+3)
    pyautogui.mouseDown()
    pyautogui.moveTo(bottomRight[0]-3, bottomRight[1]-3)
    pyautogui.mouseUp()
    pyautogui.press("#");
    pyautogui.press("right");
    pyautogui.press("right");
    pyautogui.press("enter");
    pyautogui.press("#");

def start():
    global gridByCount
    gridByCount = doMath.gridMath(topLeft, topRight, bottomLeft, bottomRight)[0]
    print(gridByCount)
    clearFrame()
    os.system("hyprshot -m output -c -o ./ -f cleartest.png")
    #pyautogui.screenshot("./positioning.png")
    maths = doMath.gridMath(topLeft, topRight, bottomLeft, bottomRight)
    grid = maths[0]
    debug = maths[1]
    print(debug)
    img = cv2.imread("./cleartest.png")
    cv2.line(img, (topLeft[0]+3, topLeft[1]+3), (bottomRight[0]-3, bottomRight[1]-3), (0, 255, 0), thickness=2)
    #res = calcPositions()
    img = cv2.circle(img, (topLeft[0]+3, topLeft[1]+3), 3, (0, 255, 255), 1)
    img = cv2.circle(img, (bottomRight[0]-3, bottomRight[1]-3), 3, (0, 255, 255), 1)
    cv2.imwrite("./cleartest.png", img)

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


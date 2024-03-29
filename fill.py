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
    os.system("hyprshot -m output -c -o ./ -f positioningtest.png")
    #pyautogui.screenshot("./positioning.png")
    maths = doMath.gridMath(topLeft, topRight, bottomLeft, bottomRight)
    grid = maths[0]
    debug = maths[1]
    print(debug)
    img = cv2.imread("./positioningtest.png")
    cv2.line(img, (topLeft[0], topLeft[1]), (bottomLeft[0], bottomLeft[1]), (0, 255, 0), thickness=2)
    cv2.line(img, (topLeft[0], topLeft[1]), (topRight[0], topRight[1]), (0, 255, 0), thickness=2)
    cv2.line(img, (bottomRight[0], bottomRight[1]), (topRight[0], topRight[1]), (0, 255, 0), thickness=2) 
    cv2.line(img, (bottomLeft[0], bottomLeft[1]), (bottomRight[0], bottomRight[1]), (0, 255, 0), thickness=2) 
    #res = calcPositions()
    img = cv2.circle(img, (int(debug[2][0]), int(debug[2][1])), 3, (0, 255, 255), 1)
    img = cv2.circle(img, (int(debug[3][0]), int(debug[3][1])), 3, (0, 255, 255), 1)
    img = cv2.circle(img, (int(debug[4][0]), int(debug[4][1])), 3, (0, 255, 255), 1)
    img = cv2.circle(img, (int(debug[5][0]), int(debug[5][1])), 3, (0, 255, 255), 1)
    for point in grid:
        #print(point)
        img = cv2.circle(img, (int(point[0]), int(point[1])), 3, (0, 0, 255), 1)
    cv2.imwrite("./positioningtest.png", img)

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


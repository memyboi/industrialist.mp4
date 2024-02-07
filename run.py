# do les macrolession
# made in late jan 2024, whereas other files made in late november 2023
# dont ask why i took so long
# thats also why this code is "cleaner"

# might work on windows, if not, oh well its just a silly script anyway
# its made to work on linux (on wayland)
# cuz thats the os i use lol
# i use arch btw
# idfk

# this is awful code lmao
# do not use this at all
# in gen alpha terms:
# the ohio skibidi toilet sigmas do not grimace this gyatted code
# (what the fuck did i just write)

# these comments are proof that i need serious therapy

#      _                            _
#     (_)_ __ ___  _ __   ___  _ __| |_ ___
#     | | '_ ` _ \| '_ \ / _ \| '__| __/ __|
#     | | | | | | | |_) | (_) | |  | |_\__ \
#     |_|_| |_| |_| .__/ \___/|_|   \__|___/
#                 |_|
import pyautogui
import pyscreenshot
import os
import sys
from pynput import mouse
from pynput import keyboard
from tkinter import messagebox
import time
from PIL import Image
import cv2
import math
sys.path.append("./real-hacks") # hax omg !11! cheetah !11!1!!1
import doMath # jk its just math (math jumpscare)

#                       __ _
#       ___ ___  _ __  / _(_) __ _
#      / __/ _ \| '_ \| |_| |/ _` |
#     | (_| (_) | | | |  _| | (_| |
#      \___\___/|_| |_|_| |_|\__, |
#                            |___/
screenshottingState = 0
    # 0 - use pyscreenshot (linux (wayland, x11), osx, windows)
    # 1 - use grimblast (linux wayland, grimblast needs to be installed),
    # 2 - use pyautogui.screenshot(linux (x11 only), osx, windows)
gui = True # enable/disable gui
placespeed = 0.020 # how fast pipes are placed
massremovepadding = 3 # how much padding to add to the mass delete feature
diffthreshold = 50 # the percentage of similarities needed to use difference rendering.
    # 0 (or below) would mean all renders but the first are diff renders
    # 100 (or above) would mean all renders are full renders.
output_folder = "./rendered" # where the images are placed after being rendered, may need changing on non unix (windows) platforms
input_folder = "./processed" # input files, make sure it only consists of .jpg files numbered from 0-${frame count}, may need changing on non unix (windows) platforms
intermission = 0 # number of seconds before playing starts, after initialisation.
switch = 1 # set to 1 by default cuz i recommend using white pipes
    # 0 - place pipe when pixel is black, leave white pixels alone
    # 1 - place pipe when pixel is white, leave black pixels alone

pyautogui.FAILSAFE = False

#                       _   _
#      _ __ _   _ _ __ | |_(_)_ __ ___   ___
#     | '__| | | | '_ \| __| | '_ ` _ \ / _ \
#     | |  | |_| | | | | |_| | | | | | |  __/
#     |_|   \__,_|_| |_|\__|_|_| |_| |_|\___|

clix = 0
topLeft = []
topRight = []
bottomLeft = []
bottomRight = []

gridByCount = []

X = 0
Y = 1

renderTypes = {
    "Full": 0,
    "Difference": 1,
}

def takeScreenshot(filename):
    if screenshottingState == 0:
        im = ImageGrab.grab()
        im.save(output_folder+"/"+str(filename))
    elif screenshottingState == 1:
        os.system("grimblast --freeze save output "+output_folder+"/"+str(filename))
    elif screenshottingState == 2:
        pyautogui.screenshot(output_folder+"/"+str(filename))
    else:
        print("ERROR - invalid config 'screenshottingState'!\nClosing due to not being able to save renders.")
        os._exit(0)

def start():
    print("Setup complete!")
    time.sleep(intermission)
    print("Playing!")

    global gridByCount
    gridByCount = doMath.gridMath(topLeft, topRight, bottomLeft, bottomRight)[0]

    frames = os.listdir(input_folder)

    lastData = []
    currentData = []
    count = 0

    while count < len(frames):
        currentData, currentImage = scanImage(str(count)+".jpg")
        if lastData == []:
            # is first frame
            renderFrame(renderTypes["Full"], currentData, currentImage, lastData)
        elif lastData != currentData:
            # is not equal frame, perform other operations
            renderFrame(depictRenderType(lastData, currentData), currentData, currentImage, lastData)
        # if is equal frame, will skip all other rendering attempts and just take a screenshot.

        takeScreenshot(str(count)+".jpg")
        lastData = currentData
        count+=1
    
    print("Rendering complete!")
    os._exit(0)

def renderFrame(renderType, currentdata, currentImage, lastdata):
    if renderType == renderTypes["Full"]:
        clearFrame()
        buildTool()
        pyautogui.PAUSE = placespeed
        global gridByCount
        global switch
        count = 0
        drawn = 0
        for bit in currentdata:
            print(str(count)+' / '+str(len(currentdata))+' pixels checked!', end='\r')
            if bit == switch:
                pos = gridByCount[count]
                pyautogui.moveTo(pos[0], pos[1])
                pyautogui.click()
                drawn += 1
            count += 1
        print("All "+str(count)+' pixels checked!\n'+str(drawn)+' pixels drawn! Frame complete!')
        currentImage.close()
    elif renderType == renderTypes["Difference"]:
        buildTool()
        pyautogui.PAUSE = placespeed
        global gridByCount
        global switch

        removeTool()

        #remove pixels
        index = 0
        for dpC in currentdata:
            dpL = lastdata[index]
            if dpl == 1 and dpC == 0:
                pos = gridByCount[index]
                pyautogui.moveTo(pos[0], pos[1])
                pyautogui.click()
                pyautogui.click()

            index += 1

        buildTool()

        #add pixels
        index = 0
        for dpC in currentdata:
            dpL = lastdata[index]
            if dpl == 0 and dpC == 1:
                pos = gridByCount[index]
                pyautogui.moveTo(pos[0], pos[1])
                pyautogui.click()

            index += 1


def depictRenderType(lastData, currentData):
    # assuming both datas have same data count.
    if len(lastData) == len(currentData):
        # both datas have same data count
        similars = 0
        index = 0
        for dpC in currentData:
            dpL = lastData[index]
            if dpC == dpL: similars+=1

            index+=1
        
        diffs = len(currentData)-similars
        samePercent = (similars/diffs)*100
        if samePercent > diffthreshold:
            # use difference rendering, full will take too long.
            return renderTypes["Difference"]
        else:
            # use full rendering, difference will take too long.
            return renderTypes["Full"]
    else:
        print("Error! Invalid data size, continuing..")
        return renderTypes["Difference"]

def scanImage(fileName):
    filePath = input_folder+"/"+fileName
    img = Image.open(filePath, "r")
    pixels = list(img.getdata())
    return pixels, img

def buildTool():
    pyautogui.PAUSE = 0.02
    pyautogui.press("1")
    pyautogui.press("T")

def removeTool():
    pyautogui.PAUSE = 0.02
    pyautogui.press("4")

def clearFrame(): # le efficiante
    removeTool()
    pyautogui.PAUSE = 0.1
    pyautogui.moveTo(topLeft[0]+3, topLeft[1]+3)
    pyautogui.click()
    pyautogui.click()
    pyautogui.mouseDown()
    pyautogui.moveTo(bottomRight[0]-3, bottomRight[1]-3)
    pyautogui.mouseUp()
    pyautogui.press("#");
    pyautogui.press("right");
    pyautogui.press("right");
    pyautogui.press("enter");
    pyautogui.press("#");

#      _             _ _
#     (_) __ _ _ __ (_) |_ ___
#     | |/ _` | '_ \| | __/ _ \
#     | | (_| | | | | | ||  __/
#     |_|\__, |_| |_|_|\__\___|
#        |___/

def getPoints():
    # THIS WILL BE BROKEN ON WAYLAND
    # WHEN VINEGAR STARTS PATCHING WINE 9.0
    # AND WINE FORCES WAYLAND
    # BE WARNED
    # (i'll probably try find another library when that happens)
    def on_click(x, y, button, pressed):
        global clix
        global topLeft
        global topRight
        global bottomLeft
        global bottomRight
        if button == mouse.Button.left:
            if clix == 0:
                topLeft = (x, y)
                print("click on top right")
            elif clix == 2:
                topRight = (x, y)
                print("click on bottom left")
            elif clix == 4:
                bottomLeft = (x, y)
                print("click on bottom right")
            elif clix == 6:
                bottomRight = (x, y)
                testfill()
        clix += 1

    def testfill():
        # render a full frame with all pipes, as output to user.
        if gui: messagebox.showinfo('run.py', 'Callibration check will begin.')
        global gridByCount
        gridByCount = doMath.gridMath(topLeft, topRight, bottomLeft, bottomRight)[0]
        clearFrame()
        buildTool()
        pyautogui.PAUSE = placespeed
        for pos in gridByCount:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
        
        if gui:
            # ask user if callibrated correctly, if not, loop back to getPoints()
            time.sleep(1)
            callibrated = messagebox.askquestion('run.py', 'Was that properly callibrated?')
            if callibrated == "yes":
                messagebox.showinfo('run.py', 'Press OK to start.')
                clearFrame()
                start()
            else:
                messagebox.showinfo('run.py', 'Please select the 4 corners. Be as PRECISE as physically possible.')
                clearFrame()
                getPoints()
        else:
            # wait 10 seconds to give usr time to check callibration
            # idk why im doing comments im bored ok?
            time.sleep(10)
            start()

    def on_press(key):
        if key == keyboard.Key.esc:
            print("ESC pressed! Exitting...")
            os._exit(0)

    with mouse.Listener(on_click=on_click) as listener:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

def checkConfig():
    error = []
    stop = False
    print("Checking User Config...")

    none = "VALID"

    if screenshottingState > 2 or screenshottingState < 0:
        error.insert(1, "INVALID - out of range")
        stop = True
    else:
        error.insert(1, none)
    
    if intermission < 0:
        error.insert(2, "INVALID - out of range")
        stop = True
    else:
        error.insert(2, none)

    if os.path.isdir(output_folder):
        error.insert(3, none)
    else:
        error.insert(3, "INVALID - directory not found")
        stop = True

    if os.path.isdir(input_folder):
        error.insert(4, none)
    else:
        error.insert(4, "INVALID - directory not found")
        stop = True

    if screenshottingState > 1 or screenshottingState < 0:
        error.insert(5, "INVALID - out of range")
        stop = True
    else:
        error.insert(5, none)

    # Output results
    print(
        "screenshottingState -> "+error[0],
        "\nintermission -> "+error[1],
        "\noutput_folder -> "+error[2],
        "\ninput_folder -> "+error[3],
        "\nswitch -> "+error[4]
        )
    return stop

invalidConfig = checkConfig()
if gui:
    if invalidConfig:
        messagebox.showinfo('run.py', 'Invalid config.')
    else:
        #play = pyautogui.confirm('Proceed with playing "Bad Apple"?', buttons=["Yes", "No"])
        #if play == "Yes":
        play = messagebox.askquestion('run.py', f'Proceed with rendering all of {input_folder}?')
        if play == "yes":
            messagebox.showinfo('run.py', 'Please select the 4 corners. Be as PRECISE as physically possible.')
            getPoints()
else:
    if invalidConfig:
        print("Invalid config.")
    else:
        getPoints()
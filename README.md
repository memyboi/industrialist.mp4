# industrialist.mp4
i have no idea what im doing help me  
NOTE : the above sentence is true.  
NOTE : the above sentence is true.  
NOTE : the above sentence is true.  

## What is this?
This is the code I specifically made to play Bad Apple in Roblox [industrialist](https://www.roblox.com/games/9192423027/Industrialist-GOLD) (really good game you should play it).  
Made in python3.11.6, functionality may differ between python versions, but should stay largely the same, as long as you have the correct dependencies.

## How to run?
This is an important section, as getting this to run may be a pain.  
First off, this project was designed to work *specifically* in linux, on wayland. That is where I do my work, and that will be the natural outcome of doing this on an unpopular OS.  
As the most of you are on windows, please note that some things may just not work, or may be incompatible.  
  
First, clone this git repository. You may need to install the git command, and you can do so by installing it from your package manager (eg. `sudo pacman -Sy git`, `sudo apt-get install git`) or by going over to the [git website](https://git-scm.com/).  
Next, run `git clone https://github.com/memyboi/industrialist.mp4.git ./industrialistmp4` (the name of this repo will make your system think this folder is a video lol) to steal my code.  
We need to now instantiate the frames of a video, so put a video of your choosing into the folder you just cloned and call it "reference.mp4", and create two folders, "processed" and "rendered", and then run `python3 ./init.py`. The script will ask you if you want to skip generating new frames, press n and enter.  
Once the script finishes, check the processed folder if the frames are there.  
Next, open the run.py script and change the config to your liking.  
Once you've messed with the config, open roblox and go into industrialist.  
Make a pipe grid with a 32x24 block area inside, and make sure that 768 pipes can fit into that area. You will need to buy the pipes beforehand.  
Go behind your pipe grid and point your camera as down as possible.  
Go to the build tool, select the pipe you'd like to render with, and unequip the build tool.  
  
Then, to run the script, simply type `python3 run.py`, go back to the game (without clicking if you disabled the gui), then click through the gui (if you have one), and then click on the 4 inner corners of the pipe grid, from top left, top right, bottom left and bottom right in that order. If you have the gui enabled, the script will then place the grid full of pipes. This is the callibration, as you may have incorrectly clicked on the corners. When you confirm that it has been properly callibrated, it will then run.  

Now, runtime isn't great. It will take a VERY, VERY long time to render, and you should be ready to keep your computer on for a good day or so, depending on video length and how drastic the colour changes are.  

Once it is done, find some program to concatenate all of the images in the "rendered" folder or something (preferrably ffmpeg, but i couldn't get ffmpeg to work)  
Once that finished, you're done!  
  
(PS: make sure to turn on DND, you will get notifications if your desktop sends a notification for each screenshot)  
(PS: you will need a lot of free space (eg. 20 gigs?), and ram to concatenate the video)

## Dependencies:
- pyautogui
- pyscreenshot
- pynput
- pil
- opencv
- numpy  
- (optional) grimblast, supported in run.py


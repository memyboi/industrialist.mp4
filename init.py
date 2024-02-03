# initialise ffmpeg folder (cuz im not doing this shit manually)

import cv2
import os
import numpy
import glob
from PIL import Image

rFolder1 = "processed"

chk = input("Would you like to skip generating new frames? (Y/N)\n --> ")
if chk.lower() == "y":
    print("skipping cv2 hell...")
else:
    print("emptying ./"+rFolder1+"/")

    files = glob.glob('./'+rFolder1+"/*")
    for f in files:
        os.remove(f)
    print("emptied ./"+rFolder1+"/!")

    # --

    #ffmpeg.input("reference.mp4", ss = 0, r = 1)\
    #    .filter('fps', fps='60/60')\
    #    .output(rFolder1+'/%d.jpg', start_number=0)\
    #    .overwrite_output()\
    #    .run(quiet=False)

    vidcap = cv2.VideoCapture('reference.mp4')
    success,image = vidcap.read()
    count = 0
    while success:
        thresh = 127
        im_bw = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite("./"+rFolder1+"/"+str(count)+".jpg", im_bw)     # save frame as JPEG file      
        print('Read frame', count, 'successfully!')
        success,image = vidcap.read()
        count += 1

    print("\n\n\nSPLITTING COMPLETE!!!\nnow to process >:(\n\n\n")

#downscale to 32x24 (4:3 aspect ratio lmao)

print("Downscaling...")

count = 0
dir = "./"+rFolder1
files = os.listdir(dir)
while count < len(files):
    filename = files[count]
    new_image = cv2.imread("./"+rFolder1+"/"+filename, cv2.IMREAD_GRAYSCALE)
    thresh = 127
    res = cv2.resize(new_image, (32, 24))
    im_bw = cv2.threshold(res, thresh, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite("./"+rFolder1+"/"+str(filename), im_bw)     # save frame as JPEG file      
    print("processed frame", count, "successfully!")
    count += 1
import cv2 as cv
import imutils
import numpy as np
import os
# from wand.image import Image
import pytesseract
from PIL import Image
import os

from matplotlib import pyplot as plt

from __constants__ import *
from __pickle_processing__ import writeFile

def loadImages(inLocation,inFileName):
    # if ".pdf" in inFileName:
    #     # img = Image(filename=file)
    #     convertedFile = Image(filename=inFileName).convert('png')
    # else:
    #     convertedFile = None

    filename_split = inFileName.rsplit(".", 1)[0]

    image = cv.imread(inLocation + "\\" +inFileName)
    try:
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (3, 3), 0)
        gray = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                     cv.THRESH_BINARY, 3, 2)
        cv.imshow("Gray",gray)
        cv.waitKey(0)

        # filename = DIR + TRAIN_TEMP_DATADIR + "{}.png".format(filename_split)
        # cv.imwrite(filename, gray)
        # return filename
    except:
        print("ERROR: " + str(filename_split))


def arrayToText(inFile):
    # Path of tesseract executable
    # pytesseract.pytesseract.tesseract_cmd = '**Path to tesseract executable**'
    text = pytesseract.image_to_string(Image.open(inFile))
    # print(text)
    return text
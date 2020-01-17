from __constants__ import *
from __image_processing import loadImages, arrayToText
from __pickle_processing__ import *
from __nlp_processing__ import *
from __scikit_learn import *
import os
import csv

from matplotlib import pyplot as plt

"""
    1. Exploratory
"""

## Get all training data filenames
train_file_directory = [file for file in os.listdir(DIR + TRAIN_DATADIR) if os.path.isfile(os.path.join(DIR + TRAIN_DATADIR,file))]


## Load images
print("Load Images into 2d array")
ocr_img = {}
if not checkFile("ocr_trained_data.pickle",DATADIR_PICKLE):
    for file in train_file_directory:
        fileName = file.rsplit('.', 1)[0]
        img = loadImages(DIR + TRAIN_DATADIR,file)
        if img:
            ocrImg = arrayToText(img)
            ocr_img[fileName] = ocrImg
        else:
            ocr_img[fileName] = "Error"

    writeFile(ocr_img,"ocr_trained_data.pickle",DATADIR_PICKLE)

## Load OCR images from pickle
if checkFile("ocr_trained_data.pickle",DATADIR_PICKLE):
    ocr_img = readFile("ocr_trained_data.pickle", DATADIR_PICKLE)
else:
    print("Pickle not found")

## Perform NLP on OCR images
if ocr_img:
    ocr_nlp_img = split_words_in_english(ocr_img)

# ocr_nlp_img = readFile("ocr_nlp_trained_data.pickle", DATADIR_PICKLE)

## Train images lables
with open(DIR + TRAIN_LABELS, mode='r',newline='\n') as infile:
    reader = csv.DictReader(infile, delimiter=',',quotechar='"')
    train_labels = list(reader)

## ML -> naive_bayes

# fit_Naive_bayes()


# Test





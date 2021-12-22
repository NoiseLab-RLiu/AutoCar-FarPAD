from __future__ import division
from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
import os
import glob
import random

import os
import re
import numpy as np
from numpy import linalg as LA
import pandas as pd
#%matplotlib inline 
import matplotlib.pyplot as plt 
from time import gmtime, strftime
from scipy.signal import butter, lfilter,savgol_filter
#from_future_import division
import scipy as sp

def dataseparation(txtlocation):
    '''
    this function change the txt.file into list of tuples
    
    input: fname: txt file location
    
    output: list
    '''
    #title_akas = pd.read_csv('/Users/seankamano/Downloads/title.akas.tsv', delimiter = '\t', encoding = 'utf-8')
    f_1 = open(txtlocation, 'r') # read files
    lines = f_1.readlines() # read line by line
    f_1.close() # close the file
    new_lines = []
    for l in lines[1:]:
        new_lines.append(l.split('\n')) # remove "\t" by line
    
    mHealth = pd.DataFrame(new_lines)
    loc_total = mHealth[0]
    num_item = loc_total.shape[0]
    loc_result = []
    for idx in range(num_item):
        loc_item = tuple(map(int, loc_total[idx].split(' ')))
        loc_result.append(loc_item)
        
    return loc_result
     
def clipimage(imagelocation, savelocation, loc_result, imagename):
    """input: loc_result: a list of tuples which contain the location for each face
              imagelocation: image location
              saveflocation: location to store clipped images
              imagename
       output: clipped faces stored in the destination"""
    
    im = Image.open(imagelocation + "/" + imagename)
    for idx, loc in enumerate(loc_result):
        region = im.crop(loc)
        region = region.resize((224, 224)) # resize the cropped image to 224x224
        region.save(savelocation + "/" + imagename[:-5] + "_cropped_" + str(idx) + ".JPEG", quality = 90 )
        # quality and be changed or removed

imagelocation = "/Users/huangzhisheng/Desktop/CSE_291/foodp/BBox-Label-Tool-master/Images/002"
txtlocation = "/Users/huangzhisheng/Desktop/CSE_291/foodp/BBox-Label-Tool-master/Labels/002/test_1.txt"
saveloction = "/Users/huangzhisheng/Desktop/CSE_291/foodp/BBox-Label-Tool-master/Images/002"
imagename = "test_1.JPEG"
loc_result = dataseparation(txtlocation)
clipimage(imagelocation, saveloction, loc_result, imagename)

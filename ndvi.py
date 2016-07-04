# script to automatically crop all photos in directory

from __future__ import print_function
from PIL import Image
import os
import numpy as np

def ndvi(image):
    img = np.asarray(image)
    r = img[:,:,0]/255
    #print (r)
    g = img[:,:,1]/255
    b = img[:,:,2]/255
    #print (b)
    ndvi = np.zeros((r.shape[0], r.shape[1]))

    try:
        ndvi = (2*b - r)/r
    except RuntimeWarning:
        pass
    neg_count = 0
    for i in range(r.shape[0]):
        #print (i)
        for j in range(r.shape[1]):
            if ndvi[i][j] > 1:
                neg_count += 1
    print(neg_count)
    """
    neg_count = 0
    for i in range(r.shape[0]):
        #print (i)
        for j in range(r.shape[1]):
            d_now = r[i][j]
            n_now = 2*b[i][j] - r[i][j]
            #print (d_now)
            #print (n_now)
            if d_now == 0:
                if n_now > 0:
                    ndvi[i][j] = 1
                elif n_now < 0:
                    ndvi[i][j] = -1
                else:
                    ndvi[i][j] = 0
            else:
                ndvi[i][j] = n_now/d_now
                #print (ndvi[i][j])
            if ndvi[i][j] <= 0:
                neg_count += 1
    print (neg_count)
    """
    return ndvi


base_dir = '/home/v-gupta/wv2016/real_project/plant'
os.chdir(base_dir)
dirs = os.listdir()
"""
for i in dirs:
    os.chdir(i)
    files = os.listdir()
    for j in files:
        image = Image.open(base_dir+'/'+i+'/'+j)
        np.savetxt(j[0:-3]+'csv',ndvi(image),fmt='%10.5f',delimiter=',')
        
    os.chdir(base_dir)
"""
np.savetxt('test.csv', ndvi(Image.open('test.jpg')), fmt = '%10.5f', delimiter = ',')




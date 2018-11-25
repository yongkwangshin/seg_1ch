import cv2
import os
import numpy as np


flist=os.listdir(os.path.join('./inputs'))
#print(flist)


for fname in flist:
    input_image = os.path.join('./inputs', fname)
    gray = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)
    #print(input_image)
    #target_image = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)[1]
    
    #print(target_image.shape)
    #cv2.imshow('gray', gray)
    
    
    img_resize = cv2.resize(gray, (128,128), interpolation = cv2.INTER_AREA)
    out_path = os.path.join('inputs2', fname)
#print(out_path)
    cv2.imwrite(out_path, img_resize)
#cv2.waitKey(0)
#fname = 'data_0014.png'

#original = cv2.imread(fname, cv2.IMREAD_COLOR)
#gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
#unchange = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
#target_image = gray
#target_image = cv2.threshold(target_image, 20, 255, cv2.THRESH_BINARY)[1]
#print(original.shape)
#print(gray.shape)
#cv2.imshow('Original', original)
#cv2.imshow('target_image', target_image)
#cv2.imshow('Unchange', unchange)

#cv2.waitKey(0)
#cv2.destroyAllWindows()


#test_image = cv2.imread('data_0014.png', cv2.IMREAD_COLOR)
#test_image.shape

#cv2.imshow('test_image', test_image)

#cv2.waitKey(0)
#cv2.destroyAllWindows()



# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:53:12 2021

@author: Laboratorio
"""

from scipy.io import loadmat

sacar = loadmat('realmatlab.mat')

slice1 = sacar['slice1']

tes = sacar['tes']

data = slice1

import numpy 
import numpy.array

def ajustar(pixel_col):
    x = numpy.array('slice1')
    y = numpy.array(tes)
    (A, B) = numpy.polyfit(x, numpy.log(y), 1, w=numpy.sqrt(y))
    KS0 = numpy.exp(A)
    T2 = -1/B

info = []
for image in range(0,50):
    for x in range (0, 128):
        for y in range (0,128):
            pixel = x*128 + y
            
            while len(info) < pixel:
                info.append([])
                
            info[pixel].append(data(image)[x][y])
            
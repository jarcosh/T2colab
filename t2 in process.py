# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:53:12 2021

@author: Laboratorio
"""

from scipy.io import loadmat

import numpy

# ajusta KS0 y T2 según la ecuacion
def ajustar(pixel_col, times):
    x = pixel_col
    y = numpy.array(times)
    (A, B) = numpy.polyfit(x, numpy.log(y), 1, w=numpy.sqrt(y))
    KS0 = numpy.exp(A)
    T2 = -1/B
    return (KS0, T2)

def main():
    sacar = loadmat('realmatlab.mat')
    
    slice1 = sacar['slice1']
    times = sacar['tes']
    
    for line_arrays in slice1:
        for pixel_array in line_arrays:
            (KS0, T2) = ajustar(pixel_array, times[0])
            # aqui su codigo de prueba

# buena practica
if __name__ == "__main__":
    main()
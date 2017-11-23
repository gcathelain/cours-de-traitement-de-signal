#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:35:27 2017

@author: guillaumecathelain
"""

from cv2 import imread, imshow

from scipy.signal import convolve, freqz

image = imread('IRM.jpeg',0)
imshow('Image initiale',image)

#%% Flou

b = ones((3,3))
b[1][1] = 8
b = b/8
flou = convolve(image,b)
flou = uint8(flou)
imshow('Image floutee',flou)

#%% Gradient
b = -ones((3,3))
b[1][1] = 8
b = b/8

grad = convolve(image,b)
grad= uint8(grad)
imshow('Gradient de l\'image',grad)

#%% Les filtres
b1_flou = array([-1,1])
freq, h = freqz(b1_flou,1)
fs = 630/100
nyq = fs/2
figure()
semilogy(nyq*freq, abs(h))
grid('on')
xlabel('Frequence spatiale en 1/mm')
ylabel('Gain')
title('Réponse fréquentielle du filtre flou équivalent 1D')
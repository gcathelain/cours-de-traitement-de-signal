#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:10:20 2017

@author: guillaumecathelain
"""
from scipy.signal import periodogram, spectrogram

#Modulation en fréquence
# superposition de sinus
fs = 500 # la frequence d'echantillonnage en Hz. Attention à vérifier la condition de Shannon
fp = 10  #frequence de la porteuse
fm = 1 #frequence du modulant
B = 5   #indice de modulation
n = 10*fs # nombre d'échantillons. Ici le signal dure 10 secondes
t = linspace(0,(n-1)/fs,n)
x = cos(2*pi*fp*t + B*sin(2*pi*fm*t))

figure()
subplot(121)
plot(t,x)
xlabel('Temps en secondes')
ylabel('Amplitude')
title('Représentation temporelle du signal')

f, psd = periodogram(x, fs)
subplot(122)
plot(f, psd)
xlabel('fréquence [Hz]')
ylabel('densité spectrale de puissance [V^2/Hz]')
title('Représentation spectrale du signal')


#Spectrogramme

f,t,Sxx = spectrogram(x,fs, nperseg = int(fs*0.2), noverlap=nperseg)
figure()
pcolormesh(t,f,Sxx)
ylabel('Frequence en Hz')
xlabel('Temps en secondes')
colorbar(label = 'Densité spectrale de puissance [V^2/Hz]')
grid('on')
title('Représentation temps-fréquence du signal')
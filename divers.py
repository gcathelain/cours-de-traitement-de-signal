#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 13:04:26 2017

@author: guillaumecathelain
"""

from scipy.signal import spectrogram, lfilter, butter, freqz

#%%
fs = 1000

order = 4
fmin = 20
fmax = 50

Wn = array([fmin/nyq,fmax/nyq])
#b,a = butter(order,Wn,'bandpass')
b,a = butter(order,fmin/nyq,'highpass')

freq, h = freqz(b,a)

figure()
semilogy(nyq*freq/pi, abs(h))
grid('on')
xlabel('Frequence [Hz]')
ylabel('Gain')
title('Réponse fréquentielle du filtre')

#%%
fs = 1000 # la frequence d'echantillonnage en Hz. Attention à vérifier la condition de Shannon
F1 = 5  #frequence de la porteuse
F2 = 80 #frequence du modulant
n = fs # nombre d'échantillons. Ici le signal dure 10 secondes
t = linspace(0,(n-1)/fs,n)
noise = 5*random.normal(0, 1, n)
x1 = 5*sin(2*pi*F1*t)
x2 = 1*sin(2*pi*F2*t)
x = x1+ x2 + noise

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

figure()
subplot(311)
plot(t,noise)
xlabel('Temps en secondes')
ylabel('Amplitude')
title('Signal filtré par un filtre de nature ...')

subplot(312)
plot(t,x1)
xlabel('Temps en secondes')
ylabel('Amplitude')
title('Signal filtré par un filtre de nature ...')

subplot(313)
plot(t,x2)
xlabel('Temps en secondes')
ylabel('Amplitude')
title('Signal filtré par un filtre de nature ...')




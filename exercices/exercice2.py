#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:56:34 2017

@author: guillaumecathelain
"""
from scipy.signal import periodogram, firls, freqz, lfilter

#%% superposition de sinus
fs = 500 # la frequence d'echantillonnage en Hz. Attention à vérifier la condition de Shannon
F1 = 1
F2 = 10
n = 10*fs # nombre d'échantillons. Ici le signal dure 10 secondes
t = linspace(0,(n-1)/fs,n)
x = 10*sin(2*pi*F1*t) + 2*sin(2*pi*F2*t)

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

#%% filtrage passe bas
nyq = fs/2   # frequence de Nyquist pour respecter la condition de Shannon
maxOrder = 201  #ordre du filtre
bands = (0,F1,F2,nyq)
desired = (0,0,1,1)
coeffs = firls(maxOrder, bands, desired,nyq = nyq)

freq, h = freqz(coeffs)
figure()
semilogy(nyq*freq/pi, abs(h))
grid('on')
xlabel('Frequence en Hz')
ylabel('Gain')
title('Réponse fréquentielle du filtre')

y = lfilter(coeffs,1,x)
figure()
subplot(121)
plot(t,y)
xlabel('Temps en secondes')
ylabel('Amplitude')
title('Représentation temporelle du signal filtré')
f, psd = periodogram(y, fs)
subplot(122)
plot(f, psd)
xlabel('fréquence [Hz]')
ylabel('densité spectrale de puissance [V^2/Hz]')
title('Représentation spectrale du signal filtré')


#Exercices: 
#- calculer la réponse fréquentielle du filtre moyen: y[n] = (x[n]+x[n-1])/2

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:04:28 2017

@author: guillaumecathelain
"""

#%%Initialisation
from wfdb import srdsamp
from scipy.signal import spectrogram, lfilter, butter

## Download data
#import os
#wfdb.dldatabase('slpdb', os.getcwd(),records=['slp01a'])
#wfdb.dldatabase('slpdb', os.getcwd())

#Choisir un signal
signals, fields = srdsamp('slp04')
#signals, fields = srdsamp('slp32')
#signals, fields = srdsamp('slp48')
#signals, fields = srdsamp('slp59')



eeg = signals[:,2]
fs = 250
n = len(eeg)
t = linspace(0,(n-1)/fs,n)
figure()
plot(t/60,eeg)
xlabel('Temps [min]')
ylabel('Amplitude [mV]')
title('Signal EEG brut')

#%% Spectrogram sur les bandes delta, theta, alpha, beta
nperseg = int(4*fs)
f_spec, t_spec, Sxx = spectrogram(eeg, fs, nperseg = nperseg,noverlap=nperseg//2)

figure()
#delta
Sxx_d = Sxx[2:12]
f_d = f_spec[2:12]
#theta
Sxx_t = Sxx[16:28]
f_t = f_spec[16:28]
#alpha
Sxx_a = Sxx[32:48]
f_a = f_spec[32:48]
#beta
Sxx_b = Sxx[52:120]
f_b = f_spec[52:120]

subplot(411)
pcolormesh(t_spec/60,f_b,Sxx_b)
ylabel('Frequence [Hz]')
xlabel('Temps [min]')
colorbar(label = 'Densité spectrale de puissance [mV^2/Hz]')
subplot(412)
pcolormesh(t_spec/60,f_a,Sxx_a)
ylabel('Frequence [Hz]')
xlabel('Temps [min]')
colorbar(label = 'Densité spectrale de puissance [mV^2/Hz]')
subplot(413)
pcolormesh(t_spec/60,f_t,Sxx_t)
ylabel('Frequence [Hz]')
colorbar(label = 'Densité spectrale de puissance [mV^2/Hz]')
subplot(414)
pcolormesh(t_spec/60,f_d,Sxx_d)
ylabel('Frequence [Hz]')
colorbar(label = 'Densité spectrale de puissance [mV^2/Hz]')

#%% Delta (0.5 - 3Hz)
#filtrage
fmin = 0.5
fmax = 3

nyq = fs/2   # frequence de Nyquist pour respecter la condition de Shannon
order = 4  #ordre du filtre

Wn = array([fmin/nyq,fmax/nyq])
b,a = butter(order,Wn,'bandpass')
freq, h = freqz(b,a)

figure()
semilogy(nyq*freq/pi, abs(h))
grid('on')
xlabel('Frequence [Hz]')
ylabel('Gain')
title('Réponse fréquentielle du filtre')

eeg_d = lfilter(b,a,eeg)

figure()
subplot(211)
plot(t,eeg)
title('Signal eeg brut')
ylabel('Amplitude [mV]')
grid('on')

subplot(212)
plot(t,eeg_d)
title('Bande delta')
xlabel('Temps [min]')
ylabel('Amplitude [mV]')
grid('on')

#%% Théta (4-7Hz)
#filtrage
fmin = 4
fmax = 7

nyq = fs/2   # frequence de Nyquist pour respecter la condition de Shannon
order = 4  #ordre du filtre

Wn = array([fmin/nyq,fmax/nyq])
b,a = butter(order,Wn,'bandpass')
freq, h = freqz(b,a)

figure()
semilogy(nyq*freq/pi, abs(h))
grid('on')
xlabel('Frequence [Hz]')
ylabel('Gain')
title('Réponse fréquentielle du filtre')

eeg_t = lfilter(b,a,eeg)

figure()
subplot(211)
plot(t,eeg)
title('Signal eeg brut')
ylabel('Amplitude [mV]')
grid('on')

subplot(212)
plot(t,eeg_t)
title('Bande Theta')
xlabel('Temps [min]')
ylabel('Amplitude [mV]')
grid('on')

#%% Autres bandes
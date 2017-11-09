#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 08:23:04 2017

@author: guillaumecathelain
"""
from scipy.signal import spectrogram, firls,freqz, butter,lfilter, periodogram

#%% Signal brut
#Charger le signal
filename = "ch3_F3.txt"
eeg = loadtxt(filename)
n = len(eeg)
fs = 200
t = linspace(0,(n-1)/fs,n)

#Représentation temporelle du signal
figure()
subplot(211)
plot(t,eeg)
title('Signal eeg brut')
xlabel('Temps [s]')
ylabel('Amplitude [V]')
grid('on')

#préfiltrage
nyq = fs/2
order = 4
fmin,fmax = 1,20
Wn = array([fmin/nyq,fmax/nyq])
b,a = butter(order,Wn,'bandpass')
eeg_f = lfilter(b,a,eeg)
eeg_f = eeg_f[2*fs:]
t_f = t[2*fs:]
subplot(212)
plot(t_f,eeg_f)
title('Signal eeg préfiltré')
xlabel('Temps [s]')
ylabel('Amplitude [V]')
grid('on')
ylim([-5e-5,5e-5])

#Représentation temps-fréquence
figure()
nperseg = int(3*fs)
f_spec,t_spec,Sxx = spectrogram(eeg,fs=fs,nperseg = nperseg,noverlap = nperseg//2)
pcolormesh(t_spec,f_spec,Sxx)
ylim([0,20])
ylabel('Frequence en Hz')
xlabel('Temps en secondes')
colorbar(label = 'Densité spectrale de puissance [V^2/Hz]')
grid('on')
title('Représentation temps-fréquence du signal brut')

#%% Periodogramme sur la moitié du signal
t1 = t[0:len(eeg)//2]
x1 = eeg[0:len(eeg)//2]
t2 = t[len(eeg)//2:len(eeg)]
x2 = eeg[len(eeg)//2:len(eeg)]

figure()
subplot(211)
plot(t1,x1)
title('Signal eeg première moitié')
ylabel('Amplitude [V]')
grid('on')
subplot(212)
plot(t2,x2)
title('Signal eeg seconde moitié')
ylabel('Amplitude [V]')
grid('on')
xlabel('Temps [s]')

figure()
subplot(211)
f, psd = periodogram(x1, fs)
plot(f, psd)
ylabel('densité spectrale de puissance [V^2/Hz]')
title('Spectre du signal première moitié')
subplot(212)
f, psd = periodogram(x2, fs)
plot(f, psd)
xlabel('fréquence [Hz]')
ylabel('densité spectrale de puissance [V^2/Hz]')
title('Spectre du signal seconde moitié')


#%% Alpha (8 à 15 Hz)
#filtrage
fmin = 7
fmax = 16

nyq = fs/2   # frequence de Nyquist pour respecter la condition de Shannon
order = 4  #ordre du filtre

Wn = array([fmin/nyq,fmax/nyq])
b,a = butter(order,Wn,'bandpass')
freq, h = freqz(b,a)

figure()
semilogy(nyq*freq/pi, abs(h))
grid('on')
xlabel('Frequence en Hz')
ylabel('Gain')
title('Réponse fréquentielle du filtre')

figure()
eeg_a = lfilter(b,a,eeg)
subplot(211)
plot(t,eeg)
title('Signal eeg brut')
ylabel('Amplitude [V]')
grid('on')

subplot(212)
plot(t,eeg_a)
title('Signal eeg bande alpha')
xlabel('Temps [s]')
ylabel('Amplitude [V]')
ylim([-2e-5,2e-5])
grid('on')

#Spectrogramme
figure()
nperseg = int(3*fs)
f_spec,t_spec,Sxx = spectrogram(eeg_a[1*fs:],fs=fs,nperseg = nperseg,noverlap = nperseg//2)
pcolormesh(t_spec,f_spec,Sxx)
ylim([0,20])
ylabel('Frequence en Hz')
xlabel('Temps en secondes')
colorbar(label = 'Densité spectrale de puissance [V^2/Hz]')
grid('on')
title('Représentation temps-fréquence du signal brut')

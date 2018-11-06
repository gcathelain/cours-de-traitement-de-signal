#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 08:41:01 2017

@author: guillaumecathelain
"""

fs = 1000 # en Hz, il s'agit d'un signal quasi continu
F = 1
n = fs
t = linspace(0,(n-1)/fs,n)
sinus = sin(2*pi*F*t)


figure()
subplot(121)
plot(t,sinus)
xlabel('Temps en secondes')
ylabel('Amplitude')
title('Signal analogique')


#%%échantillonnage
k = 10
f_ech = fs/k # en Hz, il s'agit d'un signal échantillonné
t_ech = t[arange(0,n-1,k)]
sinus_ech = sin(2*pi*F*t_ech)


#bloqueur d'ordre 0
sinus_bloq = zeros(0)
for i in range(len(sinus_ech)):
    sinus_bloq = concatenate((sinus_bloq,ones(k)*sinus_ech[i]))

subplot(122)
plot(t,sinus_bloq)
xlabel('Temps en secondes')
ylabel('Amplitude')
title('Signal échantillonné à 100 Hz')


# %% codage et loi de quantification uniforme
figure()
N = 256
n = 16  #4bits
x = linspace(-1,1,N)
val_y = linspace(-1,1,n)
y = zeros(0)
for i in range(len(val_y)):
    y = concatenate((y,ones(n)*val_y[i]))
    
plot(x,y)
xlabel('Amplitude du signal analogique échantillonné')
ylabel('Amplitude du signal codé')
title('Loi de quantification uniforme sur 4 bits')
grid(b='on')

#quantification
figure()
subplot(121)
plot(t,sinus_bloq)
xlabel('Temps en secondes')
ylabel('Amplitude')
title('Signal échantillonné à 100 Hz')
subplot(122)
sinus_quant = zeros(0)
for i in range(len(sinus_ech)):
    idx = argmin(abs(val_y-sinus_ech[i]))
    if sinus_ech[i]<val_y[idx]: 
        idx=idx-1
    sinus_quant = concatenate((sinus_quant,ones(k)*val_y[idx]))
plot(t,sinus_quant)
xlabel('Temps en secondes')
ylabel('Amplitude')
title('Signal échantillonné à 100 Hz et codé sur 4 bits')

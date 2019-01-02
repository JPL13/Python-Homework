import matplotlib.pyplot as plt
from scipy.io import wavfile as spwav
import scipy.fftpack as spft 
import numpy as np

rate,wooguy = spwav.read("wooguy.wav")
print rate
print wooguy.shape # it's stereo - there are two audio channels, each with 695k samples.
print wooguy.dtype 

wooguy=wooguy[:,0]

time_step = 1./rate # time between samples
print "rate:",rate
print "time_step:",time_step
freq = spft.fftfreq(wooguy.size, d=time_step) # get the frequencies(just like the tutorial)
print freq.shape

fft = spft.fft(wooguy)
print fft.shape
print fft.dtype

power = np.abs(fft)

plt.plot(freq,power)

index_with_max_power=np.argmax(power)
freq_with_max_power=freq[index_with_max_power]
print index_with_max_power
print freq_with_max_power

max_powers=power.argsort()[::-1]#reverse the array
print freq[max_powers][:100]

mask5=np.logical_and(np.abs(freq)>550, np.abs(freq)<600) 

fft[mask5]=0

plt.plot(freq, np.abs(fft))

new_audio = spft.ifft(fft)

spwav.write("wooguy_new.wav", rate, new_audio.astype('int16'))
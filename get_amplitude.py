import librosa as librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
from IPython.display import Audio

## TODO: find a library that can write a DMX file

dmx_data = []

audioFile = 'StarWars60.wav'
y, sr = librosa.load(audioFile)
# new_y = librosa.resample(y, orig_sr=sr, target_sr=1000) #lowering the sample rate if necessary

red = 0
green = 1

i=0
## finds amplitude values
while i < len(y):
    amplitude = abs(y[i])
    if amplitude < 0.5:
        dmx_data.append(red)
        # dmx_data.append(str(amplitude))
        i+=1
    else:
        dmx_data.append(green)
        # dmx_data.append(str(amplitude))
        i+=1

# print(dmx_data)

## if you want to send n times less commands to the light       
# second = []
# n=100
# for s in range(0,len(y),int(sr/n)):
#     second.append(np.abs(y[s:s+int(sr/n)]).mean())
# print(second)

## shows amplitude envelope
# plt.figure(figsize=(12, 4))
# librosa.display.waveshow(y, sr=sr)
# plt.title('Amplitude Envelope')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.show()

import mido
from mido import MidiFile, MidiTrack, Message
import librosa as librosa
import numpy as np
import librosa.display

audioFile = 'StarWars60.wav'
y, sr = librosa.load(audioFile)
# new_y = librosa.resample(y, orig_sr=sr, target_sr=1000) #lowering the sample rate if necessary

midi_file = MidiFile()
track = MidiTrack()
midi_file.tracks.append(track)

# sends n times less commands to the light       
n=100

for s in range(0,len(y),int(sr/n)):
    temp = (np.abs(y[s:s+int(sr/n)]).mean())
    if temp < 0.2:
        track.append(Message('note_on', note=60, velocity=64, time=0))    # Note On (C4)
        track.append(Message('note_off', note=60, velocity=64, time=500))  # Note Off (C4) after 500ms
        
    else:
        track.append(Message('note_on', note=62, velocity=64, time=0))    # Note On (D4)
        track.append(Message('note_off', note=62, velocity=64, time=500))  # Note Off (D4) after 500ms

midi_file.save('output.mid')


## sends midi notes for each signal in the audio file
#i=0
# print(len(y))
# while i < len(y):
#     amplitude = abs(y[i])
#     if amplitude < 0.5:
#         track.append(Message('note_on', note=60, velocity=64, time=0))    # Note On (C4)
#         track.append(Message('note_off', note=60, velocity=64, time=500))  # Note Off (C4) after 500ms
#         i+=1
#     else:
#         track.append(Message('note_on', note=62, velocity=64, time=0))    # Note On (D4)
#         track.append(Message('note_off', note=62, velocity=64, time=500))  # Note Off (D4) after 500ms
#         i+=1

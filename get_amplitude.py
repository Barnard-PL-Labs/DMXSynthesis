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


## below is for future use; configures channels (can use for different lights)
# def create_dmx_midi_file(filename):
#     mid = MidiFile()
#     track = MidiTrack()
#     mid.tracks.append(track)

#     # Set DMX channel 1 to value 100
#     dmx_channel_1 = 1
#     dmx_value_1 = 100
#     cc_message_1 = Message('control_change', control=dmx_channel_1, value=dmx_value_1)
#     track.append(cc_message_1)

#     # Set DMX channel 2 to value 50
#     dmx_channel_2 = 2
#     dmx_value_2 = 50
#     cc_message_2 = Message('control_change', control=dmx_channel_2, value=dmx_value_2)
#     track.append(cc_message_2)

#     # Add a delay (optional)
#     track.append(Message('control_change', control=0, value=0, time=100))

#     # Example of triggering DMX channel 3 at full intensity
#     dmx_channel_3 = 3
#     dmx_value_full = 127
#     note_on_message = Message('note_on', note=dmx_channel_3, velocity=dmx_value_full)
#     track.append(note_on_message)

#     # Add a delay (optional)
#     track.append(Message('note_on', note=0, velocity=0, time=100))

#     # Example of turning off DMX channel 3
#     note_off_message = Message('note_off', note=dmx_channel_3, velocity=0)
#     track.append(note_off_message)

#     # Save the MIDI file
#     mid.save(filename)

#     midi_file_name = "dmx_control.mid"
#     create_dmx_midi_file(midi_file_name)
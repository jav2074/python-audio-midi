#----------------------------------------------------------------------------------------
from mido import Message, MidiFile, MidiTrack, MetaMessage
import random
import datetime

#----------------------------------------------------------------------------------------
figure = [
	# {'name' : 'redonda', 		'ticks' : 1920 },
	# {'name' : 'blanca', 		'ticks' : 960 },
	{'name' : 'negra', 			'ticks' : 480 },
	# {'name' : '3-negra', 		'ticks' : 320 },
	{'name' : 'corchea', 		'ticks' : 240 },
	# {'name' : '3-corchea', 		'ticks' : 160 },
	{'name' : 'semicorchea', 	'ticks' : 120 },
	# {'name' : 'quintillo', 		'ticks' : 96 },
	# {'name' : '3-semicorchea', 	'ticks' : 80 },
	# {'name' : 'fusa', 			'ticks' : 60 },
	# {'name' : '3-fusa', 		'ticks' : 40 },
	# {'name' : 'semifusa', 		'ticks' : 30 },
]
note = [
	# {'name' : 'C8', 'pitch' : 108 },
	# {'name' : 'B7', 'pitch' : 107 },
	# {'name' : 'A7', 'pitch' : 105 },
	# {'name' : 'G7', 'pitch' : 103 },
	# {'name' : 'F7', 'pitch' : 101 },
	# {'name' : 'E7', 'pitch' : 100 },
	# {'name' : 'D7', 'pitch' : 98 },
	{'name' : 'C7', 'pitch' : 96 },
	{'name' : 'B6', 'pitch' : 95 },
	{'name' : 'A6', 'pitch' : 93 },
	{'name' : 'G6', 'pitch' : 91 },
	{'name' : 'F6', 'pitch' : 89 },
	{'name' : 'E6', 'pitch' : 88 },
	{'name' : 'D6', 'pitch' : 86 },
	{'name' : 'C6', 'pitch' : 84 },
	{'name' : 'B5', 'pitch' : 83 },
	{'name' : 'A5', 'pitch' : 81 },
	{'name' : 'G5', 'pitch' : 79 },
	{'name' : 'F5', 'pitch' : 77 },
	{'name' : 'E5', 'pitch' : 76 },
	{'name' : 'D5', 'pitch' : 74 },
	{'name' : 'C5', 'pitch' : 72 },
	{'name' : 'B4', 'pitch' : 71 },
	{'name' : 'A4', 'pitch' : 69 },
	{'name' : 'G4', 'pitch' : 67 },
	{'name' : 'F4', 'pitch' : 65 },
	{'name' : 'E4', 'pitch' : 64 },
	{'name' : 'D4', 'pitch' : 62 },
	{'name' : 'C4', 'pitch' : 60 },
	{'name' : 'B3', 'pitch' : 59 },
	{'name' : 'A3', 'pitch' : 57 },
	{'name' : 'G3', 'pitch' : 55 },
	{'name' : 'F3', 'pitch' : 53 },
	{'name' : 'E3', 'pitch' : 52 },
	{'name' : 'D3', 'pitch' : 50 },
	{'name' : 'C3', 'pitch' : 48 },
	{'name' : 'B2', 'pitch' : 47 },
	{'name' : 'A2', 'pitch' : 45 },
	{'name' : 'G2', 'pitch' : 43 },
	{'name' : 'F2', 'pitch' : 41 },
	{'name' : 'E2', 'pitch' : 40 },
	{'name' : 'D2', 'pitch' : 38 },
	{'name' : 'C2', 'pitch' : 36 },
	# {'name' : 'B1', 'pitch' : 35 },
	# {'name' : 'A1', 'pitch' : 33 },
	# {'name' : 'G1', 'pitch' : 31 },
	# {'name' : 'F1', 'pitch' : 29 },
	# {'name' : 'E1', 'pitch' : 28 },
	# {'name' : 'D1', 'pitch' : 26 },
	# {'name' : 'C1', 'pitch' : 24 },
	# {'name' : 'B0', 'pitch' : 23 },
	# {'name' : 'A0', 'pitch' : 21 },
]
#----------------------------------------------------------------------------------------
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
program = random.randint(0, 127)	# (0, 79)
track.append(Message('program_change', program=program)) # default piano

totalTicks = 0
while totalTicks < 1920*16:
	# pitch = random.randint(21, 96)	# (48, 108)
	pitch = random.randrange(len(note))
	# tick = random.randint(40, 100)
	time = random.randrange(len(figure))
	track.append(Message('note_on',  note=note[pitch]['pitch'], velocity=100, time=0))
	track.append(Message('note_off', note=note[pitch]['pitch'], velocity=100, time=figure[time]['ticks']))
	totalTicks += figure[time]['ticks']
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
print ("--------------------------------------------------------------")
print("Music Maker")
print ("--------------------------------------------------------------")
print(track)
print ("--------------------------------------------------------------")
x1 = str(datetime.datetime.now())
x1 = x1.replace(':', '-')
x1 = x1.replace(' ', '_')
x1 = x1[0:x1.find('.')]
name = 'midi_'+x1+'.mid'
print(name)
print ("--------------------------------------------------------------")
#----------------------------------------------------------------------------------------
mid.save(name)
#----------------------------------------------------------------------------------------
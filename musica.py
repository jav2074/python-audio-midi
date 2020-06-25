#----------------------------------------------------------------------------------------
import winsound
import random

figura = [
	# {'name' : 'redonda', 		'frac' : 16},
	# {'name' : 'blanca', 		'frac' : 8},
	# {'name' : 'negra', 			'frac' : 4},
	{'name' : 'corchea', 		'frac' : 2},
	{'name' : 'semicorchea', 	'frac' : 1}
]

nota = [
	# {'name' : 'si4',	'freq' : 988},
	{'name' : 'la4', 	'freq' : 880},
	{'name' : 'sol4', 	'freq' : 784},
	{'name' : 'fa4', 	'freq' : 698},
	{'name' : 'mi4', 	'freq' : 659},
	{'name' : 're4', 	'freq' : 587},
	{'name' : 'do4', 	'freq' : 523},
	{'name' : 'si3', 	'freq' : 494},
	{'name' : 'la3', 	'freq' : 440},
	{'name' : 'sol3', 	'freq' : 392},
	# {'name' : 'fa3', 	'freq' : 349},
	# {'name' : 'mi3', 	'freq' : 330},
	# {'name' : 're3', 	'freq' : 294},
	# {'name' : 'do3', 	'freq' : 262}
]

tempo = 250 # mseg. por semicorcheas

print("Music Maker")
opcion = input("Start = 1\nEnd = 4\n-->")
while opcion != '4':
    index_freq = random.randrange(len(nota))
    index_frac = random.randrange(len(figura))
    print("Note = " + nota[index_freq]['name'] + " - Figure = " + figura[index_frac]['name'])
    winsound.Beep(nota[index_freq]['freq'], figura[index_frac]['frac']*tempo)
#----------------------------------------------------------------------------------------
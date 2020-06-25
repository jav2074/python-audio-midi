# import winsound
# frequency = 2000   #2500  # Set Frequency To 2500 Hertz
# duration = 1000     # Set Duration To 1000 ms == 1 second

#----------------------------------------------------------------------------------------
# winsound.Beep(frequency, duration)
# frequency += 10

# freq_array = [2000,2100,2200,2400,2500,2600,2700,2800,2900,3000]
# for freq in freq_array:
#     winsound.Beep(freq, duration)
# for freq in freq_array[::-1]:
#     winsound.Beep(freq, duration)

#----------------------------------------------------------------------------------------
# freq_1 = 20000
# freq_2 = 30000
# i = freq_1

# opcion = input("Para Iniciar ingrese 1\nPara Salir ingrese 4\n-->")
# while opcion != '4':
#     while i<freq_2:
#         print(i)
#         winsound.Beep(i, 500)
#         i += 100
#     while i>freq_1:
#         print(i)
#         winsound.Beep(i, 500)
#         i -= 100


# #----------------------------------------------------------------------------------------
# # randrange(10)                        # Integer from 0 to 9 inclusive
# import winsound
# import random

# freq_1 = 20000
# freq_2 = 30000

# print("Auyenta Mosquitos")
# opcion = input("Para Iniciar ingrese 1\nPara Salir ingrese 4\n-->")
# while opcion != '4':
#     frequency = freq_1 + random.randrange(10000)
#     duration = 500 + random.randrange(500)
#     print("frequency = " + str(frequency) + " Hz - duration = " + str(duration) + " miliseg")
#     winsound.Beep(frequency, duration)
# #----------------------------------------------------------------------------------------


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
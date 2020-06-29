#----------------------------------------------------------------------------------------
# randrange(10)                        # Integer from 0 to 9 inclusive
import winsound
import random

freq_1 = 20000
freq_2 = 30000
freq_range = freq_2 - freq_1
durat_1 = 500
durat_2 = 1500
durat_range = durat_1 - durat_2

print("Auyenta Mosquitos")
opcion = input("Para Iniciar ingrese 1\nPara Salir ingrese 4\n-->")
while opcion != '4':
    frequency = random.randint(freq_1, freq_2)	    # freq_1 + random.randrange(freq_range)
    duration =  random.randint(durat_1, durat_2)	# durat_1 + random.randrange(durat_range)
    print("frequencia = " + str(frequency) + " Hz - duracion = " + str(duration) + " miliseg")
    winsound.Beep(frequency, duration)
#----------------------------------------------------------------------------------------

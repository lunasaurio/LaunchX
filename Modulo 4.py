from ast import keyword
from pprint import PrettyPrinter


text = """Interesting facts about the Moon. The Moon is Earth's only satellite.There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
# Añade el código necesario

text_split = (text.split ('.'))
print (text_split)
# Define las palabras clave: average, temperature y distance suenan bien
keywords = ["average", "distance", "temperature"]

# Ciclo for para recorrer la cadena
for sentence in text_split:
    for key_word in keywords:
        if key_word in sentence:
            print (sentence)
            break

for sentence in text_split:
    for key_word in keywords:
        if key_word in sentence:
            print (sentence.replace('C','Celcius'))
            break

#Ejercicio 2 
# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

print ("Gravity facts about {}".format(name))
print ('--------------------------------------')
print ("Planet name: {}".format(planet))
print ("Gravity: {}".format(gravity * 1000))

planet = 'Marte '
gravity  = 0.00143
name = 'Ganímedes'

print ("Gravity facts about {}".format(name))
print ('--------------------------------------')
print ("Planet name: {}".format(planet))
print ("Gravity: {}".format(gravity * 1000))

#############################################

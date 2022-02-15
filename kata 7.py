import pprint
#solicitar las variables 
planets = []
new_planet = ''

#creando el ciclo while
while new_planet != 'done':
    if new_planet:
        planets.append (new_planet)
    new_planet = input ('Type the planets one by one')

print (planets)

#ciclo for
for planet in planets:
    print (planets)
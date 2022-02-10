planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupyter', 'Saturn', 'Neptune', 'Uranus']
print (planet_list)

planet_list.append ('Pluto')
print (planet_list)

user_planet = input ('De que planeta quieres saber información? Recuerda iniciar con mayúscula.')
planet_index= planet_list.index (user_planet)
print('Estos son los planetas más cercanos a {}'.format(user_planet))
print(planet_list[0:planet_index])

print('Estos son los planetas más lejanos a ' + user_planet)
print(planet_list [planet_index + 1:])
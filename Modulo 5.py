from matplotlib.image import pil_to_array


distance1= 149597870 
distance2 = 778547200
distance_between = distance2 - distance1
print (distance_between)

distance_miles = distance_between * 0.612
print (distance_miles)

print ("-----------------")

#ejercicio 2 
name = input ("Cual es el nombre del planeta?")
km = int (input("Cuál es la distancia?")) 
miles = km * 0.621 
print ("La distancia en millas de {} al sol es de {} millas.".format(name, (abs(miles))))

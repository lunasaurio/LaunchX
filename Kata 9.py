# Función para leer 3 tanques de combustible y muestre el promedio
# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))

from lib2to3.pgen2 import literals
from pyparsing import nums


def reporte(tanque1, tanque2, tanque3):
    promedio = (tanque1 + tanque2 + tanque3) / 3
    return f"""Fuel Report:
    Promedio: {promedio}%
    Tanque 1: {tanque1}%
    Tanque 2: {tanque2}%
    Tanque 3: {tanque3}% 
    """

print(reporte(75, 80, 85))

# Función promedio 
def promedio(valor):
    total = sum(valor)
    number_of_items = len(valor)
    return total / number_of_items

print (promedio ([75, 80, 85]))

#EJECRCICIO 2

def mission_report (prelaunchtime, flight_time, destiny, external_tank, internal_tank):
    return f""" 
    Mission to {destiny}.
    Flight time {flight_time}.
    Total travel time {prelaunchtime + flight_time}.    
    Total fuel in tanks {external_tank + internal_tank} liters.
    """

print (mission_report(10, 50, 'Mars', 10000, 20000))

#Hazlo más flexible permitiendo cualquier número de pasos basados en el tiempo y cualquier 
# número de tanques.

def mission_report (destiny,*minutes, **fuel):
    main =  f""" 
    Mission to {destiny}.
    Total travel time {sum(minutes)}minutes.    
    Total fuel in tanks {sum(fuel.values())} liters.
    """
    for tank_name, liters in fuel.items():
        main += f"{tank_name} tank --> {liters} liters left\n"
    return main

print (mission_report( "Mars", 10, 200, internal=20000, external = 10000))
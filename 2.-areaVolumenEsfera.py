import math
# Area y Volumen - Jessica Dórame 10932 29/01/25
# Asignacion 4.1, Calculo del area y volumen de una esfera segun el radio ingresado.

# Metodo que recibe el  radio de la esfera ingresado por el usuario, donde se hacen los calculos, regresando area y volumen
def Area_volumen(radio):
    area = 4 * math.pi * radio ** 2
    volumen = (4/3) * math.pi * radio ** 3
    return area, volumen 

radio = float(input("Introduce el radio de la esfera: ")) # Variable que recibe el radio de la essfera a calcular
area, volumen = Area_volumen(radio) # llamado del metdo para calcular, enviando de parametro el radio, el resultado se guardaen las varibles area y volumen

print(f"Área de la esfera: {area:.6f}") #m  mestra el resultado  llarea
print(f"Volumen de la esfera: {volumen:.6f}") # muestra el resultado del volumen.
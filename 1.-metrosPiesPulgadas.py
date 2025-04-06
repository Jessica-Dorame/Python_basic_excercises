# Conversiones - Jessica Dórame 10932 29/01/25
#Asignacion 4.2, Conversion ce metros a pies y pulgadas.

# Metodo donde recibe los metros a convertir 
def convertir(metros): 
    pies = metros * 3.28084  
    pulgadas = metros * 39.3701
    return pies, pulgadas # Regresa la conversion en pies y pulgadas

metros = float(input("Introduce la distancia en metros: ")) # Vaiable que recibe los metros ingresados por el usuario
pies, pulgadas = convertir(metros) # Llamado del metodo para convertir, enviando los metros ya ingresados  El resultaso se guarda en las variables pies y pulgadas

print(f"{metros} metros son {pies:.4f} pies y {pulgadas:.4f} pulgadas.") # Muestra el resultado


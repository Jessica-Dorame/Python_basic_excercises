# Cajera - Jessica Dórame 10932 29/01/25
# Asignacion 4.3, Retiro de billetes con las denominaciones mas altas teniendo siempre que sean multiplos de 50.

# Metodo que recibe el monto solicitado para el retiro, calcula la mayor cantidad de altas denominaciones para entregar
def calcular_billetes(monto):
    billetes = [1000, 500, 100, 50] 
    cantidad_billetes = {}

# Ciclo que busca entregar el monto con los biletes mas grandes
    for billete in billetes:
        cantidad = monto // billete
        if cantidad > 0:
            cantidad_billetes[billete] = cantidad
            monto -= cantidad * billete 
    return cantidad_billetes 

monto = int(input("Introduce el monto a retirar (múltiplo de 50): ")) # Variable que recibe el monto que el usuario desea retirar

if monto % 50 != 0: # Condicion para recibir solo cantidades multiplos de 50, mostrara el mensaje en caso de no ser asi
    print("El monto debe ser múltiplo de 50.")
else:
    billetes = calcular_billetes(monto) # Si cumple con el requisito, manda llamar al metodo para calcular las denominaciones.
    print("Billetes a entregar:")
    for billete, cantidad in billetes.items(): # ciclo para mostrar los billetes a entregar
        print(f"${billete}: {cantidad} billetes")
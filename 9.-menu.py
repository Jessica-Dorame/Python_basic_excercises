# Función que despliega el menú y lee la opción seleccionada
def menu():
    print("\nMenú de opciones:")
    print("I) Integrar")
    print("T) Tabular")
    print("S) Salir")
    opcion = input("Seleccione una opción (I/T/S): ").upper()
    return opcion

# Función que lee los límites de integración y el número de rectángulos
def leeDatosIntegración():
    xi = float(input("Introduce el valor de xi (límite inferior): "))
    xf = float(input("Introduce el valor de xf (límite superior): "))
    n = int(input("Introduce el número de rectángulos: "))
    return (xi, xf, n)

# Función que calcula el área bajo la curva utilizando integración por rectángulos
def integrar(xi, xf, n):
    # Calculamos el ancho de cada rectángulo
    dx = (xf - xi) / n
    area = 0
    for i in range(n):
        # Calculamos la altura de cada rectángulo usando el valor de x en el punto medio
        x = xi + (i + 0.5) * dx
        # Calculamos el valor de la función en ese punto
        y = x**3 - 2*x + 3
        # Sumamos el área de cada rectángulo
        area += y * dx
    return area

# Función que lee los límites inferior, superior y el incremento para la tabulación
def leeDatosTabulación():
    xi = float(input("Introduce el valor de xi (límite inferior): "))
    xf = float(input("Introduce el valor de xf (límite superior): "))
    incremento = float(input("Introduce el valor del incremento: "))
    return (xi, xf, incremento)

# Función que tabula la función y = x^3 - 2x + 3
def tabular(xi, xf, incremento):
    print("\nTabla de valores:")
    print(f"{'x':>10} {'y = x^3 - 2x + 3':>20}")
    print("-" * 32)
    x = xi
    while x <= xf:
        y = x**3 - 2*x + 3
        print(f"{x:10.4f} {y:20.4f}")
        x += incremento

# Código principal
if __name__ == "__main__":
    while True:
        opcion = menu()
        
        if opcion == 'I':  # Opción para integrar
            xi, xf, n = leeDatosIntegración()
            area = integrar(xi, xf, n)
            print(f"\nEl área bajo la curva entre {xi:.4f} y {xf:.4f} es: {area:.4f}")
        
        elif opcion == 'T':  # Opción para tabular
            xi, xf, incremento = leeDatosTabulación()
            tabular(xi, xf, incremento)
        
        elif opcion == 'S':  # Opción para salir
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

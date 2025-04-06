import silos

def obtener_datos():
    """Obtiene los datos del usuario"""
    tipo = input("Introduce el tipo de silo (C para Cilíndrico, E para Esférico): ").strip().upper()
    
    if tipo == "C":
        radio = float(input("Introduce el radio del silo cilíndrico: "))
        altura = float(input("Introduce la altura del silo cilíndrico: "))
        calibre = int(input("Introduce el calibre de la lámina (0 o 1): "))
        return tipo, radio, altura, calibre, None

    elif tipo == "E":
        radio = float(input("Introduce el radio del silo esférico: "))
        calibre = int(input("Introduce el calibre de la lámina (0 o 1): "))
        tipoBase = input("Introduce el tipo de base ('S' para Simple, 'R' para Reforzada): ").strip().upper()
        return tipo, radio, None, calibre, tipoBase

def calcular_y_mostrar(tipo, radio, altura, calibre, tipoBase):
    """Realiza los cálculos y muestra los resultados"""
    if tipo == "C":
        print()
        superficie = silos.superficieSiloCilindrico(radio, altura)
        volumen = silos.volumenSiloCilindrico(radio, altura)
        costo = silos.costoSiloCilindrico(radio, calibre)
        
        print(f"Superficie: {superficie:.2f} m²")
        print(f"Volumen: {volumen:.2f} m³")
        print(f"Costo: ${costo:.2f}")

    elif tipo == "E":
        print()
        superficie = silos.superficieSiloEsférico(radio)
        volumen = silos.volumenSiloEsférico(radio)
        costo = silos.costoSiloEsférico(superficie, calibre, tipoBase)
        
        print(f"Superficie: {superficie:.2f} m²")
        print(f"Volumen: {volumen:.2f} m³")
        print(f"Costo: ${costo:.2f}")

def main():
    """Función principal"""
    while True:
        tipo, radio, altura, calibre, tipoBase = obtener_datos()
        calcular_y_mostrar(tipo, radio, altura, calibre, tipoBase)
        
        respuesta = input("¿Deseas realizar otro cálculo? (S para Sí, N para No): ").strip().upper()
        if respuesta != 'S':
            print("¡Gracias por usar el programa!")
            break

if __name__ == "__main__":
    main()

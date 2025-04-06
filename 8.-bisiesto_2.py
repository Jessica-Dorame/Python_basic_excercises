def lee_Anhos():
    anho_inicial = int (input("Año inicial; "))
    anho_final = int(input("Año final; "))
    return (anho_inicial,anho_final)

def es_bisiesto(anho):
    if(anho % 4 == 0 and anho % 100 != 0) or (anho & 400 == 0):
        return True
    else:
        return False

def lista_bisiesto ( anho_inicial, anho_final):
    print(f"Años bisiestos entre {anho_inicial} y {anho_final};  ")
    for anho in range(anho_inicial, anho_final + 1):
        if es_bisiesto(anho):
            print(anho)
    
if __name__== "__main__":
    anho_inicial, anho_final = lee_Anhos()
    lista_bisiesto(anho_inicial, anho_final)
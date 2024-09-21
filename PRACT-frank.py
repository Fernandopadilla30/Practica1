def calcular_precio_entrada(edad):
    if edad < 4:
        return 0  
    elif 4 <= edad <= 18:
        return 5  
    else:
        return 10  

def main():
    try:
        edad = int(input("Introduce la edad del cliente: "))
        
        precio = calcular_precio_entrada(edad)
        
        if precio == 0:
            print("La entrada es gratuita.")
        else:
            print(f"El precio de la entrada es {precio}€.")
    except ValueError:
        print("Por favor, introduce una edad válida.")

if __name__ == "__main__":
    main()

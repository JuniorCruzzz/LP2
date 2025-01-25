def es_negativo():
    try:
        numero = int(input("Ingresa un número entero: "))
        if numero < 0:
            print(f"El número {numero} es negativo.")
        else:
            print(f"El número {numero} no es negativo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def contar_digitos():
    try:
        numero = int(input("Ingresa un número entero: "))
        cantidad_digitos = len(str(abs(numero)))
        print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def es_primo():
    try:
        numero = int(input("Ingresa un número entero: "))
        
        # Caso especial para números menores o iguales a 1
        if numero <= 1:
            print(f"El número {numero} no es primo.")
            return
        
        # Verificación de si el número es primo
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        
        if es_primo:
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} no es primo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def mayor_en_lista():
    try:
        numeros = []
        for i in range(4):
            num = int(input(f"Ingrese el número {i + 1}: "))
            numeros.append(num)
        mayor = max(numeros)
        posicion = numeros.index(mayor)
        print(f"El número mayor es {mayor} y está en la posición {posicion}.")
    except ValueError:
        print("Por favor, ingresa solo números válidos.")

def eliminar_duplicados():
    numeros = [1, 1, 2, 3, 3, 2, 5, 6, 2, 7, 8, 4, 3, 1]
    numeros_sin_duplicados = list(set(numeros))
    print(f"Lista sin duplicados: {numeros_sin_duplicados}")

def main():
    while True:
        print("\n--- Menú de Ejercicios ---")
        print("1. Determinar si un número es negativo")
        print("2. Contar los dígitos de un número")
        print("3. Verificar si un número es primo")
        print("4. Encontrar el mayor en una lista de 4 números")
        print("5. Eliminar duplicados de una lista")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        # Validación de entrada para asegurarse de que sea un número
        if not opcion.isdigit():
            print("Por favor, ingresa solo numeros.")
            continue
        
        opcion = int(opcion)
        
        if opcion == 1:
            es_negativo()
        elif opcion == 2:
            contar_digitos()
        elif opcion == 3:
            es_primo()
        elif opcion == 4:
            mayor_en_lista()
        elif opcion == 5:
            eliminar_duplicados()
        elif opcion == 6:
            print("Bye...")
            break
        else:
            print("Opcion no valida, intenta nuevamente.")

if __name__ == "__main__":
    main()

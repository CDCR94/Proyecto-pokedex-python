def letra_adyacente(letra):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    letra = letra.lower()  # Convertimos a minúscula para evitar problemas
    if letra not in alfabeto:
        print("⚠ La entrada no es una letra válida del alfabeto.")
        return
    
    indice = alfabeto.index(letra)
    
    # Letra anterior (si es la primera, tomamos la última)
    letra_anterior = alfabeto[indice - 1] if indice > 0 else alfabeto[-1]
    
    # Letra siguiente (si es la última, tomamos la primera)
    letra_siguiente = alfabeto[indice + 1] if indice < len(alfabeto) - 1 else alfabeto[0]
    
    print(f"Anterior: {letra_anterior} | Siguiente: {letra_siguiente}")

# Bucle infinito
while True:
    entrada = input("Ingrese una letra (o escriba 'salir' para terminar): ")
    
    if entrada.lower() == "salir":
        print("Programa finalizado. ¡Hasta luego!")
        break
    
    if len(entrada) != 1 or not entrada.isalpha():
        print("⚠ Por favor, ingrese solo una letra.")
        continue
    
    letra_adyacente(entrada)
import requests
import os
import json

def obtener_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: el Pokémon '{nombre}' no existe en la Pokédex.\n")
        return None

    data = response.json()

    # Extraer la información que pedimos
    info_pokemon = {
        "nombre": data["name"],
        "id": data["id"],
        "peso": data["weight"],
        "altura": data["height"],
        "tipos": [t["type"]["name"] for t in data["types"]],
        "habilidades": [h["ability"]["name"] for h in data["abilities"]],
        "movimientos": [m["move"]["name"] for m in data["moves"]],
        "imagen_frontal": data["sprites"]["front_default"]
    }

    # Mostrar datos en consola
    print(f"\n Pokémon encontrado: {info_pokemon['nombre'].capitalize()}")
    print(f"ID: {info_pokemon['id']}")
    print(f"Peso: {info_pokemon['peso']}")
    print(f"Altura: {info_pokemon['altura']}")
    print(f"Tipos: {', '.join(info_pokemon['tipos'])}")
    print(f"Habilidades: {', '.join(info_pokemon['habilidades'])}")
    print(f"Total de movimientos: {len(info_pokemon['movimientos'])}")
    print(f"Imagen: {info_pokemon['imagen_frontal']}")

    # Guardar en carpeta "pokedex"
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")

    ruta = os.path.join("pokedex", f"{info_pokemon['nombre']}.json")

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(info_pokemon, f, indent=4, ensure_ascii=False)

    print(f"\n Información guardada en: {ruta}\n")

    return info_pokemon


if __name__ == "__main__":
    while True:
        nombre = input("Ingresa el nombre de un Pokémon (o escribe 'salir' para terminar): ")

        if nombre.lower() == "salir":
            print(" Saliendo de la Pokédex. ¡Hasta luego!")
            break

        obtener_pokemon(nombre)
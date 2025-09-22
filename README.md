# Proyecto-pokedex-python
Pokedex usando la PokeAPI
# Pokédex en Python

Este es un proyecto en Python que implementa una Pokédex interactiva utilizando la API pública [PokéAPI](https://pokeapi.co/).  
El usuario puede buscar un Pokémon por su nombre, y el programa muestra su información relevante y guarda los datos en formato JSON.

---

## Funcionalidades
- Consulta datos de cualquier Pokémon existente en la PokéAPI.  
- Muestra:
  - Imagen frontal
  - Peso
  - Altura
  - Movimientos
  - Habilidades
  - Tipos
- Guarda la información en un archivo `.json` dentro de la carpeta `pokedex/`.  
- Manejo de errores si el Pokémon no existe.  
- El programa se ejecuta indefinidamente hasta que el usuario elija salir.

---

## Requisitos
Antes de ejecutar el proyecto, asegúrate de tener instalado Python (3.8 o superior) y la librería `requests`.

Instala las dependencias con:

```bash
pip install -r requirements.txt

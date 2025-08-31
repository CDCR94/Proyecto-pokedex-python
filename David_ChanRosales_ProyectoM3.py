import random
import matplotlib.pyplot as plt

def simular_canicas(n_canicas, niveles):
    """
    Simula la caída de n_canicas en una máquina de Galton con 'niveles' de obstáculos.
    Retorna una lista con la cantidad de canicas en cada contenedor.
    """
    # Inicializar contenedores
    contenedores = [0] * (niveles + 1)

    for _ in range(n_canicas):
        derecha = 0
        # Cada nivel decide izquierda (0) o derecha (1)
        for _ in range(niveles):
            if random.random() < 0.5:  # 50% probabilidad
                derecha += 1
        contenedores[derecha] += 1

    return contenedores


def graficar_histograma(resultados, niveles):
    """
    Grafica un histograma de los resultados de la simulación.
    """
    plt.bar(range(niveles + 1), resultados, color="skyblue", edgecolor="black")
    plt.xlabel("Contenedores")
    plt.ylabel("Número de canicas")
    plt.title(f"Simulación de Máquina de Galton ({sum(resultados)} canicas, {niveles} niveles)")
    plt.show()


# Parámetros
N_CANICAS = 3000
N_NIVELES = 12

# Simulación
resultados = simular_canicas(N_CANICAS, N_NIVELES)

# Gráfica
graficar_histograma(resultados, N_NIVELES)
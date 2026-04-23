# ------------------------------------------------------------
# Nombre del alumno: Lautaro Alegre
# Ejercicio 3 - Parte (b)
# Función: x(t) = cos(2πf1t) sin(2πf2t), f1 = 10 Hz, f2 = 15 Hz
# Objetivo: Simulación y graficación de la función en Python
# ------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def x_b(t: np.ndarray, f1: float = 10.0, f2: float = 15.0) -> np.ndarray:
    return np.cos(2 * np.pi * f1 * t) * np.sin(2 * np.pi * f2 * t)

def main() -> None:
    t = np.linspace(0, 0.1, 1000)
    y_b = x_b(t)

    plt.figure(figsize=(10, 6))
    plt.plot(t, y_b, "-", linewidth=1.5)
    plt.title("(b) x(t) = cos(2πf1t) sin(2πf2t), f1 = 10 Hz, f2 = 15 Hz")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("x(t)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
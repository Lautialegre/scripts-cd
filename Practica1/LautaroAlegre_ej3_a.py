# ------------------------------------------------------------
# Nombre del alumno: Lautaro Alegre
# Ejercicio 3 - Parte (a)
# Función: x(t) = cos^2(2πft), f = 10 Hz
# Objetivo: Simulación y graficación de la función en Python
# ------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def x_a(t: np.ndarray, f: float = 10.0) -> np.ndarray:
    return np.cos(2 * np.pi * f * t) ** 2

def main() -> None:
    t = np.linspace(0, 0.1, 1000)
    y_a = x_a(t)

    plt.figure(figsize=(10, 6))
    plt.plot(t, y_a, "-", linewidth=1.5)
    plt.title("(a) x(t) = cos^2(2πft), f = 10 Hz")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("x(t)")
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    main()
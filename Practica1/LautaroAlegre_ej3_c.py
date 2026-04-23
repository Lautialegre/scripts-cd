# ------------------------------------------------------------
# Nombre del alumno: Lautaro Alegre
# Ejercicio 3 - Parte (c)
# Función: x(t) = 5 e^{-j2πft} | f = 20 Hz
# Objetivo: Simulación y graficación de la función en Python
# ------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def x_c(t: np.ndarray, f: float = 20.0) -> np.ndarray:
    return 5 * np.exp(-1j * 2 * np.pi * f * t)

def main() -> None:
    t = np.linspace(0, 0.1, 1000)
    y_c = x_c(t)

    plt.figure(figsize=(10, 6))
    plt.plot(t, np.real(y_c), label="Re{x(t)}", linewidth=1.5)
    plt.plot(t, np.imag(y_c), label="Im{x(t)}", linestyle="--", linewidth=1.5)
    plt.title("(c) x(t) = 5 e^{-j2πft}, f = 20 Hz")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt

def pulso_rectangular(t):
    """Pulso rectangular con ancho de 1 centrado en cero."""
    return np.where(np.abs(t) <= 0.5, 1.0, 0.0)


def senal_generatriz(t_val):
    """Generatriz x_g(t) desplazada según el inciso c."""
    return pulso_rectangular((t_val - 1/4) / (1/2))


def construir_senal_periodica(t, periodo):
    """Construye la señal periódica sumando réplicas desplazadas."""
    x = np.zeros_like(t)
    for k in range(-10, 11):
        x += senal_generatriz(t - k * periodo)
    return x


def energia_generatriz():
    """Energía de un pulso rectangular de base 1 y altura 1."""
    return 1/2


def potencia_periodica(energia, periodo):
    """Potencia de la señal periódica como energía dividida por el periodo."""
    return energia / periodo


T = 2
# Tiempo extendido para visualizar varias repeticiones
t = np.linspace(-2, 3 * T, 2000)

x_generatriz = senal_generatriz(t)
x_periodica = construir_senal_periodica(t, T)

energia_g = energia_generatriz()
potencia_p = potencia_periodica(energia_g, T)

print("=== Ejercicio 4c ===")
print(f"Energía de la señal generatriz: {energia_g}")
print(f"Potencia de la señal periódica: {potencia_p}")

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x_generatriz, 'b', linewidth=2, label='Generatriz $x_g(t)$')
plt.title('Señal Generatriz - Inciso c')
plt.xlabel('Tiempo (t)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, x_periodica, 'r', linewidth=2, label='Periódica $x_p(t)$')
plt.title(f'Señal Periódica (Período T={T})')
plt.xlabel('Tiempo (t)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

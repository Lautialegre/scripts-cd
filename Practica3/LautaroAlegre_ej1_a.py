"""
Práctica 3 - Fourier
Ejercicio 1.a
Alumno: Lautaro Alegre
"""

import numpy as np
import matplotlib.pyplot as plt

# Datos de la señal
T = 2.0
tau = 1.0
f0 = 1 / T
N_terms = [1, 3, 5, 15]

n_max = 13
ns = np.arange(-n_max, n_max + 1)
Xn = (tau / T) * np.sinc(ns * tau / T)


def rectangulo(t, T, tau):
    """Tren de pulsos rectangulares centrado en 0."""
    t0 = ((t + T / 2) % T) - T / 2
    return np.where(np.abs(t0) < tau / 2, 1.0, 0.0)


def aprox_fourier(t, T, tau, N):
    x = np.full_like(t, tau / T)
    for n in range(1, N + 1):
        an = (tau / T) * np.sinc(n * tau / T)
        x += 2 * an * np.cos(2 * np.pi * n * f0 * t)
    return x


t = np.linspace(-3, 5, 5000)
x_original = rectangulo(t, T, tau)

fig, axes = plt.subplots(2, 2, figsize=(12, 7))
fig.suptitle('Ej. 2.a - Señal original y aproximación Fourier', fontsize=13)

for ax, N in zip(axes.flatten(), N_terms):
    x_aprox = aprox_fourier(t, T, tau, N)
    ax.plot(t, x_original, 'k', linewidth=1.5, label='Original')
    ax.plot(t, x_aprox, 'r--', linewidth=1.3, label=f'N = {N}')
    ax.set_title(f'{N} armónicos')
    ax.set_xlabel('t [s]')
    ax.set_ylabel('x(t)')
    ax.set_ylim(-0.3, 1.3)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig('LautaroAlegre_ej1_a_aproximacion.png', dpi=150)
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
fig.suptitle('Ej. 2 - Espectro de Fourier', fontsize=13)

axes[0].stem(ns * f0, Xn, basefmt=' ', linefmt='b', markerfmt='bo')
axes[0].set_title('Coeficientes $X_n$')
axes[0].set_xlabel('f [Hz]')
axes[0].set_ylabel('$X_n$')
axes[0].axhline(0, color='k', linewidth=0.5)
axes[0].axvline(0, color='k', linewidth=0.5)
axes[0].grid(alpha=0.3)

axes[1].stem(ns * f0, np.abs(Xn), basefmt=' ', linefmt='b', markerfmt='bo')
axes[1].set_title('Amplitud $|X_n|$')
axes[1].set_xlabel('f [Hz]')
axes[1].set_ylabel('$|X_n|$')
axes[1].axhline(0, color='k', linewidth=0.5)
axes[1].axvline(0, color='k', linewidth=0.5)
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('LautaroAlegre_ej1_a_espectro.png', dpi=150)
plt.show()

print('Coeficientes de Fourier para n = -5..5')
print('   n | f [Hz] |    X_n')
print('-------------------------')
for n in range(-5, 6):
    xn = (tau / T) * np.sinc(n * tau / T)
    print(f'{n:3d} | {n * f0:6.3f} | {xn:8.4f}')

print()
print('Observaciones:')
print('- El tren de pulsos es par, así que la serie queda en cosenos.')
print('- El espectro de amplitud es el mismo que |X_n|.')
print('- La envolvente sigue una sinc, por eso hace falta varios armónicos.')

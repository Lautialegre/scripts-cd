"""
Práctica 3 - Fourier
Ejercicio 2.a — Parseval y reconstrucción
Alumno: Lautaro Alegre
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros
T = 2.0
tau = 1.0
f0 = 1/T

# Potencia directa (integral) — para tren rectangular P = τ/T
P_directa = tau / T
print('Teorema de Parseval — tren rectangular')
print(f'Potencia directa: P = {P_directa:.6f} W')

# Potencia por Parseval: P = X_0^2 + 2 Σ |X_n|^2
def Xn(n):
    return (tau/T) * np.sinc(n * tau/T)

N_max = 500   # muchos términos para convergencia
P_parseval = Xn(0)**2
potencias_acum = [Xn(0)**2]
ns_positivos = list(range(1, N_max + 1))

for n in ns_positivos:
    P_parseval += 2 * Xn(n)**2
    potencias_acum.append(P_parseval)

print(f'Potencia por Parseval (N={N_max}): P = {P_parseval:.6f} W')
print(f'Error relativo: {abs(P_parseval - P_directa)/P_directa * 100:.4f}%')

# Convergencia: potencia acumulada vs N
ns_graf = np.arange(0, N_max + 1)
porcentaje = np.array(potencias_acum) / P_directa * 100

# Encuentra N para 90%, 95%, 99%
for umbral in [90, 95, 99, 99.5]:
    idx = np.argmax(porcentaje >= umbral)
    n_umbral = ns_graf[idx]
    print(f'{umbral}% de potencia con N = {n_umbral}')

# Figura: convergencia de Parseval
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
fig.suptitle('Teorema de Parseval — Tren rectangular τ=1, T=2', fontsize=13)

ax = axes[0]
ax.plot(ns_graf[:20], porcentaje[:20], 'b-o', markersize=5)
ax.axhline(100, color='gray', linestyle='--', linewidth=0.8, label='100%')
ax.axhline(95,  color='r',    linestyle='--', linewidth=0.8, label='95%')
ax.axhline(90,  color='orange', linestyle='--', linewidth=0.8, label='90%')
ax.set_title('Potencia acumulada vs N')
ax.set_xlabel('N (número de armónicos)')
ax.set_ylabel('% de potencia total')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_ylim(40, 105)

# Figura: espectro de potencia |X_n|^2
n_esp = 13
ns_esp = np.arange(-n_esp, n_esp + 1)
Pot = np.array([Xn(n)**2 for n in ns_esp])

ax = axes[1]
ax.stem(ns_esp * f0, Pot, basefmt=' ', linefmt='b', markerfmt='bo')
ax.set_title('Espectro de potencia $|X_n|^2$')
ax.set_xlabel('f [Hz]')
ax.set_ylabel('$|X_n|^2$')
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0, color='k', linewidth=0.5)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('LautaroAlegre_ej2_a_parseval.png', dpi=150)
plt.show()

# Figura: reconstrucción (Fourier) vs señal original
def reconstruccion(t, T, tau, N):
    f0 = 1/T
    x = np.full_like(t, tau/T)
    for n in range(1, N + 1):
        an = (tau/T) * np.sinc(n * tau/T)
        x = x + 2 * an * np.cos(2 * np.pi * n * f0 * t)
    return x

def tren_rect(t, T, tau):
    tn = ((t + T/2) % T) - T/2
    return np.where(np.abs(tn) < tau/2, 1.0, 0.0)

t = np.linspace(-2, 4, 5000)
x_orig = tren_rect(t, T, tau)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
fig.suptitle('Reconstrucción por Fourier vs señal original', fontsize=13)

for ax, N in zip(axes, [3, 5, 15]):
    x_rec = reconstruccion(t, T, tau, N)
    
    # Potencia de la reconstrucción
    P_rec = Xn(0)**2 + sum(2*Xn(n)**2 for n in range(1, N+1))
    pct   = P_rec / P_directa * 100

    ax.plot(t, x_orig, 'k-',  linewidth=1.8, label='Original')
    ax.plot(t, x_rec,  'r--', linewidth=1.3, alpha=0.85, label=f'N={N}')
    ax.set_title(f'N={N} → P={pct:.1f}% de $P_{{total}}$')
    ax.set_xlabel('t [s]')
    ax.set_ylabel('x(t)')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-0.5, 1.5)
    ax.axhline(0, color='k', linewidth=0.5)

plt.tight_layout()
plt.savefig('LautaroAlegre_ej2_a_reconstruccion.png', dpi=150)
plt.show()

# Resumen en consola
print()
print('Potencia por armónico')
print(f"{'N':>4} | {'P acumulada':>12} | {'% del total':>11}")
print('-' * 35)
P_ac = Xn(0)**2
print(f"{'DC':>4} | {P_ac:>12.6f} | {P_ac/P_directa*100:>10.2f}%")
for n in [1, 3, 5, 7, 9]:
    P_ac += 2*Xn(n)**2
    print(f"{n:>4} | {P_ac:>12.6f} | {P_ac/P_directa*100:>10.2f}%")
 
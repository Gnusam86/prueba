import numpy as np
import matplotlib.pyplot as plt

# 1. Generar tiempo
tiempo = np.linspace(0, 10, 50)

# 2. Definir funciones
def mru(t, v):
    return [v * x for x in t]

def mrua(t, x0, v0, a):
    return [x0 + v0*x + 0.5*a*(x**2) for x in t]

def libre(t):
    return [np.sin(x) for x in t]  # Ejemplo: función seno

# 3. Calcular posiciones
pos_mru = mru(tiempo, 2)
pos_mrua = mrua(tiempo, 0, 1, 0.5)
pos_libre = libre(tiempo)

# 4. Graficar
plt.plot(tiempo, pos_mru, 'b--o', label='MRU v=2 m/s')
plt.plot(tiempo, pos_mrua, 'g-.s', label='MRUA a=0.5 m/s²')
plt.plot(tiempo, pos_libre, 'r-', label='Función libre: seno')
plt.title("Comparación de funciones")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")
plt.grid(True)
plt.legend()
plt.show()

# 5. Calcular dominio y rango
def imprimir_dom_ran(nombre, datos_t, datos_x):
    dominio = (min(datos_t), max(datos_t))
    rango = (min(datos_x), max(datos_x))
    print(f"{nombre} -> Dominio: {dominio[0]} a {dominio[1]} s | Rango: {rango[0]} a {rango[1]} m")

imprimir_dom_ran("MRU", tiempo, pos_mru)
imprimir_dom_ran("MRUA", tiempo, pos_mrua)
imprimir_dom_ran("Libre", tiempo, pos_libre)

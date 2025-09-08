import matplotlib.pyplot as plt
import numpy as np

#Generar datos simulados
tiempo = np.linspace(0, 10, 100)  # segundos
posicion = [2*t for t in tiempo]  # metros

# Graficar con estilo
plt.plot(tiempo, posicion, marker='s', color='red', linestyle=':', markersize=3)
plt.title("Posición vs. Tiempo", fontsize=14, fontweight='bold')
plt.xlabel("Tiempo (s)", fontsize=12)
plt.ylabel("Posición (m)", fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

#Calcular dominio y rango
dominio = (min(tiempo), max(tiempo))
rango = (min(posicion), max(posicion))
#impresion descriptiva
print(f"Dominio: desde t = {dominio[0]}s hasta t = {dominio[1]}s")
print(f"Rango: desde posición = {rango[0]}m hasta posición = {rango[1]}m")
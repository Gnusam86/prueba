import matplotlib.pyplot as plt

# Datos simulados
tiempo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # segundos
posicion = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # metros

# Graficar
plt.plot(tiempo, posicion, marker='o', color='blue')
plt.title("Posición vs. Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")
plt.grid(True)
plt.show()

# Análisis de dominio y rango
dominio = (min(tiempo), max(tiempo))
rango = (min(posicion), max(posicion))

print("Dominio:", dominio)
print("Rango:", rango)
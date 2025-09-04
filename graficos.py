import matplotlib.pyplot as plt
x = [1, 5, 3, 4, 5]
y = [2, 3, 6, 9, 11]
plt.plot(x, y, marker='o')
plt.title("Gráfico de ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.show()
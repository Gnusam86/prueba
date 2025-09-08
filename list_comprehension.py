cuadrados = [x**2 for x in range(10)]
print(cuadrados)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

pares = [x for x in range(10) if x % 2 == 0]
print(pares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

tiempo = [t for t in range(11)]  # segundos
aceleracion = 1.5  # m/s^2
posicion = [0.5 * aceleracion * t**2 for t in tiempo]  # metros
print(posicion)

palabra = "transversalidad"
vocales = [letra for letra in palabra if letra in 'aeiou']
print(vocales)

pares = [(x, x**2 - 4*x + 3)for x in range(-5,6)]
print(pares)
# Output: [(-5, 48), (-4, 27), (-3, 12), (-2, 3), (-1, 0), (0, 3), (1, 0), (2, -1), (3, 0), (4, 3), (5, 8)]
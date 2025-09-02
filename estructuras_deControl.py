numero = 10
if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print("El número es cero.")

frutas = ["manzana", "pera", "banana", "sandia"]
for fruta in frutas:
    print(f"Me gusta la fruta: {fruta}")

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
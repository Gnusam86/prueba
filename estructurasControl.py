# Definimos la función
def f(x):
    return (x**2 - 4) / (x - 2)

# --- 1. Valores acercándose a 2 desde la izquierda ---
# Usamos un paso pequeño para ver mejor el comportamiento
valores_izq = [1.5 + i*0.05 for i in range(0, 11)]  # de 1.5 a 2.0
# Excluimos el 2.0 para evitar división por cero
valores_izq = [x for x in valores_izq if x != 2]

# Calculamos f(x) para cada valor
resultados_izq = [f(x) for x in valores_izq]

# Mostramos resultados
print("Aproximación a x = 2 desde la IZQUIERDA:")
for x, y in zip(valores_izq, resultados_izq):
    print(f"x = {x:.2f} → f(x) = {y:.4f}")

print("\n" + "-"*50 + "\n")

# --- 2. Valores acercándose a 2 desde la derecha ---
valores_der = [2.5 - i*0.05 for i in range(0, 11)]  # de 2.5 a 2.0
valores_der = [x for x in valores_der if x != 2]

resultados_der = [f(x) for x in valores_der]

print("Aproximación a x = 2 desde la DERECHA:")
for x, y in zip(valores_der, resultados_der):
    print(f"x = {x:.2f} → f(x) = {y:.4f}")
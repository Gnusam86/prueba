def f(x):
    if x == 2:
        return float('nan')  # or return None, or a message indicating undefined
    return (x**2 - 4)/(x - 2)
valores = [1.5 + i*0.05 for i in range(0, 11)]  # x → 2 desde la izquierda (x < 2)
# Generar valores que se acercan a 2 desde la izquierda
valores = [1.5 + i*0.05 for i in range(0, 21)]  # x → 2

# Calcular f(x) para cada valor
resultados = [f(x) for x in valores]

# Mostrar resultados
for x, y in zip(valores, resultados):
    print(f"x = {x:.2f} → f(x) = {y:.4f}")

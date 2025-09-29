import random  # Para generar avances aleatorios

# Posiciones iniciales
pos_tortuga1 = 0
pos_tortuga2 = 0

# Meta
meta = 20

# Turno inicial
turno = 1

# Bucle: se repite mientras ninguna tortuga haya llegado
while pos_tortuga1 < meta and pos_tortuga2 < meta:
    print(f"\n--- Turno {turno} ---")
    
    # Avance aleatorio de cada tortuga
    avance1 = random.randint(1, 3)
    avance2 = random.randint(1, 3)
    
    pos_tortuga1 += avance1
    pos_tortuga2 += avance2
    
    # Barra de progreso: "=" repetido según la posición
    barra1 = "=" * pos_tortuga1
    barra2 = "=" * pos_tortuga2
    
    print(f"Tortuga 1: {barra1} ({pos_tortuga1} m)")
    print(f"Tortuga 2: {barra2} ({pos_tortuga2} m)")
    
    # Comprobamos si alguna llegó a la meta
    if pos_tortuga1 >= meta and pos_tortuga2 >= meta:
        print("\n🏁 ¡Empate! Las dos llegaron a la meta.")
        break
    elif pos_tortuga1 >= meta:
        print("\n🏆 ¡Tortuga 1 gana la carrera!")
        break
    elif pos_tortuga2 >= meta:
        print("\n🏆 ¡Tortuga 2 gana la carrera!")
        break
    
    turno += 1  # Pasamos al siguiente turno
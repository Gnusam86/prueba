menu = {
    1: ("Hamburguesa", 50),
    2: ("Pizza", 80),
    3: ("Ensalada", 40),
    4: ("Agua", 15)
}

# 1. Función para mostrar el menú
def mostrar_menu():
    print("\n🍔 Bienvenido al Restaurante Digital 🍔")
    for key, (item, price) in menu.items():
        print(f"{key}. {item} - ${price}")
    print("0. Salir")

# 2. Función para obtener el precio según la opción
def obtener_precio(opcion):
    if opcion in menu:
        return menu[opcion][1]
    else:
        return 0

# 3. Función para calcular el total con descuento
def calcular_total(cuenta):
    if cuenta >= 150:
        print("🎉 ¡Felicidades! Tienes un 10% de descuento.")
        return cuenta * 0.9
    else:
        return cuenta

# --- Programa principal ---
cuenta = 0
while True:
    mostrar_menu()
    try:
        opcion = int(input("Elige una opción (0-4): "))
        
        # Validar opción
        if opcion == 0:
            break
        elif opcion < 0 or opcion > 4:
            print("⚠️ Opción inválida. Intenta de nuevo.")
            continue
        
        # Sumar al total
        cuenta = cuenta + obtener_precio(opcion)
        print(f"Has añadido {menu[opcion][0]} a tu cuenta. Total actual: ${cuenta}")
    
    except ValueError:
        print("⚠️ Error: Debes escribir un número entero.")

# Mostrar total final
print("\nSubtotal:", cuenta)
print("Total a pagar:", calcular_total(cuenta))
print("🍽️ ¡Gracias por tu visita!")
# 1. Función para mostrar el menú
def mostrar_menu():
    print("\n🍔 Bienvenido al Restaurante Digital 🍔")
    print("1. Hamburguesa - $50")
    print("2. Pizza - $80")
    print("3. Ensalada - $40")
    print("4. Agua - $15")
    print("0. Terminar pedido")

# 2. Función para obtener el precio según la opción
def obtener_precio(opcion):
    if opcion == 1:
        return 50
    elif opcion == 2:
        return 80
    elif opcion == 3:
        return 40
    elif opcion == 4:
        return 15
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
        print("✅ Producto agregado. Subtotal:", cuenta)
    
    except ValueError:
        print("⚠️ Error: Debes escribir un número entero.")

# Mostrar total final
print("\nSubtotal:", cuenta)
print("Total a pagar:", calcular_total(cuenta))
print("🍽️ ¡Gracias por tu visita!")


def saludar(nombre):
    """Saluda al usuario."""
    print(f"¡Hola, {nombre}!")

def calcular_doble(numero):
    """Calcula el doble de un número."""
    return numero * 2


if __name__ == "__main__":
    print("🌟 Bienvenido al programa básico 🌟")
    
    # Pide datos al usuario
    nombre_usuario = input("¿Cómo te llamas? ")
    numero_usuario = float(input("Ingresa un número: "))
    
    # Llama a las funciones
    saludar(nombre_usuario)
    resultado = calcular_doble(numero_usuario)
    
    print(f"El doble de {numero_usuario} es: {resultado}")
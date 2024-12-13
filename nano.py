
print ("hola te damos la bienvenida al sistema operativo que te ayudara a realizar tus tareas de manera eficiente una contraseña segura ")
import random
import string

def generar_contraseña(longitud, mayusculas, minusculas, alfanumericos, simbolos):
    caracteres = ""
    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if alfanumericos:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Error: No se seleccionaron tipos de caracteres."
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

    return contraseña
def mostrar_menu():
    print("Bienvenido al generador de contraseñas seguras.")
    print("Este generador crea contraseñas seguras basadas en tus preferencias.")
    print("Selecciona las opciones a continuación para crear tu contraseña.")
    print("\Opciones:")
    print("1. Longitud de la contraseña")
    print("2. Incluir mayúsculas")
    print("3. Incluir minúsculas")
    print("4. Incluir caracteres alfanuméricos")
    print("5. Incluir símbolos")
    print("6. Generar contraseña")
    print("7. Salir")

def main():
    longitud = 8 
    mayusculas = False
    minusculas = False
    alfanumericos = False
    simbolos = False
while True:
    mostrar_menu()
    opcion = input("\\Selecciona una opción: ")

    if opcion == "1":
        longitud = int(input("Introduce la longitud deseada de la contraseña: "))

    elif opcion == "2":
        mayusculas = input("¿Incluir mayúsculas? (si/no): ").strip().lower() == "si"

    elif opcion == "3":
        minusculas = input("¿Incluir minúsculas? (si/no): ").strip().lower() == "si"

    elif opcion == "4":
        alfanumericos = input("¿Incluir caracteres alfanuméricos? (si/no): ").strip().lower() == "si"

    elif opcion == "5":
        simbolos = input("¿Incluir simbolos? (si/no): ").strip().lower() == "si"

    elif opcion == "6":
        contraseña = generar_contraseña(longitud, mayusculas, minusculas, alfanumericos, simbolos)
        print(f"\\Contraseña generada: {contraseña}")

    elif opcion == "7":
        print("¡Gracias por usar el generador de contraseñas! ¡Adiós!")
        break

    else:
        print("Opción no válida, por favor selecciona una opción correcta.")

    otra = input("\\n¿Quieres generar otra contraseña? (si/no): ").strip().lower()
    if otra != "si":
        break


        if __name__ == "**main**":main()
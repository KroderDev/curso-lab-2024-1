from mascota_virtual import MascotaVirtual
import os
import time
import pickle

def limpiar_consola():
    # Limpia la consola para Windows, Mac y Linux
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def guardar_mascota(mascota):
    with open('mascota.pkl', 'wb') as file:
        pickle.dump(mascota, file)
    print("Estado de la mascota guardado.")

def cargar_mascota():
    try:
        with open('mascota.pkl', 'rb') as file:
            mascota = pickle.load(file)
        print("Estado de la mascota cargado.")
        return mascota
    except FileNotFoundError:
        print("No se encontró un archivo guardado. Creando una nueva mascota.")
        return None

def main():
    mascota = cargar_mascota()
    if mascota is None:
        nombre = input("Introduce el nombre de tu mascota: ")
        mascota = MascotaVirtual(nombre)
    
    while True:
        limpiar_consola()
        print(mascota.estado())
        
        print("\n¿Qué quieres hacer con tu mascota?")
        print("1. Alimentar")
        print("2. Jugar")
        print("3. Descansar")
        print("4. Curar")
        print("5. Limpiar")
        print("6. Guardar y salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            mascota.alimentar()
        elif opcion == '2':
            mascota.jugar()
        elif opcion == '3':
            mascota.descansar()
        elif opcion == '4':
            mascota.curar()
        elif opcion == '5':
            mascota.limpiar()
        elif opcion == '6':
            guardar_mascota(mascota)
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")
        
        mascota.actualizar_estado()
        time.sleep(1)  # Pausa para simular el paso del tiempo

if __name__ == "__main__":
    main()

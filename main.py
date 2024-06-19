import os 
import globales
import ventas
os.system("cls")

def menu_general():
    while True:
        os.system("cls")
        print("1. Precargar Ventas")
        print("2. Crear Ventas")
        print("3. Reportes de Sueldos")
        print("4. Ver Estadísticas")
        print("5. Salir")

        opcion = globales.seleccionar_opcion(5)

        if opcion == 1:
            print("1. Precargar Ventas")
            ventas.precargar_ventas()
        elif opcion == 2:
            print("2. Crear Ventas")
        elif opcion == 3:
            print("3. Reportes de Sueldos")
        elif opcion == 4:
            print("4. Ver Estadísticas")
        elif opcion == 5:
            print("5. Salir")
            return
        input()
        
if __name__ == "__main__":
    menu_general()
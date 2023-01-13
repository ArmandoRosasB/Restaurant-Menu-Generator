import os
from Database_creator.restaurante_db_tools import *

if __name__ == '__main__':
    
    # Crear la base de datos
    crear_bd()

    # Menu de opciones del programa
    while True:
        print('\n\nBienvenido al gestor del restaurante!')
        print('\nIntroduce una opcion')
        print('[1] Agregar una categoria')
        print('[2] Agregar un plato')
        print('[3] Mostrar Menu')
        print('[4] Salir')
        opcion = input('\nIntroduce la opcion deseada: ')

        if opcion == '1':
            agregar_categoria()

        elif opcion == '2':
            agregar_plato()
        
        elif opcion == '3':
            mostrar_menu()

        elif opcion == '4':
            break
        else:
            print('\nOpcion no valida')

        os.system('pause')
        os.system('cls')

    print("Nos vemos!")


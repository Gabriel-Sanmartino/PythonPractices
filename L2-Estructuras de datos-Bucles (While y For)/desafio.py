# >>> ¡En busqueda del tesoro! <<<

# Definimos variables para coordenadas de busqueda:
t, z = 0, 0

# Definimos las coordenadas del tesoro
tesoro_t, tesoro_z = 2, 3

# Mensaje de inicio de busqueda
print("¡Adelante, Encuentra el tesoro!")

# Definimos bucle while que se ejectura mientras no se indiquen las coordenadas correctas
while (t, z) != (tesoro_t, tesoro_z):
    # Mensaje de movimiento
    movimiento = input("Ingresa: Arriba/Abajo/Izquiera/Derecha para desplazarte: ").lower() # "lower" convierte el texto ingresado a mayuscula
    # modificamos los valores de t y z segundo el moviento indicado
    if movimiento=="izquierda":
        t-=1
        print(f'Te encuentras en las siguientes coordenadas: {t,z}')
    elif movimiento=="derecha":
        t+=1
        print(f'Te encuentras en las siguientes coordenadas: {t,z}')
    elif movimiento=="arriba":
        z+=1
        print(f'Te encuentras en las siguientes coordenadas: {t,z}')
    elif movimiento=="abajo":
        z-=1
        print(f'Te encuentras en las siguientes coordenadas: {t,z}')
    else:
        print('Movimiento invalido')
else:
    print(f'¡Felicidades has encontrado el tesoro!')
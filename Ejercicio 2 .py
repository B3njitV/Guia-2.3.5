while True:
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")

    print("Ingrese producto y cantidad")
    producto = input("Nombre del producto: ")
    cantidad = input("Cantidad: ")

    confirmacion = input("¿Está seguro que desea pagar? ('s' o 'n'): ")

    if nombre.strip() == "" or telefono.strip() == "" or producto.strip() == "" or cantidad.strip() == "" or confirmacion.strip().lower() != 's':
        print("\nFaltan datos por ingresar o la confirmación es incorrecta. Por favor, chequee la información ingresada.\n")
        print("Nombre:", nombre)
        print("Teléfono:", telefono)
        print("Producto:", producto, "Cantidad:", cantidad)
        print("\nVuelva a comenzar\n")
    else:
        print("\n¡Pago procesado con éxito!")
        break  # Salir del bucle cuando la confirmación sea 's'

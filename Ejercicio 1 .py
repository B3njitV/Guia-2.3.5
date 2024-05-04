def realizar_encuesta():
    # Inicializar el puntaje total
    puntaje_total = 0
    
    # Realizar las 12 preguntas y sumar los puntos
    for i in range(1, 13):
        respuesta = input("Por favor, responda la pregunta {}: ".format(i))
        # Validar que la respuesta sea un número entre 0 y 9
        while not respuesta.isdigit() or int(respuesta) < 0 or int(respuesta) > 9:
            respuesta = input("Por favor, ingrese un número válido entre 0 y 9: ")
        puntaje_total += int(respuesta)
    
    # Devolver el puntaje total
    return puntaje_total

def categorizar_alumno(puntaje):
    # Categorizar al alumno según su puntaje
    if puntaje >= 0 and puntaje <= 3:
        return "Usted es un alumno de buen desempeño"
    elif puntaje >= 4 and puntaje <= 6:
        return "Usted es un alumno que puede mejorar"
    elif puntaje >= 7 and puntaje <= 9:
        return "Usted es un alumno con algunos desafíos"
    else:
        return "Usted es un alumno con muchos desafíos"

def main():
    print("Bienvenido al Centro de Psicología del Estudiante")
    print("Por favor, responda las siguientes preguntas con un número entre 0 y 9")
    
    # Realizar la encuesta
    puntaje = realizar_encuesta()
    
    # Categorizar al alumno según su puntaje
    categoria = categorizar_alumno(puntaje)
    
    # Mostrar la categoría
    print("\n{}".format(categoria))

if __name__ == "__main__":
    main()



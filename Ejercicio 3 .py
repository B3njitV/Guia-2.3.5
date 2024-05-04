def jugar_aventura():
    print("Juego: La gran aventura. Puedes moverte a la derecha 'd', a la izquierda 'a' o hacia adelante 'w'.\n")
    print("Inicia la aventura.\n")
    
    print("Corres hacia la montaña nevada. Un ruido te detiene.")
    movimiento = input("(muévete hacia algún lado): ")

    if movimiento.lower() == 'a':
        print("Ves un gran oso que comienza a avanzar hacia ti. Te quedas muy quieto. Después de un momento te comienzas a deslizar hacia un lado.")
        movimiento = input("Te mueves hacia la izquierda y una planta carnívora te come.\n")
    elif movimiento.lower() == 'd':
        print("Te pierdes en el bosque y encuentras una cueva misteriosa.")
        movimiento = input("Te aventuras dentro de la cueva y encuentras un tesoro.\n")
    elif movimiento.lower() == 'w':
        print("Encuentras un camino que conduce a una playa desierta.")
        movimiento = input("Camina por la playa y descubres un barco pirata abandonado.\n")
    else:
        print("Movimiento no válido. Fin de la partida.")
        return
    
    print("Fin de la partida. Muchas gracias por jugar.")

def main():
    jugar_aventura()

if __name__ == "__main__":
    main()

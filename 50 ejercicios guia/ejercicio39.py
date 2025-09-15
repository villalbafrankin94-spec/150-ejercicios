def inicio():
    print("\n Bienvenido al Bosque de las Decisiones s")
    print("Te despiertas en medio de un bosque misterioso. Hay dos caminos frente a ti.")
    print("1. Tomar el camino de la izquierda (hacia el río)")
    print("2. Tomar el camino de la derecha (hacia la montaña)")
    eleccion = input("¿Qué camino eliges? (1/2): ")

    if eleccion == "1":
        camino_rio()
    elif eleccion == "2":
        camino_montaña()
    else:
        print(" Opción inválida.")
        inicio()

def camino_rio():
    print("\n Caminas hacia el río y ves una barca abandonada.")
    print("1. Subirte a la barca")
    print("2. Seguir caminando por la orilla")
    eleccion = input("¿Qué haces? (1/2): ")

    if eleccion == "1":
        print("\n La barca te lleva a una isla secreta llena de tesoros. ¡Final feliz!")
    elif eleccion == "2":
        print("\n Tropiezas con una serpiente venenosa. No logras escapar.  Final trágico.")
    else:
        print(" Opción inválida.")
        camino_rio()

def camino_montaña():
    print("\n Subes por la montaña y encuentras una cabaña con humo saliendo de la chimenea.")
    print("1. Entrar a la cabaña")
    print("2. Rodearla y seguir subiendo")
    eleccion = input("¿Qué haces? (1/2): ")

    if eleccion == "1":
        print("\n Una anciana te ofrece sopa y refugio. Descansas y sobrevives. 🏡 Final pacífico.")
    elif eleccion == "2":
        cima_montaña()
    else:
        print(" Opción inválida.")
        camino_montaña()

def cima_montaña():
    print("\n Llegas a la cima y ves una luz brillante en el cielo.")
    print("1. Investigar la luz")
    print("2. Ignorarla y buscar un camino de regreso")
    eleccion = input("¿Qué haces? (1/2): ")

    if eleccion == "1":
        print("\n Te abducen unos extraterrestres y te llevan a otro planeta.  Final inesperado.")
    elif eleccion == "2":
        print("\n Encuentras un mapa antiguo y logras volver a casa. 🏠 Final aventurero.")
    else:
        print(" Opción inválida.")
        cima_montaña()

inicio()

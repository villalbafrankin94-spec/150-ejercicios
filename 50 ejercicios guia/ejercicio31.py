import random

class Animal:
    def __init__(self, nombre, energia=100, posicion_x=0, posicion_y=0):
        self.nombre = nombre
        self.energia = energia
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.vivo = True

    def mover(self):
        if self.vivo:
            self.posicion_x += random.randint(-1, 1)
            self.posicion_y += random.randint(-1, 1)
            self.energia -= 5
            if self.energia <= 0:
                self.vivo = False
                print(f"💀 {self.nombre} murió de agotamiento.")
           

    def esta_vivo(self):
        return self.vivo

    def __str__(self):
        estado = "Vivo" if self.vivo else "Muerto"
        return f"{self.nombre} ({self.__class__.__name__}) - Energía: {self.energia}, Pos: ({self.posicion_x},{self.posicion_y}), Estado: {estado}"

class Presa(Animal):
    def __init__(self, nombre, energia=100, posicion_x=0, posicion_y=0):
        super().__init__(nombre, energia, posicion_x, posicion_y)
        self.tipo = "presa"

    def comer(self):
        if self.vivo:
            self.energia += 20 
            if self.energia > 100: self.energia = 100
            

class Depredador(Animal):
    def __init__(self, nombre, energia=100, posicion_x=0, posicion_y=0):
        super().__init__(nombre, energia, posicion_x, posicion_y)
        self.tipo = "depredador"

    def cazar(self, presa):
        if self.vivo and presa.esta_vivo() and self.distancia_a(presa) <= 1: 
            self.energia += 50 
            if self.energia > 100: self.energia = 100
            presa.vivo = False
            print(f"🍖 {self.nombre} cazó a {presa.nombre}. Energía: {self.energia}")
            return True
        return False

    def distancia_a(self, otro_animal):
        return abs(self.posicion_x - otro_animal.posicion_x) + abs(self.posicion_y - otro_animal.posicion_y)

class Ecosistema:
    def __init__(self, ancho=10, alto=10):
        self.ancho = ancho
        self.alto = alto
        self.animales = []

    def agregar_animal(self, animal):
        animal.posicion_x = random.randint(0, self.ancho - 1)
        animal.posicion_y = random.randint(0, self.alto - 1)
        self.animales.append(animal)
        print(f"➕ {animal.nombre} ({animal.tipo}) agregado en ({animal.posicion_x},{animal.posicion_y})")

    def simular_paso(self):
        print("\n--- Nuevo Paso de Simulación ---")
        random.shuffle(self.animales) 

        for animal in self.animales:
            if not animal.esta_vivo():
                continue

            animal.mover()

            if isinstance(animal, Presa):
                animal.comer() 

            elif isinstance(animal, Depredador):
                presas_cercanas = [p for p in self.animales if isinstance(p, Presa) and p.esta_vivo() and animal.distancia_a(p) <= 2]
                if presas_cercanas:
                    presa_elegida = random.choice(presas_cercanas)
                    animal.cazar(presa_elegida)

        
        self.animales = [a for a in self.animales if a.esta_vivo()]

        self.mostrar_estado()

    def mostrar_estado(self):
        print("\nEstado actual del ecosistema:")
        if not self.animales:
            print("El ecosistema está vacío.")
            return
        for animal in self.animales:
            print(f"  {animal}")
        print(f"Total de animales vivos: {len(self.animales)}")


ecosistema = Ecosistema(ancho=5, alto=5)
ecosistema.agregar_animal(Presa("Conejo1"))
ecosistema.agregar_animal(Presa("Conejo2"))
ecosistema.agregar_animal(Depredador("Lobo1"))
ecosistema.agregar_animal(Presa("Conejo3"))

for i in range(5): 
    ecosistema.simular_paso()
    if not ecosistema.animales:
        print("El ecosistema colapsó.")
        break
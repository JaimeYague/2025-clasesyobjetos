import random
from guerreros import Guerrero

class Traje:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Traje de color: {self.color}"


class Juego:
    def __init__(self):
        self.rangers = []

        self.crear()
        self.presentar()
        self.pelear()
        self.descansar()
        self.presentar()

    def crear(self):
        colores = [
            Traje("rojo"),
            Traje("verde"),
            Traje("azul"),
            Traje("amarillo"),
            Traje("rosa")
        ]

        for i in range(5):
            color = colores.pop(0)
            vida = 3
            self.rangers.append(Guerrero(color=color, id=i, vida=vida))
            # self.rangers.append(Guerrero(color, i, vida))

        return self.rangers

    def presentar(self):
        for ranger in self.rangers:
            print(ranger.presentar())

    def pelear(self):
        for _ in range(3):
            for ranger in self.rangers:
                if random.randint(0, 1) == 1:
                    ranger.herir()

        self.rangers[3].herir(5)

        for ranger in self.rangers:
            if ranger.vida <= 0:
                print(f"El ranger {ranger.id} esta muerido")

    def descansar(self):
        print("Los Rangers descansan:")
        for ranger in self.rangers:
            print(ranger.descansar())


Juego()

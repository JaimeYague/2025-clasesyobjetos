# from animales import Perro, Larva, Gremlin
from random import randint
from animales import *


def caosZoologico():
    firulais = Perro("Firulais", "ChowChow")
    firulais.come()
    firulais.pasea()

    mizgo = Larva("Mizgo")
    mizgo.come()

    gizmo = Gremlin("Gizmo")
    gizmo.come()

    firulais.registrar()
    gizmo.registrar()

    sardinilla = Caballo("Sardinilla")
    sardinilla.come()
    sardinilla.cargar(6)













    mrEd = Caballo("Mr. Ed")
    if mrEd.cargar(randint(10, 40)):
        mrEd.transportar("Barcelona")
        carga = mrEd.descargar()
        print(f"El caballo descargo {carga} kilos")











if __name__ == "__main__":
    caosZoologico()

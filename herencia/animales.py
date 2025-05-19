from animal import Animal


class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def pasea(self):
        print(f"El Perro {self.raza} llamado {self.nombre} se pasea")


class Caballo(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.registrar()
        self.max = 5
        self.carga = 0

    def cargar(self, carga):
        self.carga = carga
        if self.carga > self.max:
            print(f"El caballo {self.nombre} va sobrecargado")


# Larva sobrescribe el método
class Larva(Animal):
    def come(self):
        self.comidas += 0.1
        print("Me fabrica seda")
        print("La Larva SE TRANFORMA en mariposa")


# Gremiln EXTIENDE el método
class Gremlin(Animal):
    def come(self):
        super().come()                  # Primero ejecuta el comportamiento del super
        print("Gremlin se TRANSFORMA")  # Luego expande la funcionalidad


<<<<<<< Updated upstream
class Caballo(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.max = 30
        self.peso = 0

    def transportar(self, destino):
        print(f"El caballo transportó la carga a {destino}")

    def cargar(self, peso):
        if peso > self.max:
            print(f"{self.nombre} se niega a cargar ({peso}) kilos")
            return False
        self.peso = peso
        return True

    def descargar(self):
        return self.peso

# Composición: Los atributos del Guerrero son otro objeto
class Guerrero:
    def __init__(self, color, id, vida):
        self.color = color
        self.id = id
        self.vida_max = vida
        self.vida = self.vida_max

    def presentar(self):
        return f"Soy el ranger {self.color} y tengo {self.vida} vidas"

    def herir(self, cantidad=1):
        self.vida -= cantidad
        if self.vida <= 0:
            print(f" * El guerrero {self.color} se ha muerido")
        else:
            print(f" * Al guerrero {self.color} aun le quedan {self.vida} vidas")

    def descansar(self):
        if self.vida <= 0:
            return f"El Guerrero {self.color} esta descansando ETERNAMENTE"

        if self.vida < self.vida_max:
            self.vida = self.vida_max

        return f"El Guerrero {self.color} ha descansado"
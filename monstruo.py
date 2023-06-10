from random import choice

class monstruo:
    def __init__(self):
        self.posicion = (None, None)
        self.personaje = "👹"
        self.vida: int = 100
    def movimiento(self):
        movimiento = ["izq","der","arr","abj"]

        dato = choice(movimiento)

        if dato == "izq":
            return (self.posicion[0], self.posicion[1]-1)
        elif dato == "der":
            return (self.posicion[0], self.posicion[1] + 1)
        elif dato == "arr":
            return  (self.posicion[0]-1, self.posicion[1])
        else:
            return (self.posicion[0]+1, self.posicion[1])


    def aumentar_vida(self):
        self.vida += 10
    def disminuir_vida(self):
        self.vida -= 25

    def cambiar_posicion(self,fila,columa):
        self.posicion = (fila,columa)

    def esta_muerto(self):
        if self.vida <= 0:
            return True
        return False
class jugador:
    def __init__(self):
        self.posicion = (None,None)
        self.personaje = "🧑🏻"
        self.vida: int = 50
        self.arma_activa = False

    def aumentar_vida(self):
        self.vida += 10
    def disminuir_vida(self):
        self.vida -= 25

    def cambiar_posicion(self,fila,columa):
        self.posicion = (fila,columa)

    def movimiento(self,dato):

        if dato == "izq":
            return (self.posicion[0], self.posicion[1]-1)
        elif dato == "der":
            return (self.posicion[0], self.posicion[1] + 1)
        elif dato == "arr":
            return  (self.posicion[0]-1, self.posicion[1])
        else:
            return (self.posicion[0]+1, self.posicion[1])


    def es_movimiento(self,dato):
        movimientos = ["arr","abj","der","izq"]
        if dato in movimientos:
            return True
        return False


    def es_atacar(self,dato):
        if dato == "sonreir":
            return True
        return False

    def guardar_arma_inventario(self):
        self.arma_activa = True

    def esta_muerto(self):
        if self.vida <= 0:
            return True
        return False





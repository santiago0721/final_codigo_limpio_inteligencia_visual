
from random import *



class mapa:
    def __init__(self,tamaño:int):
        self.tamaño = tamaño
        self.tablero = []
        self.crear_mapa(tamaño)
        self.agregar_beneficios()

    def crear_mapa(self,tamaño):
        for filas in range(tamaño):
            self.tablero.append([])
            for columnas in range(tamaño):
                self.tablero[filas].append([" "])

    def print_mapa(self):
        for i in self.tablero:
            print(i)

    def agregar_beneficios(self):
        self.armas = ["🔫","🗡️","🛠️"]
        self.comidas = ["🍔","🌮","🍟"]
        self.agregar_al_mapa(self.armas)
        self.agregar_al_mapa(self.comidas)


    def agregar_al_mapa(self,data:list):

        cantidad = randrange(1,self.tamaño)
        contador = 0

        while True:
            if contador == cantidad:
                break
            dato_agregar = randrange(len(data))
            fila = randrange(self.tamaño)
            columna = randrange(self.tamaño)

            if self.tablero[fila][columna] == [" "]:
                self.tablero[fila][columna] = [data[dato_agregar]]
                contador +=1

    def agregar_personaje(self,personaje):
        while True:
            fila = randrange(self.tamaño)
            columna = randrange(self.tamaño)

            if self.tablero[fila][columna] == [" "]:
                self.tablero[fila][columna] = [personaje.personaje]
                personaje.posicion = (fila,columna)
                break

    def ubi_comida(self,fila,columna):
        if self.tablero[fila][columna] in self.comidas:
            return True
        return False

    def ubi_armas(self,fila,columna):
        if self.tablero[fila][columna] in self.armas:
            return True
        return False

    def ubi_vacia(self,fila,columna):
        if self.tablero[fila][columna] == [" "]:
            return True
        return False

    def moverse_en_el_mapa(self,fila,columna,personaje):
        if self.tablero[fila][columna] == [" "]:
            self.tablero[fila][columna] = [personaje.personaje]
        else:
            self.tablero[fila][columna] += [personaje.personaje]

    def limpiar_casilla(self,fila,columna,personaje):
        if len(self.tablero[fila][columna]) >1:
            self.tablero[fila][columna].remove(personaje.personaje)
        else:
            self.tablero[fila][columna] = [" "]

    def hay_beneficios(self,fila,columna):
        if len(self.tablero[fila][columna]) > 1:
            if self.tablero[fila][columna][0] in self.armas or self.tablero[fila][columna][0] in self.comidas:
                return True

        return False

    def hay_comidas(self,fila,columna):
        if self.tablero[fila][columna][0] in self.comidas:
            return True
        return False



    def eliminar_beneficio(self,fila,columna):
        self.tablero[fila][columna].pop(0)


    def enemigo_cerca(self,fila,columna,enemigo):

        arr = fila - 1
        abj = fila + 1
        der = columna + 1
        izq = columna - 1

        if self.pos_valida(arr):
            if self.tablero[arr][columna] == [enemigo]:
                return True

        if self.pos_valida(abj):
            if self.tablero[abj][columna] == [enemigo]:
                return True

        if self.pos_valida(izq):
            if self.tablero[fila][izq] == [enemigo]:
                return True

        if self.pos_valida(der):
            if self.tablero[fila][der] == [enemigo]:
                return True

        return False



    def pos_valida(self,pos):
        if pos >= 0 and pos < self.tamaño:
            return True
        return False

    """def limpiar_casilla(self,fila,columna,personaje):
        if len(self.tablero[fila][columna]) >1:
            self.tablero[fila][columna].remove(personaje.personaje)
        else:
            self.tablero[fila][columna] = [" "]"""

    def enemigo_en_pos_actual(self,fila,columna,enemigo):
        if enemigo in self.tablero[fila][columna]:
            return True
        else:
            return False

    def vaciar_casilla(self,fila,columna):
        self.tablero[fila][columna] = [" "]



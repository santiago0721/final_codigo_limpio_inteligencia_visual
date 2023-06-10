from jugador import *
from mapa import *
from monstruo import *
from inteligencia_visual import *


class juego:
    def __init__(self):
        self.inteligencia_visual = inteligenciaVisual()
        self.jugador = jugador()
        self.monstruo = monstruo()
        self.iniciar_mapa()
        self.jugar()

    def iniciar_mapa(self):
        #cambiar aleatorio

        tamaño_mapa = self.inteligencia_visual.tamaño_tablero()
        self.mapa = mapa(tamaño_mapa)
        self.mapa.agregar_personaje(self.jugador)
        self.mapa.agregar_personaje(self.monstruo)
        self.mapa.print_mapa()

    def turno_monstruo(self):
        print("""
        turno monstruo
        """)

        while True:
            pos_actual = self.monstruo.posicion
            nueva_pos = self.monstruo.movimiento()
            if nueva_pos[0] >= 0 and nueva_pos[1] >= 0 and nueva_pos[0] < self.mapa.tamaño and nueva_pos[1] < self.mapa.tamaño:
                break

        if self.mapa.ubi_comida(nueva_pos[0],nueva_pos[1]):
            self.monstruo.aumentar_vida()
            self.mapa.vaciar_casilla(pos_actual[0], pos_actual[1])

        if self.mapa.ubi_vacia(nueva_pos[0],nueva_pos[1]) or self.mapa.ubi_armas(nueva_pos[0],nueva_pos[1]):
            self.mapa.vaciar_casilla(pos_actual[0],pos_actual[1])

        if self.mapa.enemigo_en_pos_actual(nueva_pos[0],nueva_pos[1],self.jugador.personaje):
            self.jugador.disminuir_vida()


        self.mapa.moverse_en_el_mapa(nueva_pos[0], nueva_pos[1], self.monstruo)

        self.mapa.limpiar_casilla(pos_actual[0], pos_actual[1],self.monstruo)


        self.monstruo.cambiar_posicion(nueva_pos[0],nueva_pos[1])
        self.mapa.print_mapa()



    def turno_jugador(self):
        print(""""
        turno jugador
        """)
        while True:
            if self.inteligencia_visual.confirmacion_siguiente_movimiento():

                accion = self.inteligencia_visual.movimientos()
                if self.jugador.es_movimiento(accion):
                    if self.movimiento_jugador(accion):
                        break
                    else:
                        print("no se puede realizar este movimiento, haga otro movimiento valido")
                elif self.jugador.es_atacar(accion):
                    if self.atacar():
                        break
                    else:
                        print("no se puede atacar")
                else:
                    if self.beneficios_jugador():
                        break
                    else:
                        print("en esta posición no se encuentra ningún beneficio")

            else:
                return False # para terminar el juego
        self.mapa.print_mapa()
        return True



    def movimiento_jugador(self,dato):
        nueva_pos = self.jugador.movimiento(dato)
        if nueva_pos[0] >= 0 and nueva_pos[1] >= 0 and nueva_pos[0] < self.mapa.tamaño and nueva_pos[1] < self.mapa.tamaño:

            self.mapa.moverse_en_el_mapa(nueva_pos[0], nueva_pos[1], self.jugador)
            fila_actual, columna_actual = self.jugador.posicion
            self.mapa.limpiar_casilla(fila_actual, columna_actual, self.jugador)
            self.jugador.cambiar_posicion(nueva_pos[0], nueva_pos[1])
            if self.mapa.enemigo_en_pos_actual(nueva_pos[0],nueva_pos[1],self.monstruo.personaje):
                self.jugador.disminuir_vida()
            return True
        return False



    def beneficios_jugador(self):
        fila,columna = self.jugador.posicion

        if self.mapa.hay_beneficios(fila,columna):

            if self.mapa.hay_comidas(fila,columna):

                self.jugador.aumentar_vida()

            else:
                self.jugador.guardar_arma_inventario()

            self.mapa.eliminar_beneficio(fila,columna)
            return True
        return False


    def atacar(self):
        fila_actual,columna_actual = self.jugador.posicion
        if self.mapa.enemigo_cerca(fila_actual,columna_actual,self.monstruo.personaje):
            if self.jugador.arma_activa:
                self.monstruo.disminuir_vida()
                return True

        return False



    def jugar(self):
        while True:
            self.marcador()
            if self.turno_jugador():
                self.turno_monstruo()
                if not self.fin_juego():
                    break
            else:
                print("juego terminado por el usuario.")
                break


    def marcador(self):
        print(f""" 
            vida jugador [{self.jugador.vida}]       vida monstruo [{self.monstruo.vida}] 
        """)


    def fin_juego(self):
        if self.monstruo.esta_muerto():
            print("fin del juego !! ganó el jugador")
            return False
        elif self.jugador.esta_muerto():
            print("fin del juego !! perdio el jugador")
            return False
        else:
            return True







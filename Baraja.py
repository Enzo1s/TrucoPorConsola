import random


class Baraja():

    jerarquia = {"1 DE ESPADA": 14, "1 DE BASTO": 13, "7 DE ESPADA": 12, "7 DE ORO": 11,
                 "3 DE ESPADA": 10, "3 DE COPA": 10, "3 DE ORO": 10, "3 DE BASTO": 10, "2 DE ESPADA": 9,
                 "2 DE COPA": 9, "2 DE ORO": 9, "2 DE BASTO": 9, "1 DE COPA": 8, "1 DE ORO": 8,
                 "12 DE ESPADA": 7, "12 DE COPA": 7, "12 DE ORO": 7, "12 DE BASTO": 7,
                 "11 DE ESPADA": 6, "11 DE COPA": 6, "11 DE ORO": 6, "11 DE BASTO": 6,
                 "10 DE ESPADA": 5, "10 DE COPA": 5, "10 DE ORO": 5, "10 DE BASTO": 5,
                 "7 DE COPA": 4, "7 DE BASTO": 4, "6 DE ESPADA": 3, "6 DE COPA": 3,
                 "6 DE ORO": 3, "6 DE BASTO": 3, "5 DE ESPADA": 2, "5 DE COPA": 2,
                 "5 DE ORO": 2, "5 DE BASTO": 2, "4 DE ESPADA": 1, "4 DE COPA": 1, "4 DE ORO": 1, "4 DE BASTO": 1
                 }
    valorCarta = {"1 DE ESPADA": 1, "1 DE BASTO": 1, "7 DE ESPADA": 7, "7 DE ORO": 7,
                  "3 DE ESPADA": 3, "3 DE COPA": 3, "3 DE ORO": 3, "3 DE BASTO": 3, "2 DE ESPADA": 2,
                  "2 DE COPA": 2, "2 DE ORO": 2, "2 DE BASTO": 2, "1 DE COPA": 1, "1 DE ORO": 1,
                  "12 DE ESPADA": 0, "12 DE COPA": 0, "12 DE ORO": 0, "12 DE BASTO": 0,
                  "11 DE ESPADA": 0, "11 DE COPA": 0, "11 DE ORO": 0, "11 DE BASTO": 0,
                  "10 DE ESPADA": 0, "10 DE COPA": 0, "10 DE ORO": 0, "10 DE BASTO": 0,
                  "7 DE COPA": 7, "7 DE BASTO": 7, "6 DE ESPADA": 6, "6 DE COPA": 6,
                  "6 DE ORO": 6, "6 DE BASTO": 6, "5 DE ESPADA": 5, "5 DE COPA": 5,
                  "5 DE ORO": 5, "5 DE BASTO": 5, "4 DE ESPADA": 4, "4 DE COPA": 4, "4 DE ORO": 4, "4 DE BASTO": 4}

    def __init__(self):  # Constructor de baraja
        # SE USA LISTA PARA PODER MEZCLAR CON TUPLA NO PODRIAMOS.
        self.mazo = ["1 DE ESPADA", "1 DE COPA", "1 DE ORO", "1 DE BASTO",
                     "2 DE ESPADA", "2 DE COPA", "2 DE ORO", "2 DE BASTO",
                     "3 DE ESPADA", "3 DE COPA", "3 DE ORO", "3 DE BASTO",
                     "4 DE ESPADA", "4 DE COPA", "4 DE ORO", "4 DE BASTO",
                     "5 DE ESPADA", "5 DE COPA", "5 DE ORO", "5 DE BASTO",
                     "6 DE ESPADA", "6 DE COPA", "6 DE ORO", "6 DE BASTO",
                     "7 DE ESPADA", "7 DE COPA", "7 DE ORO", "7 DE BASTO",
                     "10 DE ESPADA", "10 DE COPA", "10 DE ORO", "10 DE BASTO",
                     "11 DE ESPADA", "11 DE COPA", "11 DE ORO", "11 DE BASTO",
                     "12 DE ESPADA", "12 DE COPA", "12 DE ORO", "12 DE BASTO"]
        random.shuffle(self.mazo)  # desordena

    def mostrar(self):  # muestra las cartas en baraja PARA CONTROLAR QUE SE MEZCLEN BIEN
        for elemento in self.mazo:
            print(elemento)

    def repartir(self, jugadores):  # Modifocar o Abregar mas metodos
        reparte = jugadores*3
        dar = []
        for ele in range(0, reparte):
            dar.append(self.mazo[ele])
        return dar
# Volver a barajar mazo

    def mezclar(self):
        random.shuffle(self.mazo)

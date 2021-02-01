# Un objeto player es una lista con id de jugador, nombre del jugador y una lista de la mano
class Player():
    def __init__(self, nombre, idjugador, equipo):
        self.mano = []
        self.manoenv = []
        self.nombre = nombre
        self.idjugador = idjugador
        self.equipo = equipo

    def verMano(self):
        i = 0
        for elemento in self.mano:
            if i == 0:
                print("a ", elemento)
            elif i == 1:
                print("b ", elemento)
            else:
                print("c ", elemento)
            i += 1

    def tomar(self, carta):
        self.mano.append(carta)
        self.manoenv.append(carta)

    def jugar(self, opc):
        while True:
            if opc in ["a", "b", "c"]:
                if opc == "a":
                    return self.mano.pop(0)
                elif opc == "b":
                    return self.mano.pop(1)
                elif opc == "c":
                    return self.mano.pop(2)


class Bot(Player):  # Hay que hacer herencia
    def __init__(self, nombre, idjugador, equipo):
        super().__init__(nombre, idjugador, equipo)

    def verMano(self):
        super().verMano()

    def tomar(self, carta):
        super().tomar(carta)

    def jugar(self, opc):
        return super().jugar(opc)

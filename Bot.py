from Baraja import Baraja
from Player import *
from Funciones import *
from random import randint


def ordenarCartas(mano):  # ordeno de menor a mayor la mano
    for i in range(len(mano)-1):
        if Baraja.jerarquia[mano[i]] >= Baraja.jerarquia[mano[i+1]]:
            aux = mano[i+1]
            mano[i+1] = mano[i]
            mano[i] = aux


# devuelve la mejor carta de la mano. podría reemplazarse usando la lista ordenada
def miMejorCarta(mano):
    mayor = mano[0]
    for i in mano:
        if Baraja.jerarquia[i] > Baraja.jerarquia[mayor]:
            mayor = i
    return mayor


def miPeorCarta(mano):
    menor = mano[0]
    for i in mano:
        if Baraja.jerarquia[i] < Baraja.jerarquia[menor]:
            menor = i
    return menor


def mayorCarta(equipo):
    mayor = "4 DE COPA"
    for i in range(0, len(equipo)):
        for j in range(0, 3):
            if Baraja.jerarquia[equipo[i].mano[j]] >= Baraja.jerarquia[mayor]:
                mayor = equipo[i].mano[j]
    print("La mejor carta del equipo es ", mayor)
    return mayor


def cantoBot(puntosMano, falta, canto2):  # envido
    if falta == False:
        if puntosMano in [27, 28]:
            if randint(0, 10) <= 6:
                return canto2.index("Quiero")
            else:
                return canto2.index("No Quiero")
        if puntosMano in [29, 30, 31]:
            if randint(0, 10) <= 6:
                return canto2.index("Quiero")
            else:
                if "Envido" in canto2:
                    return canto2.index("Envido")
                elif "Real Envido" in canto2:
                    return canto2.index("Real Envido")
                elif puntosMano == 31:
                    return canto2.index("Quiero")
                else:
                    return canto2.index("No Quiero")
        if puntosMano in [32, 33]:
            if randint(0, 10) < 8:
                if "Real Envido" in canto2:
                    return canto2.index("Real Envido")
                elif "Falta Envido" in canto2:
                    return canto2.index("Falta Envido")
                else:
                    return canto2.index("Quiero")
            elif(randint(0, 20)+puntosMano) % 2 == 0:
                if "Falta Envido" in canto2:
                    return canto2.index("Falta Envido")
                else:
                    return canto2.index("Quiero")
        if puntosMano in [24, 25, 26]:
            if randint(0, 10) <= 6:  # empeiza a mentir
                if "Real Envido" in canto2:
                    return canto2.index("Quiero")
                elif "Envido" in canto2:
                    return canto2.index("Envido")
                else:
                    return canto2.index("No Quiero")
            elif(randint(0, 20)+puntosMano) % 2 == 0:
                return canto2.index("Quiero")
            else:
                return canto2.index("No Quiero")
        if puntosMano < 24:
            if randint(0, 20) >= 12:
                return canto2.index("Quiero")
            else:
                return canto2.index("No Quiero")
    else:
        if puntosMano in [31, 32]:
            if randint(0, 10) <= 9:
                return canto2.index("Quiero")
            else:
                return canto2.index("No Quiero")
        elif puntosMano == 33:
            return canto2.index("Quiero")
        # Miente en base de que el resultado de la operación esté en ese rango
        elif ((puntosMano*2)+3)/4 in range(1, 5):
            return canto2.index("Quiero")
        else:
            return canto2.index("No Quiero")


def trucoBot(bot, paratruco):

    manoactual = []
    for i in bot.manoenv:
        manoactual.append(i)
    cartaMayor = miMejorCarta(manoactual)
    cartaMala = miPeorCarta(manoactual)
    if len(manoactual) == 3:
        manoactual.remove(cartaMayor)  # Uso para buscar la carta media
        manoactual.remove(cartaMala)
        cartaMedia = manoactual[0]
    else:
        cartaMedia = cartaMala
    if paratruco[1][1] == "Nada" and Baraja.jerarquia[cartaMayor] >= 9 and Baraja.jerarquia[cartaMedia] >= 9:  # tiene almenos 2 dos
        if randint(0, 10) % 2 == 0:
            return "Truco"
        else:
            return "Jugar"
    # agregar opcion por si es mayor que 7 incluido
    elif paratruco[1][1] == "Nada" and Baraja.jerarquia[cartaMayor] >= 7 and Baraja.jerarquia[cartaMedia] >= 7:
        if randint(0, 10) % 2 == 0:
            return "Truco"
        else:
            return "Jugar"
    elif paratruco[1][1] == "Nada":
        return "Jugar"
    if paratruco[1][0] == "E2":  # analizar solo los quiero
        if paratruco[1][1] == "Truco" and Baraja.jerarquia[cartaMayor] >= 9 and Baraja.jerarquia[cartaMedia] >= 9:
            if randint(0, 10) % 2 == 0:
                return "Quiero"
            elif Baraja.jerarquia[cartaMayor] >= 10 or Baraja.jerarquia[cartaMedia] >= 10:
                return "Retruco"
            else:
                return "No Quiero"

        if paratruco[1][1] == "Vale 4" and paratruco[0] == 4:
            if Baraja.jerarquia[cartaMayor] >= 12 or Baraja.jerarquia[cartaMedia] >= 10:
                if randint(0, 10) % 2 == 0:
                    return "Quiero"
                else:
                    return "No Quiero"
            elif Baraja.jerarquia[cartaMayor] >= 9 or Baraja.jerarquia[cartaMedia] >= 9:
                return "Quiero"
            else:
                return "No Quiero"
        if paratruco[1][1] == "Retruco" and paratruco[0] == 3:
            if Baraja.jerarquia[cartaMayor] >= 10 or Baraja.jerarquia[cartaMedia] >= 10:
                if randint(0, 10) % 2 == 0:
                    return "Quiero"
                else:
                    return "Vale 4"
            elif randint(0, 10) % 2 == 0:
                return "Quiero"
            else:
                return "No Quiero"

        if paratruco[1][1] == "Quiero" and paratruco[0] == 2:
            if Baraja.jerarquia[cartaMayor] >= 10 or Baraja.jerarquia[cartaMedia] >= 9:
                if randint(0, 10) % 2 != 0:
                    return "Retruco"
                else:
                    return "Jugar"
            elif randint(0, 10) % 2 == 0:
                return "Retruco"
            else:
                return "Al Mazo"
        if paratruco[1][1] == "Quiero" and paratruco[0] == 3:
            if Baraja.jerarquia[cartaMayor] >= 10 or Baraja.jerarquia[cartaMedia] >= 9:
                if randint(0, 10) % 2 != 0:
                    return "Vale 4"
                else:
                    return "Jugar"
            elif randint(0, 10) % 2 == 0:
                return "Vale 4"
            else:
                return "Al Mazo"
    if paratruco[1][0] == "E1":
        if paratruco[1][1] == "Truco" and Baraja.jerarquia[cartaMayor] >= 9 and Baraja.jerarquia[cartaMedia] >= 9:
            if randint(0, 10) <= 6:
                return "Quiero"
            elif Baraja.jerarquia[cartaMayor] >= 10 or Baraja.jerarquia[cartaMedia] >= 10:
                return "Retruco"
            else:
                return "No Quiero"
        elif paratruco[1][1] == "Truco":
            if randint(0, 10) <= 6:
                return "Quiero"
            elif Baraja.jerarquia[cartaMayor] >= 10 or Baraja.jerarquia[cartaMedia] >= 10:
                return "Retruco"
            else:
                return "No Quiero"
        if paratruco[1][1] == "Quiero" and paratruco[0] == 2:
            if Baraja.jerarquia[cartaMayor] >= 10 or Baraja.jerarquia[cartaMedia] >= 9:
                if randint(0, 10) <= 7:
                    return "Retruco"
                else:
                    return "Jugar"
            elif randint(0, 10) <= 4:
                return "Retruco"
            else:
                return "No Quiero"
        if paratruco[1][1] == "Retruco" and paratruco[0] == 3:
            if Baraja.jerarquia[cartaMayor] >= 10 or Baraja.jerarquia[cartaMedia] >= 10:
                if randint(0, 10) <= 7:
                    return "Quiero"
                elif Baraja.jerarquia[cartaMayor] >= 12:
                    return "Vale 4"
                else:
                    if Baraja.jerarquia[cartaMayor] >= 8 and Baraja.jerarquia[cartaMayor] >= 8:
                        return "Quiero"
                    else:
                        return "No Quiero"
            elif randint(0, 10) % 2 == 0:
                return "Quiero"
            else:
                return "No Quiero"
        if paratruco[1][1] == "Vale 4" and paratruco[0] == 4:
            if Baraja.jerarquia[cartaMayor] >= 11 or Baraja.jerarquia[cartaMedia] >= 11:
                if randint(0, 10) % 2 == 0:
                    return "Quiero"
                else:
                    return "No Quiero"
            elif randint(0, 10) % 2 == 0:
                return "Quiero"
            else:
                return "No Quiero"


############################
############################
##     ESTO ES EL BOT     ##
############################
############################
def turnoBot(cartaanterior, gana, ganaronda, ronda, jugadores):
    cartaMayor = miMejorCarta(jugadores[1].mano)
    cartaMenor = miPeorCarta(jugadores[1].mano)
    cartaMedia = ""
    if ganaronda == 0 and gana == "":  # primera ronda
        for i in jugadores[1].mano:
            if Baraja.jerarquia[i] > Baraja.jerarquia[cartaMenor] and Baraja.jerarquia[i] < Baraja.jerarquia[cartaMayor]:
                return jugadores[1].mano.pop(jugadores[1].mano.index(i))
            elif Baraja.jerarquia[i] == Baraja.jerarquia[cartaMenor] and Baraja.jerarquia[i] == Baraja.jerarquia[cartaMayor]:
                return jugadores[1].mano.pop(jugadores[1].mano.index(i))
            elif Baraja.jerarquia[i] > Baraja.jerarquia[cartaMenor] and Baraja.jerarquia[i] <= Baraja.jerarquia[cartaMayor]:
                return jugadores[1].mano.pop(jugadores[1].mano.index(i))
        # si la carta no cumple con lo anterior jugar la mejor carta
        return jugadores[1].mano.remove(miMejorCarta(jugadores[1].mano))
# Despues de primera Ronda
    if ganaronda == 0 and gana == "E1" and ronda == 0:  # Entraria en la segunda ronda
        # Si mi peor carta es mayor
        if cartaanterior < Baraja.jerarquia[cartaMenor]:
            # Juego la menor
            return jugadores[1].mano.pop(jugadores[1].mano.index(cartaMenor))
        else:
            if len(jugadores[1].mano) == 3:  # si tengo 3 cartas en mano
                for i in jugadores[1].mano:
                    if i != cartaMayor and i != cartaMenor:
                        cartaMedia = i
                if cartaanterior < Baraja.jerarquia[cartaMedia]:
                    return jugadores[1].mano.pop(jugadores[1].mano.index(cartaMedia))
                elif cartaanterior < Baraja.jerarquia[cartaMayor]:
                    return jugadores[1].mano.pop(jugadores[1].mano.index(cartaMayor))
                else:
                    return jugadores[1].mano.pop(jugadores[1].mano.index(cartaMenor))

    if ganaronda == 0 and gana == "E1" and ronda == 1:
        # Si mi peor carta es mayor
        if cartaanterior < Baraja.jerarquia[cartaMenor]:
            # Juego la menor
            return jugadores[1].mano.pop(jugadores[1].mano.index(cartaMenor))
        else:
            if cartaanterior < Baraja.jerarquia[cartaMayor]:
                return jugadores[1].mano.pop(jugadores[1].mano.index(cartaMayor))
            else:
                return jugadores[1].mano.pop(jugadores[1].mano.index(cartaMenor))
    if ganaronda == 0 and gana == "E1" and ronda == 2:  # Pierde
        return jugadores[1].mano.pop()
    if ganaronda == 1 and ronda == 1:  # Si gano primera juega chico para ganar tercera
        return jugadores[1].mano.pop(jugadores[1].mano.index(cartaMenor))
    if ganaronda == 1 and ronda == 2:  # si gano 1 de las dos primeras ronda juega mejor carta q es ultima carta
        return jugadores[1].mano.pop(jugadores[1].mano.index(cartaMayor))

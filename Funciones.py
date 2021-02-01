from Player import *
from Baraja import *
from Bot import *
from random import randint


def envido(equipo1, equipo2, turno, paraenvido, bot):
    ptsEpo1 = paraenvido[0]
    ptsEpo2 = paraenvido[1]
    env = 0  # Si hay o no envido
    turnoaux = turno
    juegabot = False
    puntosBot = 0
    if bot:
        puntosBot = contarPuntos(equipo2, 0)
    else:
        puntosBot = 0
    puntosrechazo = 1
    puntosenv = 2
    real = 0
    canto1 = ["Envido", "Real Envido", "Falta Envido", "Jugar", "Al Mazo"]
    canto2 = ["Quiero", "Envido", "Real Envido", "Falta Envido", "No Quiero"]
    puntosE1 = 0
    puntosE2 = 0
    falta = False
    if turno % 2 == 0:  # muestro los puntos de los compañeros. hay que cambiar
        print("\n##################\nPuntos equipo 1")
        for l in range(0, len(equipo1)):
            print("# ", contarPuntos(equipo1, l), " \t#")
        print("##################\n")
    else:
        if bot == False:
            print("\n##################\nPuntos Equipo 2")
            for l in range(0, len(equipo2)):
                print("# ", contarPuntos(equipo2, l), " \t#")
            print("##################\n")

    if bot:  # Si se juega con bot
        if turno != 1:  # y si no es el turno del bot
            for i in range(0, len(canto1)):  # muestro las opciones a cantar
                print(i, ")", canto1[i])
    else:  # Si no juego con bot
        for i in range(0, len(canto1)):  # muestro las opciones a cantar
            print(i, ")", canto1[i])
    op = 0
    # SI ES EL TURNO DEL BOT ELIJE SI CANTA Y QUE CANTA LLAMANDO A UNA FUNCION
    if bot and turno == 1:  # si hay bot cuenta los puntos que tiene en mano
        if randint(0, 10) % 2 == 0:  # para que no siempre cante
            # cuento los puntos para verificar si canta algo
            puntosBot = contarPuntos(equipo2, 0)
            if puntosBot in [27, 28]:  # Canta envido si esta entre esos valores
                op = "0"
            elif puntosBot in [29, 30, 31]:  # canta realenvido si esta entre estos valores
                op = "1"
            # Si esta entre estos valores y obtiene mas de 7 puntos canta falta, sino solo envido
            elif puntosBot in [32, 33]:
                if paraenvido[0] < 15:
                    if (15-paraenvido[0]) <= 7:
                        op = "2"
                    else:
                        # para simular ser aleatoreo
                        if (paraenvido[1]+paraenvido[0]+puntosBot) % 2 != 0:
                            op = "1"
                        else:
                            op = "0"
                elif paraenvido[0] > 15:
                    if (30-paraenvido[0]) <= 7:
                        op = "2"
                    else:
                        # para simular ser aleatoreo
                        if (paraenvido[1]+paraenvido[0]+puntosBot) % 2 != 0:
                            op = "1"
                        else:
                            op = "0"
            elif puntosBot in [24, 25, 26]:  # para simular ser aleatoreo
                if randint(0, 10) <= 6:
                    op = "0"
                else:
                    op = "3"
            else:
                op = "3"
        else:
            op = "3"
    else:
        op = input()
        juegabot = True
    while True:
        if op in ["0", "1", "2", "3", "4"]:
            op = int(op)
            break
        else:
            print("Opción Invalida. Ingrese una opción Válida")
            op = input()
    if op in [0, 1, 2]:
        env = 1
    if op == 1:
        canto2.remove("Envido")
        canto2.remove("Real Envido")
        puntosenv = puntosenv+1
    elif op == 2:
        canto2.remove("Envido")
        canto2.remove("Real Envido")
        canto2.remove("Falta Envido")
        falta = True
    elif op == 3:
        return env
    elif op == 4:
        for i in range(len(equipo1)):
            if turnoaux+1 == equipo1[i].idjugador:
                paraenvido[1] = paraenvido[1]+2
            if turnoaux+1 == equipo2[i].idjugador:
                paraenvido[0] = paraenvido[0]+2
        env = 2
        return env
    print("\n¡¡", canto1.pop(op).upper(), "!!\n")
    if turno % 2 == 0:
        print("**Puntos equipo 2**\n")
        for l in range(0, len(equipo2)):
            print(contarPuntos(equipo2, l))
        print()
    else:
        print("**Puntos Equipo 1**\n")
        for l in range(0, len(equipo1)):
            print(contarPuntos(equipo1, l))
        print()
    while True:
        if bot:
            if juegabot == False:
                for i in range(0, len(canto2)):
                    print(i, ")", canto2[i])
        else:
            for i in range(0, len(canto2)):
                print(i, ")", canto2[i])
        if bot and juegabot:
            op = cantoBot(puntosBot, falta, canto2)
            juegabot = False
        else:
            op = input()
            juegabot = True
            while True:
                if op.isdigit():
                    op = int(op)
                    break
                else:
                    print("Opción Invalida. Ingrese una opcion Válida")
                    op = input()
        print(canto2[op].upper())
        if op == 0:
            for k in range(0, len(equipo1)):
                puntosauxE1 = contarPuntos(equipo1, k)
                puntosauxE2 = contarPuntos(equipo2, k)
                if puntosauxE1 > puntosE1:
                    puntosE1 = puntosauxE1
                if puntosauxE2 > puntosE2:
                    puntosE2 = puntosauxE2
            if puntosE1 > puntosE2:  # si los puntos del equipo 1 son mayores se sumn directamente
                if falta:
                    if paraenvido[1] < 15:
                        puntosenv = 15-paraenvido[1]
                    else:
                        puntosenv = 30-paraenvido[1]
                paraenvido[0] = paraenvido[0]+puntosenv
                print("\t\t Ganó el equipo1 con ", puntosE1,
                      " son ## ", puntosenv, " ## para equipo1")
            elif puntosE2 > puntosE1:
                if falta:
                    if paraenvido[0] < 15:
                        puntosenv = 15-paraenvido[0]
                    else:
                        puntosenv = 30-paraenvido[0]
                paraenvido[1] = paraenvido[1]+puntosenv
                print("\t\t Ganó el equipo2 con ", puntosE2,
                      " son ## ", puntosenv, " ## para equipo2")
            # si son iguales se suman al equipo que sea mano.
            elif puntosE1 == puntosE2 and turno % 2 == 0:
                if falta:
                    if paraenvido[1] < 15:
                        puntosenv = 15-paraenvido[1]
                    else:
                        puntosenv = 30-paraenvido[1]
                paraenvido[0] = paraenvido[0]+puntosenv
                print("Ganó el equipo1 son ", puntosenv, " para equipo1")
            elif puntosE1 == puntosE2 and turno % 2 != 0:
                if falta:
                    if paraenvido[0] < 15:
                        puntosenv = 15-paraenvido[0]
                    else:
                        puntosenv = 30-paraenvido[0]
                paraenvido[1] = paraenvido[1]+puntosenv
                print("Ganó el equipo2 son ", puntosenv, " para equipo2")
            turnoaux = turnoaux+1
            break
        elif canto2[op] == "Envido":  # Envido+Envido
            puntosrechazo = puntosrechazo+1
            puntosenv = puntosenv+2
            canto2.remove("Envido")
            turnoaux = turnoaux+1
            continue
        elif canto2[op] == "Real Envido" and op == 2:  # Envido+Real Envido
            puntosrechazo = puntosrechazo+1
            puntosenv = puntosenv+3
            canto2.remove("Envido")
            canto2.remove("Real Envido")
            turnoaux = turnoaux+1
            continue
        elif canto2[op] == "Real Envido" and op == 1:  # Envido+Envido+Real Envido
            puntosrechazo = puntosrechazo+1
            puntosenv = puntosenv+3
            canto2.remove("Real Envido")
            turnoaux = turnoaux+1
            continue
        elif canto2[op] == "Falta Envido" and op == 3:  # Envido+Falta Envido
            puntosrechazo = 1
            falta = True
            canto2.remove("Envido")
            canto2.remove("Real Envido")
            canto2.remove("Falta Envido")
            turnoaux = turnoaux+1
            continue
        elif canto2[op] == "Falta Envido" and op == 2:
            puntosrechazo = 1
            falta = True
            canto2.remove("Real Envido")
            canto2.remove("Falta Envido")
            turnoaux = turnoaux+1
            continue
        elif canto2[op] == "Falta Envido" and op == 1:  # Real envido+falta
            puntosrechazo = 1
            falta = True
            canto2.remove("Falta Envido")
            turnoaux = turnoaux+1
            continue
        elif canto2[op] == "Falta Envido" and op == 1 and real == 1:
            puntosrechazo = 1
            falta = True
            canto2.remove("Falta Envido")
            turnoaux = turnoaux+1
            continue
        elif canto2[op] == "Falta Envido" and op == 1 and puntosrechazo == 4:
            puntosrechazo = 1
            falta = True
            canto2.remove("Falta Envido")
            turnoaux = turnoaux+1
            continue
        elif canto2[op] == "No Quiero":
            if turnoaux % 2 == 0:
                paraenvido[0] = paraenvido[0]+puntosrechazo
                print("**", puntosrechazo, " para equipo1\n")
            else:
                paraenvido[1] = paraenvido[1]+puntosrechazo
                print("**", puntosrechazo, " para equipo2\n")
            break
        if turnoaux > (len(equipo1)*2)-1:
            turnoaux = 0
    return env


def contarPuntos(jugadores, njugador):
    hay2 = False
    puntos = 0
    pinta = ["ORO", "ESPADA", "BASTO", "COPA"]
    for i in range(0, 4):  # es hasta 4 por cada pinta
        puntosaux = 0
        hay2 = False
        hay3 = False
        existe = 0  # existe me dice cuantas cartas de esa pinta hay en la mano
        for j in range(0, 3):
            unacarta = jugadores[njugador].manoenv[j]

            if unacarta.find(pinta[i]) != -1:
                puntosaux = puntosaux + \
                    Baraja.valorCarta[jugadores[njugador].manoenv[j]]
                existe = existe+1
                if existe == 2 and puntosaux != 0:
                    hay2 = True
                if existe == 3:
                    hay2 = False
                    hay3 = True
                    carta1 = Baraja.valorCarta[jugadores[njugador].manoenv[0]]
                    carta2 = Baraja.valorCarta[jugadores[njugador].manoenv[1]]
                    carta3 = Baraja.valorCarta[jugadores[njugador].manoenv[2]]
                    if carta1+carta2+carta3 <= 13:  # cuenta los puntos entre las 3 cartas si son menos de 13 se devuelve este valor
                        puntos = carta1+carta2+carta3
                        if puntos == 0:
                            return puntos
                    else:  # si son mas de 13 se busca las 2 cartas de mayor valor y se devulven esos puntos
                        if carta1 > carta2 and carta2 > carta3 or carta2 > carta1 and carta1 > carta3:
                            puntos = carta1+carta2
                        elif carta1 > carta3 and carta3 > carta2 or carta3 > carta1 and carta1 > carta2:
                            puntos = carta1+carta3
                        elif carta2 > carta3 and carta3 > carta1 or carta3 > carta2 and carta2 > carta1:
                            puntos = carta2+carta3
        if puntosaux > puntos:
            puntos = puntosaux
        if puntos <= 13 and puntos > 0:
            if hay2 == True or hay3 == True:
                puntos = puntos + 20
    return puntos


def mayorCarta(equipo):
    mayor = "4 DE COPA"
    for i in range(0, len(equipo)):
        for j in range(0, 3):
            if Baraja.jerarquia[equipo[i].mano[j]] >= Baraja.jerarquia[mayor]:
                mayor = equipo[i].mano[j]
    print("La mejor carta del equipo es ", mayor)


def Truco(jugadores, equipo1, equipo2, turno, paratruco, bot):
    continua = 0
    turnoaux = turno
    elbot = jugadores[1]
    turno = turno+1
    if turno >= len(jugadores):
        turno = 0
    if paratruco[0] == 0:
        if bot and turnoaux == 1:
            opcionT = {"Truco": "a", "Al Mazo": "b", "Jugar": "c"}
            # paso el jugador y los datos de truco para que sepa que cantar
            op = opcionT[trucoBot(elbot, paratruco)]
        else:
            print(
                "---------------------------------------\na)Truco\t\tb)Al Mazo\tc)Jugar")
            op = input()
        while True:
            if op in ["a", "b", "c"]:
                break
            else:
                print("Ingrese una opción válida")
                op = input()
        if op == "a":
            for i in range(0, len(equipo1)):
                if turno+1 == equipo1[i].idjugador:
                    paratruco[1][0] = equipo2[i].equipo
                    paratruco[1][1] = "Truco"
                elif turno+1 == equipo2[i].idjugador:
                    paratruco[1][0] = equipo1[i].equipo
                    paratruco[1][1] = "Truco"
            paratruco[0] = 1
            print("#########\n# Truco #\n#########\n")
            sigturno = turnoaux+1
            if sigturno >= len(jugadores):
                sigturno = 0
            if bot == False:
                print(jugadores[turno].nombre, " Responde \nSu mano es:")
                jugadores[turno].verMano()
            elif bot == True and turno != 1:
                print(jugadores[turno].nombre, " Responde \nSu mano es:")
                jugadores[turno].verMano()
            continua = Truco(jugadores, equipo1, equipo2,
                             (sigturno), paratruco, bot)
            return continua
        if op == "b":
            paratruco[0] = 1
            continua = 2
            for i in range(0, len(equipo1)):
                if turno+1 == equipo1[i].idjugador:
                    paratruco[1][0] = equipo2[i].equipo
                    paratruco[1][1] = "Al Mazo"
                elif turno+1 == equipo2[i].idjugador:
                    paratruco[1][0] = equipo1[i].equipo
                    paratruco[1][1] = "Al Mazo"
            print("###########\n# Al Mazo #\n###########\n")
            return continua
        if op == "c":
            paratruco[0] = 0
            continua = 0
            return continua
    if paratruco[0] == 1:
        if paratruco[1][0] == equipo1[0].equipo:
            if bot and paratruco[1][1] == "Truco":
                opcionR = {"Quiero": "a", "Retruco": "b", "No Quiero": "c"}
                op = opcionR[trucoBot(elbot, paratruco)]
            else:
                print(
                    "-------------------------------------------\na)Quiero\tb)Retruco\tc)No Quiero")
                op = input()
            while True:
                if op in ["a", "b", "c"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 2
                continua = 1
                print("##########\n# Quiero #\n##########\n")
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Quiero"
                return continua
            if op == "b":
                paratruco[0] = 3
                print(
                    "#######################\n# Quiero Retruco #\n#######################\n")
                sigturno = turnoaux+1
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Retruco"
                if sigturno >= len(jugadores):
                    sigturno = 0
                if bot == False:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                elif bot == True and turno != 1:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                continua = Truco(jugadores, equipo1, equipo2,
                                 (sigturno), paratruco, bot)
                return continua
            if op == "c":
                paratruco[0] = 1
                continua = 2
                print("################\n# No se Quiere #\n################\n")
                paratruco[1][0] = "E2"
                paratruco[1][1] = "No Quiero"
                return continua
        elif paratruco[1][0] == equipo2[0].equipo:
            print(
                "-------------------------------------------\na)Quiero\tb)Retruco\tc)No Quiero")
            op = input()
            while True:
                if op in ["a", "b", "c"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 2
                continua = 1
                print("##########\n# Quiero #\n##########\n")
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Quiero"
                return continua
            if op == "b":
                paratruco[0] = 3
                print(
                    "#######################\n# Quiero Retruco #\n#######################\n")
                sigturno = turnoaux+1
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Retruco"
                if sigturno >= len(jugadores):
                    sigturno = 0
                if bot == False:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                elif bot == True and turno != 1:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                continua = Truco(jugadores, equipo1, equipo2,
                                 (sigturno), paratruco, bot)
                return continua
            if op == "c":
                paratruco[0] = 1
                continua = 2
                print("################\n# No se Quiere #\n################\n")
                paratruco[1][0] = "E1"
                paratruco[1][1] = "No Quiero"
                return continua
    if paratruco[0] == 2:
        if paratruco[1][0] == equipo1[0].equipo and paratruco[1][1] == "Quiero" and turno % 2 != 0:
            print(
                "---------------------------------------\na)Retruco\tb)Al Mazo\tc)Jugar")
            op = input()
            while True:
                if op in ["a", "b", "c"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 3
                print("###########\n# Retruco #\n###########\n")
                sigturno = turnoaux+1
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Retruco"
                if sigturno >= len(jugadores):
                    sigturno = 0
                if bot == False:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    # poner un condiconal para que no lo muestre con bot
                    jugadores[turno].verMano()
                elif bot == True and turno != 1:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                continua = Truco(jugadores, equipo1, equipo2,
                                 (sigturno), paratruco, bot)
                return continua
            if op == "b":
                paratruco[0] = 2
                continua = 2
                print("###########\n# Al Mazo #\n###########\n")
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Al Mazo"
                return continua
            if op == "c":
                paratruco[0] = 2
                continua = 1
                return continua
        # Agregar otra opcion similar xq bot no entra acá
        if paratruco[1][0] == equipo2[0].equipo and paratruco[1][1] == "Quiero" and turno % 2 == 0:
            if bot and paratruco[1][1] == "Quiero":
                opcionRe = {"Retruco": "a", "Al Mazo": "b", "Jugar": "c"}
                op = opcionRe[trucoBot(elbot, paratruco)]
            else:
                print(
                    "---------------------------------------\na)Retruco\tb)Al Mazo\tc)Jugar")
                op = input()
            while True:
                if op in ["a", "b", "c"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 3
                print("###########\n# Retruco #\n###########\n")
                sigturno = turnoaux+1
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Retruco"
                if sigturno >= len(jugadores):
                    sigturno = 0
                if bot == False:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    # poner un condiconal para que no lo muestre con bot
                    jugadores[turno].verMano()
                elif bot == True and turno != 1:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                continua = Truco(jugadores, equipo1, equipo2,
                                 (sigturno), paratruco, bot)
                return continua
            if op == "b":
                paratruco[0] = 2
                continua = 2
                print("###########\n# Al Mazo #\n###########\n")
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Al Mazo"
                return continua
            if op == "c":
                paratruco[0] = 2
                continua = 1
                return continua

    if paratruco[0] == 3 and paratruco[1][1] == "Retruco":
        if paratruco[1][0] == equipo1[0].equipo and turno % 2 == 0:
            if bot:
                opcionRe = {"Quiero": "a", "Vale 4": "b", "No Quiero": "c"}
                op = opcionRe[trucoBot(elbot, paratruco)]
            else:
                print(
                    "-------------------------------------------\na)Quiero\tb)Vale 4\tc)No Quiero")
                op = input()
            while True:
                if op in ["a", "b", "c"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 3
                continua = 1
                print("##########\n# Quiero #\n##########\n")
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Quiero"
                return continua
            if op == "b":
                paratruco[0] = 4
                print(
                    "######################\n# Quiero Vale Cuatro #\n######################\n")
                sigturno = turnoaux+1
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Vale 4"
                if sigturno >= len(jugadores):
                    sigturno = 0
                if bot == False:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                elif bot == True and turno != 1:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                continua = Truco(jugadores, equipo1, equipo2,
                                 (sigturno), paratruco, bot)
                return continua
            if op == "c":
                paratruco[0] = 2
                continua = 2
                paratruco[1][0] = "E2"
                paratruco[1][1] = "No Quiero"
                print("################\n# No se Quiere #\n################\n")
                return continua
        elif paratruco[1][0] == equipo1[0].equipo and turnoaux % 2 == 0:
            # Creo q tampoco entra a esta condición puede hacer que me muestre las opciones en un turno no correspondiente
            print(
                "-------------------------------------------\na)Quiero\tb)Vale 4\tc)No Quiero")
            op = input()
            while True:
                if op in ["a", "b", "c"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 3
                continua = 1
                print("##########\n# Quiero #\n##########\n")
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Quiero"
                return continua
            if op == "b":
                paratruco[0] = 4
                print(
                    "######################\n# Quiero Vale Cuatro #\n######################\n")
                sigturno = turnoaux+1
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Vale 4"
                if sigturno >= len(jugadores):
                    sigturno = 0
                if bot == False:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    # poner un condiconal para que no lo muestre con bot
                    jugadores[turno].verMano()
                elif bot == True and turno != 1:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                continua = Truco(jugadores, equipo1, equipo2,
                                 (sigturno), paratruco, bot)
                return continua
            if op == "c":
                paratruco[0] = 2
                paratruco[1][0] = "E2"
                paratruco[1][1] = "No Quiero"
                continua = 2
                print("################\n# No se Quiere #\n################\n")
                return continua
        if paratruco[1][0] == equipo2[0].equipo and turno % 2 != 0:
            print(
                "-------------------------------------------\na)Quiero\tb)Vale 4\tc)No Quiero")
            op = input()
            while True:
                if op in ["a", "b", "c"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 3
                continua = 1
                print("Quiero")
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Quiero"
                return continua
            if op == "b":
                paratruco[0] = 4
                # continua=1
                print(
                    "######################\n# Quiero Vale Cuatro #\n######################\n")
                sigturno = turnoaux+1
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Vale 4"
                if sigturno >= len(jugadores):
                    sigturno = 0
                if bot == False:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    # poner un condiconal para que no lo muestre con bot
                    jugadores[turno].verMano()
                elif bot == True and turno != 1:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                continua = Truco(jugadores, equipo1, equipo2,
                                 (sigturno), paratruco, bot)
                return continua
            if op == "c":
                paratruco[0] = 2
                paratruco[1][0] = "E1"
                paratruco[1][1] = "No Quiero"
                continua = 2
                print("################\n# No se Quiere #\n################\n")
                return continua
        # tambien creo q está demasy puede probocar mostrar opciones cuando no se debe
        elif paratruco[1][0] == equipo2[0].equipo and turnoaux % 2 != 0:
            if bot and paratruco[1][1] == "Retruco":
                opcionV = {"Quiero": "a", "Vale 4": "b", "No Quiero": "c"}
                op = opcionV[trucoBot(elbot, paratruco)]
            else:
                print(
                    "-------------------------------------------\na)Quiero\tb)Vale 4\tc)No Quiero")
                op = input()
            while True:
                if op in ["a", "b", "c"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 3
                continua = 1
                print("##########\n# Quiero #\n##########\n")
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Quiero"
                return continua
            if op == "b":
                paratruco[0] = 4
                print(
                    "######################\n# Quiero Vale Cuatro #\n######################\n")
                sigturno = turnoaux+1
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Vale 4"
                if sigturno >= len(jugadores):
                    sigturno = 0
                if bot == False:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    # poner un condiconal para que no lo muestre con bot
                    jugadores[turno].verMano()
                elif bot == True and turno != 1:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                continua = Truco(jugadores, equipo1, equipo2,
                                 (sigturno), paratruco, bot)
                return continua
            if op == "c":
                paratruco[0] = 2
                paratruco[1][0] = "E1"
                paratruco[1][1] = "No Quiero"
                continua = 2
                print("################\n# No se Quiere #\n################\n")
                return continua
    if paratruco[0] == 3 and paratruco[1][1] == "Quiero":
        # Este tendria q ser turno%2!=0
        if paratruco[1][0] == equipo1[0].equipo and turno % 2 != 0:

            print("---------------------------------------\na)Vale 4\tb)Al Mazo\tc)Jugar")
            op = input()
            while True:
                if op in ["a", "b", "c"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 4
                # continua=1
                print(
                    "################################\n# Vamos por el Vale Cuatro #\n################################\n")
                sigturno = turnoaux+1
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Vale 4"
                if sigturno >= len(jugadores):
                    sigturno = 0
                if bot == False:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    # poner un condiconal para que no lo muestre con bot
                    jugadores[turno].verMano()
                elif bot == True and turno != 1:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                continua = Truco(jugadores, equipo1, equipo2,
                                 (sigturno), paratruco, bot)
                return continua
            if op == "b":
                paratruco[0] = 3
                continua = 2
                print("###########\n# Al Mazo #\n###########\n")
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Al Mazo"
                return continua
            if op == "c":
                paratruco[0] = 3
                continua = 1
                return continua
        if paratruco[1][0] == equipo2[0].equipo and turno % 2 == 0:  # turno%2==0 debería de ser
            if bot:
                opcionVa = {"Vale 4": "a", "Al Mazo": "b", "Jugar": "c"}
                op = opcionVa[trucoBot(elbot, paratruco)]
            else:
                print(
                    "---------------------------------------\na)Vale 4\tb)Al Mazo\tc)Jugar")
                op = input()
            while True:
                if op in ["a", "b", "c"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 4

                print(
                    "################################\n# Vamos por el Vale Cuatro #\n################################\n")
                sigturno = turnoaux+1
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Vale 4"
                if sigturno >= len(jugadores):
                    sigturno = 0
                if bot == False:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    # poner un condiconal para que no lo muestre con bot
                    jugadores[turno].verMano()
                elif bot == True and turno != 1:
                    print(jugadores[turno].nombre, " Responde \nSu mano es:")
                    jugadores[turno].verMano()
                continua = Truco(jugadores, equipo1, equipo2,
                                 (sigturno), paratruco, bot)
                return continua
            if op == "b":
                paratruco[0] = 3
                continua = 2
                print("###########\n# Al Mazo #\n###########\n")
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Al Mazo"
                return continua
            if op == "c":
                paratruco[0] = 3
                continua = 1
                return continua
    if paratruco[0] == 4:
        if paratruco[1][0] == equipo1[0].equipo and paratruco[1][1] == "Vale 4" and turno % 2 == 0:
            if bot:
                querer = {"Quiero": "a", "No Quiero": "b"}
                op = querer[trucoBot(elbot, paratruco)]
            else:
                print("---------------------------\na)Quiero\tb)No Quiero")
                op = input()
            while True:
                if op in ["a", "b"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 4
                continua = 1
                print("##########\n# Quiero #\n##########\n")
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Quiero"
                return continua
            if op == "b":
                paratruco[0] = 3
                continua = 2
                print("################\n# No se Quiere #\n################\n")
                paratruco[1][0] = "E2"
                paratruco[1][1] = "No Quiero"
                return continua
        elif paratruco[1][0] == equipo1[0].equipo and paratruco[1][1] == "Vale 4" and turnoaux % 2 == 0:  # Creo q está demás
            print("---------------------------\na)Quiero\tb)No Quiero")
            op = input()
            while True:
                if op in ["a", "b"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 4
                continua = 1
                print("##########\n# Quiero #\n##########\n")
                paratruco[1][0] = "E2"
                paratruco[1][1] = "Quiero"
                return continua
            if op == "b":
                paratruco[0] = 3
                continua = 2
                print("################\n# No se Quiere #\n################\n")
                paratruco[1][0] = "E2"
                paratruco[1][1] = "No Quiero"
                return continua
        if paratruco[1][0] == equipo2[0].equipo and paratruco[1][1] == "Vale 4" and turno % 2 != 0:

            print("---------------------------\na)Quiero\tb)No Quiero")
            op = input()
            while True:
                if op in ["a", "b"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 4
                continua = 1
                print("##########\n# Quiero #\n##########\n")
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Quiero"
                return continua
            if op == "b":
                paratruco[0] = 3
                continua = 2
                print("No se Quiere")
                paratruco[1][0] = "E1"
                paratruco[1][1] = "No Quiero"
                return continua
                # Lo de abajo está repetido
        # Creo q tambien está demás
        elif paratruco[1][0] == equipo2[0].equipo and paratruco[1][1] == "Vale 4" and turnoaux % 2 != 0:
            if bot and turnoaux == 1:
                querer = {"Quiero": "a", "No Quiero": "b"}
                op = querer[trucoBot(elbot, paratruco)]
            else:
                print("---------------------------\na)Quiero\tb)No Quiero")
                op = input()
            while True:
                if op in ["a", "b"]:
                    break
                else:
                    print("Ingrese una opción válida")
                    op = input()
            if op == "a":
                paratruco[0] = 4
                continua = 1
                print("##########\n# Quiero #\n##########\n")
                paratruco[1][0] = "E1"
                paratruco[1][1] = "Quiero"
                return continua
            if op == "b":
                paratruco[0] = 3
                continua = 2
                print("################\n# No se Quiere #\n################\n")
                paratruco[1][0] = "E1"
                paratruco[1][1] = "No Quiero"
                return continua


def puntas(jugadores, puntospuntas, empieza, bot):
    dar = []
    participantes = len(jugadores)
    for punta in range(3):
        jugador1 = jugadores[punta]
        jugador2 = jugadores[punta+3]
        participan = [jugador1, jugador2]
        equipo1 = [jugador1]
        equipo2 = [jugador2]

        gana = ""  # gana vale 1 si es quipo1 2 si es equipo2 y cero para empate
        ganarondaJ1 = 0
        ganarondaJ2 = 0
        primeraronda = ""
        proxronda = 0  # Con esta variable me aseguro de que empiece el la ronda el jugador que gana la anterior
        env = 0
        puntostruco = 0
        canto = ["Nada", "Nada"]
        paratruco = [puntostruco, canto]
        salir = 0
        opcionescarta = ["a", "b", "c"]
        for ronda in range(3):
            if salir == 2:
                break
            if ronda == 0:
                turno = 0
            else:
                opcionescarta.pop()
                turno = proxronda  # con esta asignacion digo que empiece desde el que gano la ronda anterior
            turnosjugados = 0  # Controlar despues por las dudas
            cartaanterior = 0
            print("@@@@@@@@@@@@@\n@ Ronda ", ronda+1, " @\n@@@@@@@@@@@@@\n")

            while turnosjugados < 2:  # solo está para ver si se está jugando
                if salir == 2:
                    break
                print("\n#####*****#####\n\nTurno jugador ",
                      participan[turno].nombre, "\n Su Mano es:")
                paraenvido = [puntospuntas[0], puntospuntas[1]]
                if ronda == 0 and env == 0:
                    participan[turno].verMano()
                    env = envido(equipo1, equipo2, turno, paraenvido, bot)
                    puntospuntas[0] = paraenvido[0]
                    puntospuntas[1] = paraenvido[1]

                participan[turno].verMano()

                salir = Truco(participan, equipo1, equipo2,
                              turno, paratruco, bot)
                puntostruco = paratruco[0]
                canto[0] = paratruco[1][0]
                canto[1] = paratruco[1][0]

                if salir == 2:
                    ronda = 4
                    if canto[0] == "E1":
                        ganarondaE2 = 2
                        ganarondaE1 = 0
                    elif canto[0] == "E2":
                        ganarondaE1 = 2
                        ganarondaE2 = 0
                    break
                print("Introduce la opción a jugar")
                juego = input()
                while True:
                    if juego in opcionescarta:
                        break
                    else:
                        print("Opción Invalida. Ingrese opciones posibles")
                        juego = input()
                carta = participan[turno].jugar(juego)
                print("\n", participan[turno].nombre, "Juega ", carta, "\n")
                if cartaanterior == 0:  # si es la primera vez que entra
                    # carta anterior = a el valor de la Primera carta jugada
                    cartaanterior = Baraja.jerarquia[carta]
                    # El equipo que juega primero es quien empieza ganando
                    gana = participan[turno].equipo
                    proxronda = turno  # si el primer jugador es quien gana será el primero en jugar

                # si no es la primera pasada comparo valores
                elif Baraja.jerarquia[carta] > cartaanterior:
                    # Gana = a E1 o E2 dependiendo a que grupo pertenezca
                    gana = participan[turno].equipo
                    # la ultima carta ganadora pasa a ser la anterior para volver a comparar
                    cartaanterior = Baraja.jerarquia[carta]
                    proxronda = turno  # si gana será el proximo en empezar

                # Si son de igual valor se guarda EM para decir empate
                elif Baraja.jerarquia[carta] == cartaanterior:
                    gana = "EM"
                    proxronda = 0  # se iguala a sero para quien sea mano empice para el desempate
                turno = turno+1  # sumo para que juegue el siguiente jugador
                # se usa para llevar el conteo de los turnos jugados
                turnosjugados = turnosjugados+1

                if turno >= participantes:  # si la suma se excede de la cantidad de jugadores
                    turno = 0  # se reinicia para que todos puedan jugar
            if ronda == 0:
                if gana != "EM":
                    primeraronda = gana
                else:
                    if empieza % 2 == 0:
                        primeraronda = "E1"
                    else:
                        primeraronda = "E2"

            if gana == "E1":
                ganarondaJ1 = ganarondaJ1+1
            elif gana == "E2":
                ganarondaJ2 = ganarondaJ2+1
            if ganarondaJ2 == 2 or ganarondaJ1 == 2:
                break
            if ganarondaJ1 == 1 and ganarondaJ2 == 1 and ronda == 2:
                if primeraronda == "E1":
                    ganarondaJ1 = 2
                elif primeraronda == "E2":
                    ganarondaJ2 = 2

        if ganarondaJ1 > ganarondaJ2 and ganarondaJ1 >= 2:
            print("\t¡¡¡VICTORIA PARA ELQUIPO 1!!!")
            if puntostruco == 0:
                puntospuntas[0] = puntospuntas[0]+1
            elif puntostruco > 0:
                puntospuntas[0] = puntospuntas[0]+puntostruco

        elif ganarondaJ2 > ganarondaJ1 and ganarondaJ2 >= 2:
            print("\t¡¡¡VICTORIA PARA EQUIPO 2!!!")
            if puntostruco == 0:
                puntospuntas[1] = puntospuntas[1]+1
            elif puntostruco > 0:
                puntospuntas[1] = puntospuntas[1]+puntostruco

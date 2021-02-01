from Baraja import *
from Funciones import *
import random
from Player import *

#####/////_____INICIO_____\\\\\#####
print("\t\tBIENVENIDO AL JUEGO DEL TRUCO\n\n\n")
while True:
    bot = False
    print("\n\t\tOpciones:\n\t1-JUGAR\n\t2-Desarrollado por\n\t3-Acerca de\n\t4-Salir")
    opcion = input()
    while True:
        if opcion in ["1", "2", "3", "4"]:
            break
        else:
            print("Opción Inválida, introduzca una opción válida")
            opcion = input()
    if opcion == "2":
        print("\nEnzo Ariel Martín (Programador)\nMarcos Alberto Duperú (Testing)")
    elif opcion == "3":
        print("Proyecto desarrollado por alumnos de la Universidad Tecnológica Nacional UTN\n"
              "Desarrollo de soluciones Back end y Testing")
    elif opcion == "4":
        break
    elif opcion == "1":
        nuevoMazo = Baraja()  # NUEVO MAZO ES DE TIPO BARAJA Y CONTIENE UNA LISTA DE 40 ELEMENTOS
        # nuevoMazo.mostrar()#FUNCION DE VERIFICACION DE ESTADO DE MAZO

        # SELECCION DE CANTIDAD DE JUGADORES

        participantes = 2
        # bot=False
        print("Ingrese cantidad de jugadores \n 2\n 4\n 6")
        while True:  # cargo el tipo de partida segun cantidad de jugadores
            participantes = input()
            if participantes in ["2", "4", "6"]:  # verifico que sea opcion válida
                participantes = int(participantes)
                if participantes == 2:
                    print("Desea jugar con un bot\na-Si    b-No")
                    while True:
                        inpt = input()
                        if inpt in ["a", "b"]:
                            if inpt == "a":
                                bot = True
                                print("\n El Bot será el jugador 2")
                            break
                        else:
                            print("Opción incorrecta. Ingrese una opción válida")
                break
            else:
                print("Cantidad de participantes incorecta elija una opción válida")

        # SE CREAN LOS JUGADORES
        jugadores = []
        equipo1 = []  # guardar los jugadores por grupo
        equipo2 = []
        print("\n\nLos jugadores se reparten uno para cada equipo, así el jugador 1 es del equipo 1 y el 2 del segundo equipo"
              "\nLas partidas de 4 y 6 jugadores son a 30 puntos mientras que las de 2 jugadores pueden ser a 15 o 30 puntos")
        for i in range(participantes):
            print("Ingrese el nombre del jugador ", (i+1))
            nombre = input()

            if i % 2 == 0:
                juegan = Player(nombre, (i+1), "E1")
                equipo1.append(juegan)
            elif bot != True:
                juegan = Player(nombre, (i+1), "E2")
                equipo2.append(juegan)
            elif bot:
                juegan = Bot(nombre, (i+1), "E2")
                equipo2.append(juegan)
            jugadores.append(juegan)

        finjuego = 0
        if participantes in [4, 6]:
            finjuego = 30
        else:
            print("La partida es hasta 1-15 2-30")
            while True:  # Se carga hasta cuantos puntos se puede jugar.
                op = input()
                if op in ["1", "2"]:
                    if op == "1":
                        finjuego = 15
                    else:
                        finjuego = 30
                    break
                else:
                    print("Opcion no valida elija entre opcion 1 o 2")
#################################################################################
#################################################################################
##                                                                             ##
##                              COMIENZA LA PARTIDA                            ##
##                                                                             ##
#################################################################################
#################################################################################

        dar = []
        ptsEpo1 = 0
        ptsEpo2 = 0
        empieza = 0
        ##########################################
        while ptsEpo1 < finjuego or ptsEpo2 < finjuego:  # ESTE WHILE CONTROLA EL FIN DEL JUEGO###
            ##########################################
            # ELIJO CARTAS A REPARTIR
            nuevoMazo.mezclar()
            for i in range(participantes):
                if len(jugadores[i].mano) > 0:
                    for j in range(len(jugadores[i].mano)):
                        jugadores[i].mano.pop(0)
                if len(jugadores[i].manoenv) > 0:
                    for j in range(len(jugadores[i].manoenv)):
                        jugadores[i].manoenv.pop(0)
            # eligen cartas a repartir a jugadores
            dar = nuevoMazo.repartir(int(participantes))
            while True:  # se reparten las cartas
                if dar:
                    for i in range(participantes):
                        jugadores[i].tomar(dar.pop(0))
                else:
                    break

            gana = ""  # gana vale 1 si es quipo1 2 si es equipo2 y cero para empate
            ganarondaE1 = 0
            ganarondaE2 = 0
            primeraronda = ""
            proxronda = 0  # Con esta variable me aseguro de que empiece el la ronda el jugador que gana la anterior
            env = 0
            puntostruco = 0
            canto = ["Nada", "Nada"]
            paratruco = [puntostruco, canto]
            salir = 0
            puntospuntas = [ptsEpo1, ptsEpo2]
            if (ptsEpo1+ptsEpo2) % 5 == 0 and participantes == 6 and (ptsEpo1+ptsEpo2) >= 5:
                print("\n%%%%%%%%%%%%%%%%%%%%\n%%\tPUNTAS\t  %%\n%%%%%%%%%%%%%%%%%%%%")
                puntas(jugadores, puntospuntas, empieza, bot)
                ptsEpo1 = puntospuntas[0]
                ptsEpo2 = puntospuntas[1]
                continue
            opcionescarta = ["a", "b", "c"]
            for ronda in range(3):
                if salir == 2:
                    break
                if ronda == 0:
                    turno = empieza
                else:
                    opcionescarta.pop()
                    turno = proxronda  # con esta asignacion digo que empiece desde el que gano la ronda anterior
                turnosjugados = 0  # Controlar despues por las dudas
                cartaanterior = 0
                print("@@@@@@@@@@@@@\n@ Ronda ",
                      ronda+1, " @\n@@@@@@@@@@@@@\n")

                while turnosjugados < participantes:  # solo está para ver si se está jugando
                    if salir == 2:
                        break
                    if bot and turno == 1:
                        print("\n%%%%%%%%%°°°°°°°°°%%%%%%%%%\nTurno Bot ",
                              jugadores[turno].nombre)
                    else:
                        print("\n%%%%%%%%%°°°°°°°°°%%%%%%%%%\nTurno jugador ",
                              jugadores[turno].nombre, "\n Su Mano es:")

                    paraenvido = [ptsEpo1, ptsEpo2]
                    if ronda == 0 and env == 0 and len(jugadores) == 2 and turnosjugados <= 1 and paratruco[0] == 0:
                        if bot and turno == 0:
                            jugadores[turno].verMano()
                        elif bot != True:
                            jugadores[turno].verMano()
                        env = envido(equipo1, equipo2, turno, paraenvido, bot)
                        ptsEpo1 = paraenvido[0]
                        ptsEpo2 = paraenvido[1]
                    elif ronda == 0 and env == 0 and len(jugadores) == 4 and turnosjugados >= 2 and paratruco[0] == 0:
                        jugadores[turno].verMano()
                        env = envido(equipo1, equipo2, turno, paraenvido, bot)
                        ptsEpo1 = paraenvido[0]
                        ptsEpo2 = paraenvido[1]
                    elif ronda == 0 and env == 0 and len(jugadores) == 6 and turnosjugados >= 4 and paratruco[0] == 0:
                        jugadores[turno].verMano()
                        env = envido(equipo1, equipo2, turno, paraenvido, bot)
                        ptsEpo1 = paraenvido[0]
                        ptsEpo2 = paraenvido[1]
                    if env == 2:
                        salir = 2
                        ronda = 4
                        break
                    if bot:  # Para que no muestre la mano del bot
                        if turno != 1:
                            jugadores[turno].verMano()
                    else:
                        jugadores[turno].verMano()

                    salir = Truco(jugadores, equipo1, equipo2,
                                  turno, paratruco, bot)
                    # Agrego este if por los puntos de retruco
                    if paratruco[1][1] == "Retruco":
                        puntostruco = 2
                    else:
                        puntostruco = paratruco[0]
                    canto[0] = paratruco[1][0]
                    canto[1] = paratruco[1][1]

                    if salir == 2:
                        ronda = 4
                        if canto[0] == "E1":
                            ganarondaE2 = 2
                            ganarondaE1 = 0
                            if env == 0 and canto[1] == "Al Mazo" and len(jugadores[len(jugadores)-1].mano) == 3:
                                ptsEpo2 = ptsEpo2+1
                        elif canto[0] == "E2":
                            ganarondaE1 = 2
                            ganarondaE2 = 0
                            if env == 0 and canto[1] == "Al Mazo" and len(jugadores[len(jugadores)-1].mano) == 3:
                                ptsEpo1 = ptsEpo1+1
                        break
                    if bot:
                        if turno == 1:
                            carta = turnoBot(
                                cartaanterior, gana, ganarondaE2, ronda, jugadores)
                            print(
                                "\n", jugadores[turno].nombre, "Juega ", carta, "\n")
                        else:
                            print("Introduce la opción a jugar")
                            juego = input()
                            while True:
                                if juego in opcionescarta:
                                    break
                                else:
                                    print(
                                        "Opción Invalida. Ingrese opciones posibles")
                                    juego = input()
                            carta = jugadores[turno].jugar(juego)
                            print(
                                "\n", jugadores[turno].nombre, "Juega ", carta, "\n")
                    else:
                        print("Introduce la opción a jugar")
                        juego = input()
                        while True:
                            if juego in opcionescarta:
                                break
                            else:
                                print("Opción Invalida. Ingrese opciones posibles")
                                juego = input()
                        carta = jugadores[turno].jugar(juego)
                        print("\n", jugadores[turno].nombre,
                              "Juega ", carta, "\n")

                    if cartaanterior == 0:  # si es la primera vez que entra
                        # carta anterior = a el valor de la Primera carta jugada
                        cartaanterior = Baraja.jerarquia[carta]
                        # El equipo que juega primero es quien empieza ganando
                        gana = jugadores[turno].equipo
                        proxronda = turno  # si el primer jugador es quien gana será el primero en jugar

                    # si no es la primera pasada comparo valores
                    elif Baraja.jerarquia[carta] > cartaanterior:
                        # Gana = a E1 o E2 dependiendo a que grupo pertenezca
                        gana = jugadores[turno].equipo
                        # la ultima carta ganadora pasa a ser la anterior para volver a comparar
                        cartaanterior = Baraja.jerarquia[carta]
                        proxronda = turno  # si gana será el proximo en empezar

                    # Si son de igual valor se guarda EM para decir empate
                    elif Baraja.jerarquia[carta] == cartaanterior:
                        gana = "EM"
                        proxronda = 0  # se iguala a cero para quien sea mano empice para el desempate
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

                # Revisar cuando son pardas
                if gana == "E1":
                    ganarondaE1 = ganarondaE1+1
                elif gana == "E2":
                    ganarondaE2 = ganarondaE2+1
                if ganarondaE2 == 2 or ganarondaE1 == 2:
                    break
                if ganarondaE1 == 1 and ganarondaE2 == 1 and ronda == 2:
                    if primeraronda == "E1":
                        ganarondaE1 = 2
                    elif primeraronda == "E2":
                        ganarondaE2 = 2

            if ganarondaE1 > ganarondaE2 and ganarondaE1 >= 2:
                print("\t¡¡¡GANA EQUIPO 1!!!")
                if puntostruco == 0:
                    ptsEpo1 = ptsEpo1+1
                elif puntostruco > 0:
                    ptsEpo1 = ptsEpo1+puntostruco

            elif ganarondaE2 > ganarondaE1 and ganarondaE2 >= 2:
                print("\t¡¡¡GANA EQUIPO 2!!!")
                if puntostruco == 0:
                    ptsEpo2 = ptsEpo2+1
                elif puntostruco > 0:
                    ptsEpo2 = ptsEpo2+puntostruco

            if ptsEpo1 >= finjuego or ptsEpo2 >= finjuego:
                break  # solo está para que salga el programa
            empieza = empieza+1
            if empieza >= participantes:
                empieza = 0
            print("\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\nPuntos:\nEquipo1: ",
                  ptsEpo1, "\tEquipo2: ", ptsEpo2, "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")

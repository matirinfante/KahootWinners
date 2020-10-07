#@matirinfante on Github
#Taller práctica II - Informática -- Pablo VI
#Oct. 2020

"""
Cálculo de Kahoot Winners

El cálculo de los kahoot winners se basa en la cantidad de participantes que hubo en la sesión y el porcentaje de acierto promedio una vez finalizado el quiz. Este último solo será tomado en cuenta si es mayor igual al 60%.

En el algoritmo están incluidos conceptos de variables, entrada de datos, estructura condicional simple y aritmética sencilla.
"""

def calcKahootWinners():
    kahootWinnersBase = int(input('Cuantos participaron?\n')) // 3
    porcentaje = int(input('Porcentaje?\n')) // 10

    if porcentaje > 5:
        kahootWinnersFinal = kahootWinnersBase + porcentaje - 5

    print('Hay %a kahoot winners hoy' % (kahootWinnersFinal))

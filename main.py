"""
Cálculo de Kahoot Winners
@matirinfante on Github

El cálculo de los kahoot winners se basa en la cantidad de participantes que hubo en la sesión y el porcentaje de acierto promedio una vez finalizado el quiz. Este último solo será tomado en cuenta si es mayor igual al 60%.
"""


def calcKahootWinners():
    kahootWinnersBase = int(input('Cuantos participaron?\n')) // 3
    porcentaje = int(input('Porcentaje?\n')) // 10

    if porcentaje > 5:
        kahootWinnersFinal = kahootWinnersBase + porcentaje - 5

    print('Hay %a kahoot winners hoy' % (kahootWinnersFinal))

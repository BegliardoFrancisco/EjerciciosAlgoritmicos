from typing import List
from Data import generateData, getData
import funcionality


def PrinterOptionsMenu() -> None:
    print('Selected Options')
    print('1 Pasajeros por lineas  ')
    print('2 Promedio de pasajeros por parada')
    print('3 Parada con menorpsajeros de una linea ')
    print('4 Recaudacion Total de la empresa ')
    print('5 Salir ')
    return None

def menu() -> None:
    lineas, paradas = getData()     
    table: List[List[int]] = generateData(lineas,paradas, 25)
    print(table)
    PrinterOptionsMenu()
    op:int = 0
    while op in range(0,5):
        print('')
        op = int(input('Insert to options: '))
        if str(op) == '0':
            print('')
            print('Invalid Selected Option')
            print('')
            print('Exit')
            break
        if str(op) == '1':
            rta = funcionality.PassengersForLines(table, lineas)
            print('')
            print(f'Pasajeros por lineas {rta} ')
        if str(op) == '2':
            rta = funcionality.averageStopsPassengers(paradas, table)
            print('')
            print(f'Promedio de pasajeros por parada {rta}')
        if str(op) == '3':
            rta = funcionality.lowerPassengersLine(table, lineas)
            print('')
            print(f'Cantidad menor de pasajeros en una linea {rta}')
        if str(op) == '4':
            price = 8.5
            rta=funcionality.grossPrice(table, price)
            print('')
            print(f'Recaudacion Total de la empresa ${rta}')
        if str(op) == '5':
            print('')
            print('Exit')
            break
    else: 
        print('')
        print('Invalid Selected Option')
        print('')
        print('Exit')

    return None    
    


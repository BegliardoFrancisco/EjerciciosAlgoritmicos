from typing import Tuple, List,Dict
import random

def getData() -> Tuple[int]:
    print('')
    print('Ingrese los datos: ')
    print('')
    try:
        printLine:str = 'Ingrese en numero de lineas de colectivos: '
        lineas:int = int(input(printLine,))
        print('')
        printStops:str='Ingrese en numero de paradas de colectivos: '
        paradas:int= int(input(printStops,))
    except ValueError:
        print('ValueError: input is not required type ')
        lineas, paradas = getData() 
    finally:
        return lineas,paradas

def generateData(lineas:int, paradas:int, maxPassengers:int) -> dict:
    table: dict[List[int]] = {}  
    values = []
    for key in range(1,lineas+1):
        for __ in range(0,paradas):
            values.append(random.randint(0,maxPassengers))
        table[f'{key}'] = values
        values= []
    return table
def PassengersForLines( table: dict, lineas:int)  -> dict:
    Passengers:dict = {}
    suma = 0
    for lineas, paradas in table.items():
        suma = 0
        for pasajeros in paradas:
            suma += pasajeros
        Passengers[f'{lineas}'] = suma 
    return Passengers
        
def averageStopsPassengers(paradas: int, table: dict) -> float:

    StopsNumbers: int = int(input('Ingrese el numero de parada: ',))
    averageStopPassengers: int = 0 
    while StopsNumbers not in range(1,paradas):
        print("Invalid Stop")
        StopsNumbers: int = int(input('Ingrese el numero de parada: ',))
    else:
        for __ , parada in table.items():
            averageStopPassengers += parada[StopsNumbers]

    averageStopPassengers /= len(table.keys())
    return averageStopPassengers

def lowerPassengersLine(table:dict , linea:int)  -> int:

    MinPassengersLine: int = 0
    selectedLine :int = int(input('Ingrese el numero de linea: ',))
    while  selectedLine not in range(1,linea +1):
        print("Invalid Line")
        selectedLine :int = int(input('Ingrese el numero de linea: ',))
    else:
        menor = -1
        n = len (table[f'{selectedLine}'])
        paradas = table[f'{selectedLine}']
        for numero in range(0, n-1):
            if menor == -1:
                menor = 0
            elif paradas[numero] <= paradas[menor]:
                menor = numero
            else:
                menor = menor

        MinPassengersLine = paradas[menor]
    return MinPassengersLine


def grossPrice(table: int , price: float)  -> float:
    grossprice :int= 0
    for stops, lines in table.items():
        grossprice += sum(lines) 
    return grossprice * price
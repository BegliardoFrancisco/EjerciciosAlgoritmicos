# 2019_AED_TP4
# Begliardo_83573[1k7]_Bracamonte_81713[1k7]_Herrera_82805[1k7]

from registro import *
import random
import datetime
from datetime import date, timedelta
from archivos import *

##############################################
#Generación de publicaciones del sitio en el vector v

def provincias1():  # Función que contiene un listado de provincias para llamar y utilizar
    provincias = ["Córdoba", "Buenos Aires", "Entre Ríos", "Santa Fé", "Corrientes", "Misiones", "Tierra del Fuego",
                  "Santiago del Estero", "San Luís", "Neuquén", "Mendoza", "San Juan", "La Rioja", "Catamarca",
                  "Tucumán", "Salta", "Jujuy", "Chaco", "Formosa", "Río Negro", "Chubut", "Santa Cruz", "La Pampa"]
    return provincias  # Retorna una lista de provincias


def generardatos(n, v):  # Función que carga el vector de artículos por medio del registro.
    for i in range(n):
        iden = random.randint(100, 6000)
        precio = random.randint(10, 99)
        ubc = (random.randint(0, 22))
        est = random_estado()
        cant = random.randint(10, 100)
        point = random.randint(0, 4)
        v[i] = Registro(iden, precio, ubc, est, cant, point)


def random_estado():  # Función que asigna a los artículos el string de "Usado" con el valor 0 y "Nuevo" con el valor 1.
    e = random.randint(0, 1)
    if e == 0:
        estado = "Usado"
    else:
        estado = "Nuevo"
    return estado  # Retorna el string


def n_vector_mensaje():  # Función que muestra un mensaje de validación
    msj = "\nPara comenzar, ingrese el número de articulos disponibles en la plataforma: ➮ "
    return msj


def n_vector(msj, msj2):  # Función que crea el vector principal que almacenará toda la información.
    n = vldez_es_num(msj, msj2)
    v = [None] * n
    return n, v


def vector_sin_productos(v):  # Función que muestra un mensaje en caso de que no existiesen artículos en el sitio.
    romper = False
    if v == []:
        romper = True
    return romper  # Retorna la bandera

######################################################################
#MOSTRAR TODOS LOS ARTÌCULOS DISPONIBLES EN EL SITIO (opcion 1)

def mostrar_todos_articulos(v,n,provincias):
    for i in range(n):
        write(v,i,provincias)

##############################################################
#Punto 1
def ordenar_por_codigo(v, n):  # Función que ordena el vector principal por su código de menor a mayor.
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].iden > v[j].iden:
                v[i], v[j] = v[j], v[i]


def mensaje_error():  # Función que muestra un mensaje de validación.
    msj2 = "\n✘ Error, Solo se permiten caracteres numéricos. Intente de nuevo."
    return msj2


def busqueda_mensaje():  # Función que muestra un mensaje de validación.
    msj = "\nIngrese el codigo del articulo que desea buscar: ➮ "
    return msj


def busqueda(n, v, msj, msj2):  # Función que busca un código insertado por teclado.
    ordenar_por_codigo(v, n)
    codigo = vldez_es_num(msj, msj2)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if codigo == v[c].iden:
            return c  # Returna el índice del código encoentrado.
        if codigo < v[c].iden:
            der = c - 1
        else:
            izq = c + 1
    return -1  # Retorna una señal que indica que no se logró encontrar el valor solicitado.


def cantidadcompra_mensaje(): #Mensaje para mostrar en pantalla.
    msj = "\nIngrese la cantidad que desea comprar: ➮ "
    return msj


def cantidadcompra(rb, v, n, msj, msj2):  # Función que se encarga de procesar las compras.
    cant_sol = vldez_es_num(msj, msj2) #Se llama a una función que valida que el input sea un número.
    envio = 0
    if v[rb].cant >= cant_sol:
        envio = tipo_envio() #Se llama a una función que pregunta por el tipo de envio.
        x = confirmacioncompra() #Se llama a una función que pregunta por la confirmación final de compra.
        if x == 2:
            return 0, v, n,envio,cant_sol  # Retorna la cancelación de la compra
        v[rb].cant -= cant_sol #Se resta la cantidad de artículos comprados al stock de artículos en venta.
        if v[rb].cant == 0: #Si la cantidad total de artículos es igual a 0, se elimina este del vector v.
            del v[rb]
            n = len(v) #Se actualiza el len del vector v de artículos.
        return 1, v, n,envio,cant_sol  # Retorna la concretación de la compra
    else:
        return -1, v, n , envio, cant_sol   # Retorna que la cantidad deseada de artículos es más grande que el stock disponible.
    # El primer retorno indica el mensaje que debe mostrarse, el segundo el vector actualizado, el tercero el len del vector,
    #y el cuarto la cantidad de artículos a comprar.


def confirmacioncompra():  # Función que se encarga del proceso de confirmación y cancelación de la compra.
    x = -1
    opciones = ["1", "2"]
    print("\n１- SI, ACEPTAR LA COMPRA.")
    print("２- NO, RECHAZAR LA COMPRA.")
    while x not in opciones:
        x = input("\n¿Desea confirmar su comprar? Ingrese una opción: ➮ ")
        if x not in opciones:
            print("\n✘ Error, esa opción no se encuentra disponible. Intente de nuevo.")
    x = int(x)
    return x  # Retorna la opción ingresada.


def tipo_envio(): #Función que pregunta por el tipo de envio y que valida la opción ingresada.
    y = -1
    opciones = ["1", "2"]
    print("¿Cómo desea retirar el producto?")
    print("\n１- ENVIO A DOMICILIO .")
    print("２- RETIRO A SUCURSAL")
    while y not in opciones:
        y = input("\n Ingrese una opción disponible: ➮ ")
        if y not in opciones:
            print("\n✘ Error, esa opción no se encuentra disponible. Intente de nuevo.")
    y = int(y)
    return y #Retorna la opción.


def montos(n, envio, cant_sol, rb_copia_dato_precio): #Función que realiza el cálculo del interés de envio(o cargo), precio y precio total.
    interes = 0
    precio = rb_copia_dato_precio * cant_sol
    total = precio
    if envio == 1:
        interes = (precio * 10) /100
        total = round(interes,2) + precio
        return total, precio, round(interes,2) #Retorna el precio total (+ interés), el precio y el interés.
    else:
        return total, precio, interes #Retorna el precio total (+ interés), el precio y el interés.


def tiempo(): #Función que obtiene la fecha exacta actual. NOTA: solo se acepta el formato DD/MM/AAAA. Se si desea probar
    #el funcionamiento de esta función, deberá ajustarse al formato mencionado anteriormente.
    ayer = date.today() - timedelta()
    anos = str(ayer.year)
    meses = ayer.month
    meses = cerosantes_tiempo(meses)
    dias = ayer.day
    dias = cerosantes_tiempo(dias)
    fecha = "{}/{}/{}".format(dias,meses,anos)

    return fecha #Retorna la fecha en forma de string en el siguiente formato: DD/MM/AAAA


def cerosantes_tiempo(fecha):
    if fecha < 10:
        fecha = "0"+str(fecha)
        print(fecha)

    return fecha


def envio_numero_a_texto(envio): #Función que convierte en tipo de envio en formato numérico en un string con el tipo de envio.
    if envio == 1:
        envio = "Envío a domicilio"
    else:
        envio = "Retiro en sucursal"

    return envio #Retorna el tipo de envio.


def vcompras(rb_copia_dato_codigo, cant_sol, total, envio, precio, fecha, vcompra): #Carga un vector vcompra de un solo elemento.
    iden = rb_copia_dato_codigo
    cant_comp = cant_sol
    precio = precio
    envio = envio
    monto_total = total
    fecha = fecha

    vcompra[0] = Compra(iden,cant_comp,precio,envio,monto_total,fecha)


def archivosbinarios(): #Función que contiene los nombre de archivos binarios.
    mis_compra = "miscompras.dat"
    favoritos = "favoritos.dat"

    return mis_compra, favoritos #Retorna los nombres.

def archivostxt(contadorticket, rb_copia_dato_codigo): #Función que crea el nombre de archivo txt del ticket.
    ticket = "ticket_"+"codigo-"+str(rb_copia_dato_codigo)+"_"+str(contadorticket)+".txt"

    return ticket #Retorna el nombre del ticket.


def mensaje_ticket_exitoso(): #Función que muestra un mensaje correspondiente al ticket.
    print("\n————————————————————————————————————————————————")
    print("▤ ¡Su ticket se ha emitido con éxito!")
    print("————————————————————————————————————————————————")
##############################################################
#PUNTO 2

def ingresar_periodo_fechas(): #Función que pregunta por el origen y el final del rango de fechas.
    dia1 = dia2 = mes1 = mes2 = anio1 = anio2 = primerperiodo = segundoperiodo =  0
    op = -1

    #Se pregunta por el mes y el año de inicio del rango de la fecha a consultar.
    while op == -1:

        print("\n📅 PRIMER INTERVALO DE TIEMPO 📅")
        msj1_2 = ("\nDESDE: Ingrese un número de año de 4 cifras (Ejemplo: 2014): ➮ ")
        msj2 = mensaje_error()
        while op == -1:
            anio1 = vldez_es_num(msj1_2, msj2)
            op = validez_anio(anio1)

        op = -1

        print("\n📅 PRIMER INTERVALO DE TIEMPO 📅")
        msj1_1 = ("\nDESDE: Ingrese un número de mes (del 1 al 12): ➮ ")
        msj2 = mensaje_error()

        while op == -1:
            mes1 = vldez_es_num(msj1_1, msj2)
            op = validez_mes(mes1)

        op = -1

        print("\n📅 PRIMER INTERVALO DE TIEMPO 📅")
        msj1_1 = ("\nDESDE: Ingrese un número de día (del 1 al 31): ➮ ")
        msj2 = mensaje_error()

        while op == -1:
            dia1 = vldez_es_num(msj1_1, msj2)
            op = validez_dia(dia1, mes1, anio1)

        print("\n﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
        print("Su primera fecha de comparación es: {}/{}/{}".format(dia1,mes1,anio1))
        print("﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")

    #Se pregunta por el mes y el año final del rango de la fecha a consultar.
        op = -1

        print("\n📅 SEGUNDO INTERVALO DE TIEMPO 📅")
        msj1_2 = ("\nHASTA: Ingrese un número de año de 4 cifras (Ejemplo: 2020): ➮ ")
        msj2 = mensaje_error()

        while op == -1:
            anio2 = vldez_es_num(msj1_2, msj2)
            op = validez_anio(anio2)

        op = -1

        print("\n📅 SEGUNDO INTERVALO DE TIEMPO 📅")
        msj1_1 = ("\nHASTA: Ingrese un número de mes (del 1 al 12): ➮ ")
        msj2 = mensaje_error()

        while op == -1:
            mes2 = vldez_es_num(msj1_1, msj2)
            op = validez_mes(mes2)

        op = -1

        print("\n📅 SEGUNDO INTERVALO DE TIEMPO 📅")
        msj1_1 = ("\nDESDE: Ingrese un número de día (del 1 al 31): ➮ ")
        msj2 = mensaje_error()

        while op == -1:
            dia2 = vldez_es_num(msj1_1, msj2)
            op = validez_dia(dia2, mes2, anio2)

        print("\n﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
        print("Su segunda fecha de comparación es: {}/{}/{}".format(dia2,mes2,anio2))
        print("﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")

        op, primerperiodo, segundoperiodo = validez_repeticion(dia1, dia2, mes1, mes2, anio1, anio2) #Se llama a una función que valida
    #que la segunda fecha del rango sea menor a la primera.



    return primerperiodo, segundoperiodo #Retorna la primer y segunda fecha del rango respectivamente.


def validez_dia(dia, mes, anios): #Función que valida que el rango de dias se encuentre en un rango acorde a su mes y año.
    #También valida que ciertos meses se encuentren dentro del rango de 31, otros meses a sus correspondientes 30 días y,
    #en caso de los años bisiestos y no bisiestos, considera los días de Febrero.
    dias_31 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30","31"]
    dias_30 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
    mes_31 = ["1","3","5","7","8","10","12"]
    mes_30 = ["4","6","9","11"]
    febrero_nobisiesto = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
    febrero_bisiesto = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29"]
    mes_nobisiesto = ["1","2","3"]
    dia = str(dia)
    mes = str(mes)
    if mes in mes_31:
        if dia not in dias_31:
            op = -1
            print("\n✘ Error, ese día del mes no existe. Intente de nuevo.")
            return op #Retorna un aviso que indica que el día ingresado no se encuentra dentro del rango 1-31.
        else:
            op = 0
            return op #Retorna un aviso que indica que el día ingresado si se encuentra dentro del rango 1-31.
    elif mes in mes_30:
        if dia not in dias_30:
            op = -1
            print("\n✘ Error, ese día del mes no existe. Intente de nuevo.")
            return op #Retorna un aviso que indica que el día ingresado no se encuentra dentro del rango 1-30.
        else:
            op = 0
            return op #Retorna un aviso que indica que el día ingresado si se encuentra dentro del rango 1-30.
    elif str(mes) == "2":
        if int(anios) % 4 == 0:
            if dia not in febrero_bisiesto:
                op = -1
                print("\n✘ Error, ese día del mes no existe. Recuerde que Febrero es bisiesto. Intente de nuevo.")
                return op #Retorna un aviso que indica que el día ingresado no se encuentra dentro del rango 1-29.
            else:
                op = 0
                return op #Retorna un aviso que indica que el día ingresado si se encuentra dentro del rango 1-29.
        elif dia not in febrero_nobisiesto:
            op = -1
            print("\n✘ Error, ese día del mes no existe. Recuerde que Febrero es no bisiesto. Intente de nuevo.")
            return op #Retorna un aviso que indica que el día ingresado no se encuentra dentro del rango 1-28.
        else:
            op = 0
            return op #Retorna un aviso que indica que el día ingresado si se encuentra dentro del rango 1-28.
    else:
        op = -1
        return -1


def validez_mes(mes): #Función que valida que el rango de meses se encuentre entre 1 y 12.
    meses = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    mes = str(mes)

    if mes not in meses:
        op = -1
        print("\n✘ Error, ese mes del año no existe. Intente de nuevo.")
        return op #Retorna un aviso que indica que el mes ingresado no se encuentra dentro del rango 1-12.
    else:
        op = 0
        return op #Retorna un aviso que indica que el mes ingresado si se encuentra dentro del rango 1-12.


def validez_anio(anio): #Función que realiza la validez del año ingresado. Se asegura que este tenga 4 cifras.
    anio = str(anio)
    op = 0

    if len(anio) == 4:
        op = 0
        return op #Retorna un aviso que indica que el año ingresado es correcto.
    else:
        op = -1
        print("\n✘ Error, solo se permite ingresar un año con 4 cifras. Intente de nuevo.")
        print("Nota: Los 0 no se considerarán al menos que exista un número mayor a 0 delante de el.")
        return op #Retorna un aviso que indica que el año ingreado no existe.


def validez_repeticion(dia1, dia2, mes1, mes2, anio1, anio2): #Función que valida que la primer fecha del rango sea menor a la segunda.
    primerperiodo = dia1 + (30 * mes1) + (360 * anio1)
    segundoperiodo = dia2 +  (30 * mes2) + (360 * anio2)
    if primerperiodo > segundoperiodo:
        print("\n——————————————————————————————————————————————————————————")
        print("✘ Error, el punto final del intervalo de tiempo debe ser mayor al tiempo inicial. intente de nuevo.")
        print("——————————————————————————————————————————————————————————")
        op = -1
        return op, primerperiodo, segundoperiodo #Retorna un aviso de error de rango menor-mayor, la primera fecha y la segunda.
    else:
        op = 0
        return op, primerperiodo, segundoperiodo #Retorna un aviso de rango menor-mayor, la primera fecha y la segunda.

################################################################
#PUNTO 3
def valoresprecio(v, n):  # Función que busca el precio menor y mayor.
    mayor = 0
    menor = 0
    for i in range(n):
        if v[i].precio > mayor:
            mayor = v[i].precio
        if v[i].precio < menor or menor == 0 :
            menor = v[i].precio
    return menor,mayor #Retorna el menor y mayor precio respectivamente.


def valores_min_max(mayor, menor): #Comprueba  que los valores que desea buscar enten dentro del rango de precio
    r_max  = 0
    r_min = 0
    while r_max >= (mayor+1) or r_min <= (menor-1):
        r_max = vldez_es_num_con_negativos("\nIngrese un rango máximo de precio que desea buscar: ➮ ", mensaje_error())
        r_min =vldez_es_num_con_negativos("\nIngrese el rango mínimo de precio que desea buscar: ➮ ", mensaje_error() )
        if r_max >= (mayor+1) or r_min <= (menor-1):
            print("\n————————————————————————————")
            print("✘ Rango de precios incorrecto. Intente de nuevo.")
            print("————————————————————————————")
    return  r_max, r_min #Retorna el precio máximo y mínimo fijado por el usuario.


def brango(n, v, max, min): #Función que se encanrga de almacenar en una lista los productos que cumplen con el rango de precios.
    rangoprecio = [] # vector de rangos
    for i in range(n):
        if v[i].precio in range(min,max+1): # comparacion de los precios con los rangos
            rangoprecio.append(v[i]) #carga del vector
    return rangoprecio # vector cargado con los articulos que admiten el rango de precio


def vldez_es_num_con_negativos(msj, msj2):  # Función que valida que no se ingresen caracteres no numéricos.
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]
    contador = 0
    while True:
        n = input(("{}".format(msj)), )
        for i in range(len(n)):
            if n[i] not in num:
                contador -= 1
            else:
                contador += 1
        if contador == len(n):
            n = int(n)
            return n
        else:
            print(msj2)
            contador = 0


def mostrar_punto3(rangoprecio, provincias): #Función que se encarga de mostrar en pantalla las publicaciones que cumplen con el rango de precios.
    if len(rangoprecio) != 0:
        for i in range(len(rangoprecio)):
            write(rangoprecio,i,provincias)
    else:
        print("\n———————————————————————————————————————————————————————")
        print("✘ Error, no existen publicaciones que se encuentren dentro del rango buscado. Intente de nuevo.")
        print("———————————————————————————————————————————————————————")

##############################################################
#PUNTO 4

def list(v,rb, lista): #Función que guarda en una lista todas las publicaciones que se desean almacenar en favoritos.
    fv = v[rb]
    lista.append(fv)
    list = no_repite(v, rb, lista) #Se llama a una función que valida que no se encuentren repetidas publicaciones.
    return list #Retorna una lista con las publicaciones guardadas en favoritos.


def no_repite(v, rb , lista): #Función que valida que no se encuentren publicaciones favoritas repetidas. Si una se repite, es eliminada.
    cont = 0
    for i in range(len(lista)):
        if lista[i] == v[rb]:
            cont += 1
            if cont > 1:
                del lista[i]
    return lista #Retorna una lista con las publicaciones guardadas en favoritos.


def ordenamiento_insercion(lista): #Función que ordena la lista de publicaciones favoritas.
    n = len(lista)
    for i in range(1,n):
        j = lista[i]
        k = i-1
        while k >= 0 and j.iden < lista[k].iden:
            lista[k+1] = lista[k]
            k -= 1
        lista[k+1] = j


def muestra_pantalla_favoritos(lista, provincias): #Función que muestra las publicaciones guardadas en favoritos.
    print("\n✩ Mis publicaciones favoritas en esta sesión:")
    for i in range(len(lista)):
         write(lista, i, provincias)


def mostrar_guardado_exitoso(): #Función que muestra un mensaje.
    print("\n﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    print("‣ La publicación fue agregada en favoritos. Asegúrese de actualizar su registro de favoritos o perderá sus cambios realizados. ⚠")
    print("﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")

##############################################################
#PUNTO 5
#Función que se encarga de validar que no se repitan publicaciones en favorito y que registra estas en favoritos.dat
def validar_carga_favoritos_binario(lista_copia, lista, lista_agregados_favoritos_binario,favoritos, provincias):
    if lista_copia == -1:
        mostrar_binario_favoritos(favoritos, "rb", provincias)
        return lista_copia, lista_agregados_favoritos_binario #Retorna el respaldo de lista y la lista de agregados.
    else:
        for post in lista_copia:
            if post not in lista_agregados_favoritos_binario:
                archivo_binario_favoritos(favoritos, post, lista)
                lista_agregados_favoritos_binario.append(post)
        mostrar_binario_favoritos(favoritos, "rb", provincias)

    lista_copia = -1
    return lista_copia, lista_agregados_favoritos_binario #Retorna el respaldo de lista y la lista de agregados.

##############################################################
# VALIDACIÓN GENERAL

def vldez_es_num(msj, msj2):  # Función que valida que no se ingresen caracteres no numéricos.
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    contador = 0
    while True:
        n = input(("{}".format(msj)), )
        for i in range(len(n)):
            if n[i] not in num:
                contador -= 1
            else:
                contador += 1
        if contador == len(n):
            n = int(n)
            return n
        else:
            print(msj2)
            contador = 0

##############################################################

def menu():  # Función que muestra el menu de opciones.
    print("\n﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
    print("{:<28}{}{:<28}".format("", "ＭＥＮＵ ＰＲＩＮＣＩＰＡＬ 💻", ""))
    print("﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    print(" １- ↳ Mostrar todos los artículos disponibles en la plataforma.")
    print(" ２- ❤ Comprar: Realizar una compra.")
    print(" ３- ⅀ Mis compras: Mostrar todas tus compras realizadas en un cierto intérvalo de tiempo.")
    print(" ４- ⟺ Rango de precios: Mostrar las publicaciones que se encuentren en un rango determinado de precios.")
    print(" ５- ✩ Agregar favorito: Buscar una publicación cuyo código se ingresa por teclado y agregarla a favoritos.")
    print(" ６- ✔ Actualizar Favoritos: Registra las publicaciones guardadas como favoritos en el sistema de forma permanente.")
    print(" ７- ⌦ Finalizar programa.")


def menu_validacion():  # Función que se encarga de controlar que el número ingresado sean caracteres numéricos.
    op = -1
    opciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    op = input("\n Ingrese una opción deseada: ➮ ")
    print("﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    for i in op:
        if i not in opciones:
            op = -1
            return op
    op = int(op)
    return op  # Retorna la opción ingresada.


def mensajeinicial():  # Función que muestra un texto de bienvenida al iniciar el programa.
    print("\n﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
    print("Bienvenido al modelo de simulación de Mercado Libre®")
    print("﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")


def test():  # Función principal.
    # Mensajes de validaciones
    msj_n_vector = n_vector_mensaje()
    msj_cantidad_compra = cantidadcompra_mensaje()
    msj_busqueda = busqueda_mensaje()
    msj2 = mensaje_error()
    op = 0
    mensajeinicial()

    n, v = n_vector(msj_n_vector, msj2) #Creación del vector v de artículos de la plataforma.
    generardatos(n, v) #Generación de datos del vector v.
    provincias = provincias1()  # Se llama a la función y se almacenan todas las provincias en ella.
    v_nuevos = 0
    control_opciones = [1,2,4,5] #Lista que contiene las opciones que se bloquean en caso de no existir artículos en la plataforma.

    contadorticket = 1 #Contador que sirve para enumerar los tickets generados en formato .txt
    mis_compra, favoritos = archivosbinarios() #Se llama a una función y esta almacena el nombre de tipo binario de 2 archivos.
    vcompra = [0] #Vector vcompra que almacena en un solo índice los artículos comprados para luego ser almacenados en un archivo binario.
    lista = [] #Lista que almacena las publicaciones guardadas en favoritos.
    lista_copia = -1 #Lista que almacena lo más reciente que se almacena en lista. Cuando este se carga en el archivo favoritos.dat
    #entonces se reinicia a -1.
    lista_agregados_favoritos_binario = [] #Lista que almacena los favoritos cargados en el archivo con el fín de evitar repeticiones de carga.
    fv = [] #Lista de apoyo que se utiliza en el punto 4.


    while op != 7: #Menú de opciones.
        menu()
        op = menu_validacion()  # Se llama a función que valida que el input ingresado sean caracteres numéricos.menu()
        romper = vector_sin_productos(v)  # Validación que controla si el vector principal se encuentra vacio.
        if romper == True and (op in control_opciones):
            print("\n‣Lo sentimos, se han agotado todos los artículos del sitio ☹. Vuelve a intentar más tarde.", "\n")
            continue
        if op == 1:  # Mostrar todos los artìculos disponibles
            mostrar_todos_articulos(v, n, provincias)
            continue
        elif op == 2:  # Opción 1
            rb = busqueda(n, v, msj_busqueda, msj2)  # Se realiza la busqueda del código en el vector principal.
            rb_copia_dato_precio = v[rb].precio #Se realiza una copia del precio del índice br para no perderlo.
            rb_copia_dato_codigo = v[rb].iden #Se realiza una copia del código del índice br para no perderlo.
            if rb == -1:
                print("\n—————————————————————————————————————————————————")
                print("✘ El codigo que esta buscando es invalido, no existe ese artículo. Intente de nuevo.")
                print("—————————————————————————————————————————————————")
                continue
            else:
                buy, v, n, envio, cant_sol = cantidadcompra(rb, v, n, msj_cantidad_compra, msj2)

                if buy == 0:  # En caso que se cancele el pedido de compra.
                    print("\n————————————————————————")
                    print("✘ Su pedido fue cancelado correctamente.")
                    print("————————————————————————")
                    continue
                elif buy == 1:  # En caso de aceptar la confirmación de compra.
                    mensaje_ticket_exitoso()
                    print("————————————————————————————————————————————————")
                    print("❤ Su compra se realizó correctamente. ¡Muchas gracias por utlizar Mercado Libre!")
                    print("————————————————————————————————————————————————")
                    total, precio, interes = montos(n, envio, cant_sol, rb_copia_dato_precio) #Cálculo del precio total, precio e interés.
                    envio = envio_numero_a_texto(envio) #Se llama a una función que convierte el número de envio a string.
                    fecha = tiempo() #Función que almacena en la variable fecha la fecha actual en formato string.
                    vcompras(rb_copia_dato_codigo, cant_sol, total, envio, precio, fecha, vcompra) #Carga del vector vcompras.
                    ticket = archivostxt(contadorticket, rb_copia_dato_codigo) #Genera el tipo de nombre del archivo .txt del ticket.
                    archivo_bin_generador(mis_compra,"ab",vcompra, 0) #Crea y carga el archivo binario "miscompras.dat"
                    archivo_txt_compra(ticket, "a", vcompra, rb_copia_dato_precio, rb_copia_dato_codigo) #Crea y carga el archivo .txt de ticket.
                    contadorticket += 1 #Contador de número de ticket emitido por sesión de uso del programa.
                    continue
                else:  # En caso de que la cantidad requerida supere al stock.
                    print("\n✘ La cantidad disponible de stock no satisface la cantidad requerida de artículos. "
                          "Intente de nuevo.")
                    continue
        elif op == 3:  # Opción 2
            primerperiodo, segundoperiodo = ingresar_periodo_fechas() #Carga de las fechas de rango del periodo de búsqueda.
            archivo_bin_compra_mostrar_por_fechas(mis_compra, "rb", primerperiodo, segundoperiodo) #Muestra las compras por rango de fecha.
            continue
        elif op == 4:  # Opción 3
            menor,mayor = valoresprecio(v, n)
            print("\n‣ El Articulo con mayor precio es: ", mayor)
            print("\n‣ El Articulo con menos precio es: ", menor)
            r_max,r_min= valores_min_max(mayor,menor)
            rangoprecio = brango(n, v, r_max,r_min)
            mostrar_punto3(rangoprecio, provincias)
            continue
        elif op == 5:  # Opción 4
            rb = busqueda(n, v, msj_busqueda, msj2)  # Se realiza la busqueda del código en el vector principal.
            if rb == -1:
                print("\n——————————————————————————————————————————————————")
                print("✘ El codigo que esta buscando es invalido, no existe ese artículo. Intente de nuevo.")
                print("——————————————————————————————————————————————————")
                continue
            else:
                lista = list(v,rb, lista) #Se llama a una función que valida que no haya repeticiones de favoritos y lo almacena.
                ordenamiento_insercion(lista) #Se realiza un ordenamiento por insersión.
                mostrar_guardado_exitoso()
                muestra_pantalla_favoritos(lista, provincias) #Muestra en pantalla una lista de favoritos.
                lista_copia = lista #Se realiza una copia de la lista de favoritos para usar de respaldo en la opción 5.
        elif op == 6: # Opción 5
            print("\n ✔ Registro de favoritos actualizado correctamente.")
            lista_copia, lista_agregados_favoritos_binario = validar_carga_favoritos_binario(lista_copia, lista, lista_agregados_favoritos_binario,favoritos, provincias)
            #Función que se encarga de almacenar las publicaciones favoritas en el archivo binario favoritos.dat
            continue
        elif op == 7:
            print("\nMuchas gracias por utilizar nuestra aplicación (•ᴗ•).")
            break
        else:
            print("\n✘ Opción no disponible, intente de nuevo.")  # Otro input distinto a las opciones dispnibles.


if __name__ == '__main__':
    test()

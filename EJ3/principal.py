# 2019_AED_TP3
# Begliardo_83573[1k7]_Bracamonte_81713[1k7]_Herrera_82805[1k7]

from registro import *
import random


# CARGA DEL VECTOR
def generardatos(n, v):  # Función que carga el vector por medio del regristro.
    iden_coleccion = []
    for i in range(n):
        iden = random.randint(100, 900)
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


# OPCIÓN 1
def opcion1(n, v, provincias):  # Función principal de la opción 1.
    ordenar(n, v)  # Se llama a la función ordenar(n,v) y esta procede a ordenar el vector por precio.
    v_nuevos = articulos_nuevos(n, v)  # Se llama a la función y esta retorna un nuevo vector de artículos nuevos.
    for i in range(len(v_nuevos)):  # Se llama al registro y se procede a almacenar la información en el vector.
        write(v_nuevos, i, provincias)
    if len(v_nuevos) == 0:
        print("\n✘ Error, no existen artículos nuevos disponibles. Intente más tarde.")

def ordenar(n, v):  # Función que ordena el vector de menor precio a mayor precio
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].precio > v[j].precio:
                v[i], v[j] = v[j], v[i]


def articulos_nuevos(n, v):  # Función que crea un vector el cual almacenará todos los artículos nuevos
    v_nuevos = []
    for i in range(n):
        if v[i].est == "Nuevo":
            v_nuevos.append(v[i])

    return v_nuevos  # Retorna el vector


# OPCIÓN 2
def usados_calificacion(v, n):  # Función que cuenta la cantidad de artículos que tienen el estado de Usado.
    cantidad = 0
    for i in range(5):
        cantidad = 0
        for j in range(n):
            if v[j].point == i and v[j].est == "Usado":
                cantidad += 1
        usados_calificacion_print(i, cantidad)
        # Llama a una función que muestra en consola los artículos usados por puntos.


def usados_calificacion_print(i, cantidad):
    # Función que muestra en pantalla un mensaje con respecto a la función usados_calificacion(v,n)
    print("\n✮ Artículos usados por", i + 1, "estrellas:", cantidad)


# OPCIÓN 3
def provincias1():  # Función que contiene un listado de provincias para llamar y utilizar
    provincias = ["Córdoba", "Buenos Aires", "Entre Ríos", "Santa Fé", "Corrientes", "Misiones", "Tierra del Fuego",
                  "Santiago del Estero", "San Luís", "Neuquén", "Mendoza", "San Juan", "La Rioja", "Catamarca",
                  "Tucumán", "Salta", "Jujuy", "Chaco", "Formosa", "Río Negro", "Chubut", "Santa Cruz", "La Pampa"]
    return provincias  # Retorna una lista de provincias


def ubicaciongeogeografica_generarmatriz_datos(v, n):
    # Función que crea una matriz estadística y la carga con cantidad de productos vendidos por puntuación y provincia.
    matriz_datos = [[0] * 5 for i in range(23)]  # Creación de la matríz estadística
    for i in range(len(v)):  # Carga de la matriz
        f = v[i].ubc
        g = v[i].point
        matriz_datos[f][g] += 1
    return matriz_datos  # Retorna una matriz con sólo valores numéricos.


def ubicaciongeogeografica_generarmatriz_muestra(v, n):
    # Función que crea una matriz con texto en ella para mostrar en consola y la carga con cantidad de productos
    # vendidos por puntuación y provincia.
    matriz_muestra = [[0] * 6 for i in range(24)]  # Creación de la matríz para mostrar
    for i in range(len(v)):  # Carga de la matriz
        f = v[i].ubc
        g = v[i].point
        matriz_muestra[1 + f][1 + g] += 1
    return matriz_muestra  # Retorna una matriz con texto en ella para mostrar.


def ubicaciongeografica_provinciasmatriz(v, n, provincias, matriz_muestra):
    # Función que añade en la primer columna el nombre de la provincia
    for iii in range(0, 23):
        # Carga la la primer columna con los nombres de las provincias contenidas en la lista de la función provincias1()
        matriz_muestra[1 + iii][0] = "{:<20}".format(provincias[iii])
    return matriz_muestra  # Retorna la matriz


def ubicaciongeografica_eliminarfilasvacias(matriz):
    # Esta función elimina las filas con elementos "vacios",
    # entendiéndose por vacio a una fila con todos sus elementos con valor 0.
    sumaceros = 0
    for i in range(len(matriz)):
        sumaceros = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                sumaceros += 1
        if sumaceros == 5:
            for k in range(6):
                del matriz[i][-1]
    return matriz  # Retorna la matriz despejada


def ubicaciongeografica_cargartextomatriz(matriz):  # Función que ingresa texto en la matriz que se muestra por pantalla
    a = [0, 0, 0, 0, 0, 0]
    contador = 0
    matriz[0][0] = "{:<6}{}{:<5}".format("", "PROVINCIA", "")
    for i in range(1, 6):
        contador += 1
        matriz[0][i] = "{:<2}PRODUCTOS CON {}/5 PUNTOS{:<1}".format("", str(contador), "")
    for j in range(1, len(matriz)):
        for k in range(1, len(matriz[j])):
            matriz[j][k] = "{:<13}{}{:<13}".format("", str(matriz[j][k]), "")
    return matriz  # Retorna la matriz


def ubicaciongeografica_mostrarmatriz(ubicacion_matriz):  # Función que imprime la matriz
    a = []
    print()
    for f in range(len(ubicacion_matriz)):
        if ubicacion_matriz[f] != a:
            print(ubicacion_matriz[f])


# OPCIÓN 4
def totalprovincial_grafica(provincias):
    # Función que crea una tabla (matriz) de códigos por provincia para mostrar en pantalla.
    grafica = [[0] * 2 for i in range(24)]
    for j in range(1):
        del grafica[0][-1]
    grafica[0][0] = "{:<5}{}:{:<5}".format("", "TABLA DE CÓDIGOS POR PROVINCIA", "")
    for k in range(1, 24):
        grafica[k][0] = "{:<20}".format(provincias[k - 1])
    for l in range(1, 24):
        grafica[l][1] = "{:<7}{:<2}{:8}".format("", l - 1, "")
    return grafica  # Retorna dicha matriz


def totalprovincial_salida(valor, matriz):  # Función que cuenta la cantidad de artículos por provincia.
    contador = 0
    for j in range(5):
        contador += matriz[valor][j]
    return contador  # Retorna la cantidad de artículos por provincia


def totalprovincial_salida_print(contador, valor, provincia):
    # Función que imprime unos mensajes relacionados a la función totalprovincial_salida.
    if contador > 0:
        print("\n🏳️ ‍Existen actualmente", str(contador), "artículos disponibles en", str(provincia[valor]) + ".")
    else:
        print("\n⊘ No existen artículos disponibles para esta provincia.")


def totalprovincial_salida_validacion_mensaje():
    msj = "\nIngrese un código de provincia: ➮ "
    return msj


def totalprovincial_salida_validacion(msj, msj2):
    # Función que valida que el código de provincia ingresado se encuentra dentro del rango y sean carácteres numéricos.
    opciones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    valor = vldez_es_num(msj, msj2)
    while not valor in opciones:
        print("\nError, ese código de provincia no existe. Intente de nuevo.")
        valor = int(input("\nIngrese un código de provincia: ➮ "))
    return valor  # Retorna el código ingresado.


# OPCIÓN 5
def cantidadusados(n, v):
    # Función que crea una lista y en ella se van agregando aquellos artículos usados. También cuenta la cantidad de usados.
    vusados = []
    cantidad = 0
    for i in range(n):
        if v[i].est == "Usado":
            cantidad += 1
            vusados.append(v[i])
    return cantidad, vusados  # Retorna la lista vusados y la cantidad de artículos usados.


def sumapreciouse(vusados):  # Función que suma los precios de los artículos usados.
    pp_use = 0
    for i in range(len(vusados)):
        pp_use += vusados[i].precio
    return pp_use  # Retorna la suma de artículos usados por precio.


def use_pro_p(cantidad, vusados, pp_use, provincias):
    # Función que obtiene el promedio entre la suma de los precios de artículos usados por su cantidad
    if cantidad == 0 or len(vusados) == 0:
        print("\n✘ No existen artículos disponibles, intente en otro momento.")
        return
    promuse = (pp_use // cantidad)

    marcador = 0
    print("\n‣El promedio de precio de artículos usados es de $"+str(promuse))
    for i in range(len(vusados)):
        if vusados[i].precio > promuse:
            write(vusados, i, provincias)  # Se muestran los artículos usados que son mayores al promedio de usados.
            marcador += 1

    if marcador == 0:
        print("\n✘ No existen artículos mayores al promedio, intente en otro momento.")
# OPCIÓN 6
def mejorprecio(n, v):  # Función que obtiene el artículo nuevo al mejor precio y puntaje.
    for i in range(n):
        if v[i].est == "Nuevo" and v[i].point > 1:
            return i  # Retorna el indice del artículo nuevo al mejor precio y puntaje.
    return -1  # Retorna una señal que indica que no existe un producto nuevo


def mejorpreciorepetidos(acc, v, n, provincias):  # Función que busca, en base al indice, los mejores.
    # Si se repiten, se imprimen.
    for i in range(n):
        if v[i].precio == v[acc].precio and v[i].point == v[acc].point and v[i].est == v[acc].est:
            write(v, i, provincias)  # Función que llama a la funcion write para imprimir en pantalla.


# OPCIÓN 7
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


def cantidadcompra_mensaje():
    msj = "\nIngrese la cantidad que desea comprar: ➮ "
    return msj


def cantidadcompra(rb, v, n, msj, msj2):  # F unción que se encarga de procesar las compras.
    cant_sol = vldez_es_num(msj, msj2)
    # El primer retorno indica el mensaje que debe mostrarse, el segundo el vector actualizado y
    # el tercero el len del vector.
    if v[rb].cant >= cant_sol:
        x = confirmacioncompra()
        if x == 2:
            return 0, v, n  # Retorna la cancelación de la compra
        v[rb].cant -= cant_sol
        if v[rb].cant == 0:
            del v[rb]
            n = len(v)
        return 1, v, n  # Retorna la concretación de la compra
    else:
        return -1, v, n  # Retorna que la cantidad deseada de artículos es más grande que el stock disponible.


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


# VALIDACION PRINCIPAL
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


def menu():  # Función que muestra el menu de opciones.
    print("\n﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
    print("{:<28}{}{:<28}".format("", "ＭＥＮＵ ＰＲＩＮＣＩＰＡＬ 💻", ""))
    print("﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    print(" １- ↳ Artículos nuevos por precio.")
    print(" ２- ♻ Artículos usados por calificación.")
    print(" ３- ✈ Cantidad de artículos por distribución geográfica y puntuación del vendedor.")
    print(" ４- ⅀ Total provincial de artículos.")
    print(" ５- ‰ Artículos usados con precios mayores al promedio de usados")
    print(" ６- ✔ Compra ideal: El menor precio para un artículo nuevo.")
    print(" ７- ✍ Comprar")
    print(" ８- ☒ Salir de la aplicación.")


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
    msj_totalprovincial = totalprovincial_salida_validacion_mensaje()
    msj2 = mensaje_error()

    op = 0
    mensajeinicial()
    n, v = n_vector(msj_n_vector, msj2)
    generardatos(n, v)
    provincias = provincias1()  # Se llama a la función y se almacenan todas las provincias en ella.
    ubicacion_matriz = 0
    v_nuevos = 0
    grafica = 0
    matriz_datos = ubicaciongeogeografica_generarmatriz_datos(v, n)  # Se genera la matriz de datos y se almacena.
    control_opciones = [1, 2, 3, 4, 5, 6, 7]

    while op != 8:
        menu()
        op = menu_validacion()  # Se llama a función que valida que el input ingresado sean caracteres numéricos.menu()
        romper = vector_sin_productos(v)  # Validación que controla si el vector principal se encuentra vacio.
        if romper == True and (op in control_opciones):
            print("\n‣Lo sentimos, se han agotado todos los artículos del sitio ☹. Vuelve a intentar más tarde.", "\n")
            continue
        if op == 1:  # Opción 1
            opcion1(n, v, provincias)
        elif op == 2:  # Opción 2
            usados_calificacion(v, n)
            continue
        elif op == 3:  # Opción 3
            matriz_muestra = ubicaciongeogeografica_generarmatriz_muestra(v, n)
            # Se genera la matriz gráfica.
            matriz_muestra = ubicaciongeografica_provinciasmatriz(v, n, provincias, matriz_muestra)
            # Se ingresan los strings de provincia en la matriz muestra.
            matriz_muestra = ubicaciongeografica_eliminarfilasvacias(matriz_muestra)
            # Se eliminan las filas vacias de la matriz gráfica.
            matriz_muestra = ubicaciongeografica_cargartextomatriz(matriz_muestra)
            # Se cargan textos en la matriz gráfica.
            ubicaciongeografica_mostrarmatriz(matriz_muestra)  # Muestra la matriz gráfica.
            continue
        elif op == 4:  # Opción 4
            grafica = totalprovincial_grafica(provincias)  # Se crea una tabla(matriz) con las provincias y sus códigos.
            ubicaciongeografica_mostrarmatriz(grafica)  # Se muestra la matriz tabla.
            valor = totalprovincial_salida_validacion(msj_totalprovincial, msj2)  # Se ingresa el código a buscar.
            contadorprovincia = totalprovincial_salida(valor, matriz_datos)
            # Contador que devuelve la cantidad de valores de la provincia.
            totalprovincial_salida_print(contadorprovincia, valor, provincias)
            # Se imprime la cantidad de artículos de la provincia.
            continue
        elif op == 5:  # Opción 5
            cantidad, vusados = cantidadusados(n, v)  # se retorna una lista de usados y su cantidad respectiva.
            pp_use = sumapreciouse(vusados)  # Suma de los precios de los artículos usados.
            use_pro_p(cantidad, vusados, pp_use, provincias)  # Promedio de los artículos y impresión en pantalla.
            continue
        elif op == 6:  # Opción 6
            ordenar(n, v)  # Se ordena el vector por precio, de menor a mayor.
            acc = mejorprecio(n, v)  # Se obtiene el valor del flag.
            if acc == -1:
                print("\n✘ No se encontro un artículo nuevo. Intente más tarde.")
                continue
            else:
                mejorpreciorepetidos(acc, v, n, provincias)  # Se muestran los mejores precios.
                continue
        elif op == 7:  # Opción 7
            rb = busqueda(n, v, msj_busqueda, msj2)  # Se realiza la busqueda del código en el vector principal.
            if rb == -1:
                print("\n✘ El codigo que esta buscando es invalido, no existe ese artículo. Intente de nuevo.")
                continue
            else:
                buy, v, n = cantidadcompra(rb, v, n, msj_cantidad_compra, msj2)
                if buy == 0:  # En caso que se cancele el pedido de compra.
                    print("\n✘ Su pedido fue cancelado correctamente.")
                    continue
                elif buy == 1:  # En caso de aceptar la confirmación de compra.
                    print("\n❤ Su compra se realizó correctamente. ¡Muchas gracias por utlizar Mercado Libre!")
                    continue
                else:  # En caso de que la cantidad requerida supere al stock.
                    print("\n✘ La cantidad disponible de stock no satisface la cantidad requerida de artículos. "
                          "Intente de nuevo.")
                    continue
        elif op == 8:  # Opción 8
            print("\nMuchas gracias por utilizar nuestra aplicación (•ᴗ•).")
        else:
            print("\n✘ Opción no disponible, intente de nuevo. ")  # Otro input distinto a las opciones dispnibles.


if __name__ == '__main__':
    test()

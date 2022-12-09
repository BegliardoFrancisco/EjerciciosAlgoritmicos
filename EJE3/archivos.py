# 2019_AED_TP4
# Begliardo_83573[1k7]_Bracamonte_81713[1k7]_Herrera_82805[1k7]

import pickle
import os
import os.path
import io
from registro import *


def archivo_bin_generador(file, modo, vector, indice): #Función que crea (en caso de no existir) y almacena las compras realizadas en "miscompras.dat"
    p = open(file,modo)
    lista_elementos = vector[indice]
    pickle.dump(lista_elementos,p)
    p.close()


def archivo_binario_favoritos(file, i, lista): #Función que crea y graba el archivo favoritos.dat
    a = open(file,"ab")
    pickle.dump(i,a)
    a.close()

def mostrar_binario_favoritos(file, modo, provincias): #Función que muestra el archivo favoritos.dat
    contador = 0
    if not os.path.exists(file):
        print("\n✘ No se registran publicaciones registradas en favoritos por el momento.")
        return 0
    a = open(file, modo)
    x = os.path.getsize(file)
    while a.tell() < x:
        d = pickle.load(a)
        write_favoritos(d, contador, provincias)
        contador += 1
    a.cls

def archivo_bin_compra_mostrar_por_fechas(file, modo, primerperiodo, segundoperiodo): #Muestra las compras de "miscompras.dat" por rango de fechas.
    contador = 0
    if not os.path.exists(file):
        print("\nNo se registran compras realizadas por el momento.")
        return
    p = open(file,modo)
    x = os.path.getsize(file)

    while p.tell() < x:
        d = pickle.load(p)
        fecha = identificar_fechas(d) #Llama a una función que devuelve los números del string DD/MM/AAAA en una lista.
        diastotal = conversor_de_dias(fecha) #Se llama a una función que convierte los DDMMAAAA en un número de días.
        flag = verificar_fecha_entre_periodo(primerperiodo, segundoperiodo, diastotal)
        if flag == True:
            write_compra(d, contador) #Se llama a una función del módulo registro.py que muestra todos los datos de compras.
        else:
            print("\nNo se han logrado encontrar resultados para ese periodo de tiempo. Intente con otro periodo.")
        contador += 1 #Contador que enumera las cargas de la función write_compra.
    p.close()


def identificar_fechas(d): #Función que agrega en una lista todos los elementos de la fecha en string que son números.
    fecha = []
    for i in d.fecha:
        if i != "/":
            fecha.append(i)

    return fecha #Retorna una lista ordenada de cada número de la fecha DD/MM/AAAA.


def conversor_de_dias(fecha): #Función que convierte los números DDMMAAAA en cantidad de días y luego los suma.
    d1 = int(fecha[0]) * 10
    d2 = int(fecha[1])
    m1 = int(fecha[2]) * 300
    m2 = int(fecha[3]) * 30
    a1 = int(fecha[4]) * 360000
    a2 = int(fecha[5]) * 36000
    a3 = int(fecha[6]) * 3600
    a4 = int(fecha[7]) * 360
    diastotal = d1 + d2 + m1 + m2 + a1 + a2 +a3 + a4

    return diastotal #Retorna un número entero de cantidad de días de la fecha.


def verificar_fecha_entre_periodo(primerperiodo, segundoperiodo, diastotal): #Función que valida que la fecha se encuentre dentro del rango de fechas.
    flag = False
    if primerperiodo <= diastotal <= segundoperiodo:
        flag = True
        return flag #Retorna un aviso de bandera que indica que la fecha de compra se encuentra dentro del rango del periodo.
    else:
        return flag #Retorna un aviso de bandera que indica que la fecha de compra no se encuentra dentro del rango del periodo.


def archivo_txt_compra(file,modo,vector, rb_copia_dato_precio, rb_copia_dato_codigo): #Función que genera un archivo ticket.txt y lo escribe.
    interes = vector[len(vector)-1].monto_total - ((vector[len(vector)-1].precio)) #Cálculo aritmético del interés.
    interes = round(interes,2) #Cálculo aritmético del interés.

    largo = len(vector)
    p = open(file,modo)
    p.write(" -------------------------------------\n")
    p.write("               TICKET\n")
    p.write(" -------------------------------------\n")
    p.write("  Compra #"+str(rb_copia_dato_codigo)+"- "+str(vector[largo-1].fecha)+"\n")
    p.write("\n")
    p.write("  Producto:        $"+str(vector[largo-1].precio)+" ("+str(vector[largo-1].cant_comp)+" x $"+ str(rb_copia_dato_precio)+")\n")
    p.write("  Cargo de envio:  $"+str(interes)+"\n")
    p.write("  Tu pago:         $"+str(vector[largo-1].monto_total)+"\n")
    p.write(" -------------------------------------\n")
    p.write("    ¡Muchas gracias por su compra!\n")
    p.write(" -------------------------------------\n")
    p.close()



# 2019_AED_TP4
# Begliardo_83573[1k7]_Bracamonte_81713[1k7]_Herrera_82805[1k7]

import os
import os.path
import pickle

class Registro(): #Registro de artículos disponibles en la plataforma.
    def __init__(self, iden, precio, ubc, est, cant, point):
        self.iden = iden
        self.precio = precio
        self.ubc = ubc
        self.est = est
        self.cant = cant
        self.point = point


def write(v, i, provincias): #"Display"/muestra de datos de artículos.
    print("\n‣ Articulo N°", i + 1)
    print("\nCódigo de identificación del artículo: ", v[i].iden, end="  |  ")
    print("Precio:", "$"+str(v[i].precio), end="  |  ")
    print("Ubicacion geográfica:", provincias[v[i].ubc])
    print("Estado del artículo:", v[i].est, end="  |  ")
    print("Cantidad disponible:", v[i].cant, "unidades", end="  |  ")
    print("Puntuación del vendedor:", str(v[i].point + 1)+"/5 puntos")

#########################################################################

class Compra(): #Registro de las compras realizadas.
    def __init__(self, iden, cant_comp, precio, envio, monto_total, fecha):
        self.iden = iden
        self.cant_comp = cant_comp
        self.precio = precio
        self.envio = envio
        self.monto_total = monto_total
        self.fecha = fecha


def write_compra(vcompra, contador): #"Display"/muestra de datos de compras.
    print("\n‣ Compra N°",contador + 1)
    print("\nCódigo de identificación del artículo: ", vcompra.iden, end="  |  ")
    print("Cantidad de artículos comprados: ",vcompra.cant_comp, "unidades", end="  |  ")
    print("Precio: ", vcompra.precio, end="  |  ")
    print("Forma de entrega del producto: ",vcompra.envio, end="  |  ")
    print("Monto total pagado (+ envío): ", vcompra.monto_total, end="  |  ")
    print("Fecha de compra: ", vcompra.fecha)


##########

def write_favoritos(v, i, provincias): #"Display"/muestra de datos de publicaciones favoritas.
    print("\n‣ Articulo N°", i + 1)
    print("\nCódigo de identificación del artículo: ", v.iden, end="  |  ")
    print("Precio:", "$"+str(v.precio), end="  |  ")
    print("Ubicacion geográfica:", provincias[v.ubc])
    print("Estado del artículo:", v.est, end="  |  ")
    print("Cantidad disponible:", v.cant, "unidades", end="  |  ")
    print("Puntuación del vendedor:", str(v.point + 1)+"/5 puntos")

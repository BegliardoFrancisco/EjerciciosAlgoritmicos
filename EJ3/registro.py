class Registro():
    def __init__(self, iden, precio, ubc, est, cant, point):
        self.iden = iden
        self.precio = precio
        self.ubc = ubc
        self.est = est
        self.cant = cant
        self.point = point

def write(v, i, provincias):

    print("\n‣ Articulo N°", i + 1)
    print("\nCódigo de identificación del artículo: ", v[i].iden, end="  |  ")
    print("Precio:", "$"+str(v[i].precio), end="  |  ")
    print("Ubicacion geográfica:", provincias[v[i].ubc])
    print("Estado del artículo:", v[i].est, end="  |  ")
    print("Cantidad disponible:", v[i].cant, "unidades", end="  |  ")
    print("Puntuación del vendedor:", str(v[i].point + 1)+"/5 puntos")

# clase producto 
class Productos:
    
    # metodo init o constructor
    def __init__(self, nombre,precio,tipo):
        self.nombre = nombre
        self.precio = precio
        self.tipo=tipo
    
    # metodo str
    def __str__(self):
        return f"El producto creado es --> ['{self.nombre}', cuesta ${self.precio}, corresponde al sector {self.tipo}]"
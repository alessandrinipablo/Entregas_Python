"""  
Segunda Entrega 
Conceptos de Clases y Objetos.
--- Crear un programa que permita el modelamiento de Clientes en una página de compras. 
--- Se debe utilizar el concepto de Programación Orientada a Objetos y lo aprendido en clase.
--  Se evaluará el uso correcto de atributos y métodos.
--  Crear un paquete redistribuible con el programa creado."
--  El proyecto debe ser un archivo comprimido del paquete. 
--  Formatos aceptados: .zip o .tar.gz bajo el nombre “Segunda pre-entrega+Apellido”.
--  "La Clase Cliente debe tener mínimo 4 atributos y 2 métodos.
--  Se debe utilizar el método __str__() para darle nombre a los objetos.
--  Para crear el paquete distribuible también como adicional el archivo de la Pre entrega #1.
--  Es opcional el uso de herencia."

"""
from productos import Productos

# creo clase persona , que seria clase padre
class Persona:   
    
    #constructor clase persona
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# creacion de la clase cliente ( clase Hija  aplico Herencia)
class Cliente(Persona):
    
    # inicializador
    def __init__(self, nombre, apellido, email, telefono):
        super().__init__(nombre, apellido)
        self.email = email
        self.telefono = telefono
        self.carrito = []
        self.precio = 0
    
    
    # metodo str
    def __str__(self):
        return f"Cliente creado --> :[Nombre y apellido{self.nombre}, {self.apellido}, email: {self.email}, nro cel={self.telefono}]"
    

    # metodo para agregar productos al carrito
    def compra(self, producto):
        self.carrito.append(producto.nombre)
        self.precio += producto.precio
        print(f"Usted '{self.nombre} {self.apellido}' compro: '{producto.nombre}', que ha sido añadido al carrito")
        
    # metodo para mostrar los productos en el carrito
    def mostrar_carrito(self):
        print("Se procede a mostrar el carrito".center(100,"-"))
        for producto in self.carrito:
            print(f"{producto}".center(100,"-"))
        print(f"Debe abonar ${self.precio}".center(100,"-")) 
    
#------------------------------------------------------------------
#--------------------cuerpo principal------------------------------
#------------------------------------------------------------------

if __name__ == "__main__":
    
    # instancio un objeto de la clase cliente
    cliente1 = Cliente("Pablo", "Alessandrini", "pablo@alessandrini.com", "123456789")
    print(cliente1)
    
    # instancio objeto de la clase producto
    producto1=Productos("computadora Mac Bok",3543,"informatica")
    producto2=Productos("iphone 16",1230,"celulares")
    
    # muestro los productos que cree
    print(producto1)
    print(producto2)
    
    # aplico metodo compra sobre el objeto cliente, con un parametro de objeto producto
    cliente1.compra(producto1)
    cliente1.compra(producto2)
    
    # muestro atraves del metodo mostrar_carrito ( muestra productos y lo que debe pagar)
    cliente1.mostrar_carrito()

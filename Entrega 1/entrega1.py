""" Objetivo
--- Practicar el concepto de funciones. Preparar la parte lógica para el registro de usuarios.
    Consigna
----Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos.
    Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.
"""
# Importar la función limpiar_pantalla
import os

# funcion que carga el registro en el diccionario
def cargar_registro (diccionario, user, password ):
    diccionario[user] = password
# ---------------------------------------------------------------------------------------------    
    
# funcion que permite loguearse
def logueo(diccionario_registros, usuario, contraseña):

    # Verificar si el usuario y la contraseña ingresados coinciden con los valores del diccionario
    if (usuario in diccionario_registros) and (diccionario_registros[usuario] == contraseña):
        return True
    else:
        return False
# ---------------------------------------------------------------------------------------------    
    
# funcion mostrar los usuarios y contraseñas creados 
def mostrar_base(diccionario_registro):
    print("--------------------------------")
    if len(diccionario_registro)==0:  
        print("----No hay valores cargados aún.")
    else:
        for i in diccionario_registro:
            print("Usuario: \t", i.capitalize(), '->', "\tContraseña: ", diccionario_registro[i])
    print("--------------------------------")
        
# ---------------------------------------------------------------------------------------------        
        
# funcion verificacion de usuario (para no tener dos usuarios iguales)
def usuario_disponible(diccionario_registro, usuario):
    if usuario in diccionario_registro:
        return False
    else:
        return True
# ---------------------------------------------------------------------------------------------
# funcion que permite verificar si ingreso cadena vacia o no
def cadena_vacia(cadena):
    if len(cadena)==0:
        return True
    else:
        return False
# ---------------------------------------------------------------------------------------------
# funcion que me permite limpiar la pantalla cada vez que ejecuto        
def limpiar_pantalla():
    # Para Windows
    if os.name == "nt":
        os.system("cls")
    # Para otros sistemas (Linux, MacOS)
    else:
        os.system("clear")
# ---------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# -----------------------------CUERPO PRINCIPAL-------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


limpiar_pantalla()
registro_usuarios={}
while True:
    # exepcion para controlar si ingresa caracteres en lugar de numeros
    try:    
        print("1. Generar usuario y contraseña")
        print("2. Loguearse")
        print("3. Mostrar base de datos de usuarios creados")
        print("4. Salir")
        opcion = int(input("Opcion: "))
        print("---------------------------")
        
        # opcion para realizar  la creacion de usuario y contraseña
        if opcion == 1:
            # funcion que limpia la pantalla para hacer mas prolijo la visual
            limpiar_pantalla()
            print("=== PROCESO DE CARGA DE USUARIO Y CONTRASEÑA ===")
            usuario = input("Ingrese nombre de usuario: ").lower()
            
            # validar que el usuario este disponible
            while not usuario_disponible(registro_usuarios, usuario):
                print("El usuario que eligio se encuentra activo, por favor elija otro.")
                usuario = input("Ingrese otro nombre de usuario: ").lower()
                
            # validar que el usuario ingresado no este vacio
            while cadena_vacia(usuario) :
                usuario = input("El usuario no debe estar en blanco, ingrese uno valido: ") 
            print("Usuario valido")
                
            contraseña = input("Ingrese contraseña: ")
            
            # validar que la contraseña no este vacia
            while cadena_vacia(contraseña):
                print("La contraseña no puede estar en blanco, por favor ingrese una valida")
                contraseña=input("Contraseña: ")
                
            
            cargar_registro(registro_usuarios, usuario, contraseña)
            print("Base de datos guardada exitosamente.")
            print("---------------------------")
            salir=input("Desea seguir en el programa 'S/N' --> ").lower()
            if salir=="n":
                break
            
            
        # opcion de Loguearse
        elif opcion == 2:
            limpiar_pantalla()
            print("===PROCESO DE LOGUEO===")
            cantidad_permitida=3
            intentos_logueo = 0
            
            # bucle para controlar que los logueos sean menores a tres
            salir=False
            while intentos_logueo < cantidad_permitida and not salir: 
                
                user = input("Ingrese su usuario: ")
                password = input("Ingrese su contraseña: ")
                if logueo(registro_usuarios, user, password):
                    print("Sesión iniciada correctamente.")
                    salir=True
                else:
                    intentos_logueo += 1
                    print("Error de acceso. Por favor intente nuevamente.")
                    print(f"Atencion le quedan {cantidad_permitida-intentos_logueo}")
                    
            # condicional que si llego al maximo permito directamente termina el programa para evitar que hackeen la contraseña
            if intentos_logueo == 3:
                print("Se ha alcanzado el número máximo de intentos........")
                print("Por precaucion se va a salir del programa.")
                break

            salir=input("Desea seguir en el programa 'S/N' --> ").lower()
            if salir=="n":
                break
            
        # opcion mostrar el registro de usuarios realizados
        elif opcion == 3:
            limpiar_pantalla()
            print("===PROCESO DE MOSTRAR LA BASE USUARIOS REGISTRADOS===")
            mostrar_base(registro_usuarios)
            salir=input("Desea seguir en el programa 'S/N' --> ").lower()
            if salir=="n":
                break
            
        # salir del programa principal    
        elif opcion == 4:
            limpiar_pantalla()
            print("===SALIENDO DEL PROGRAMA LOGUEO ===")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")
    except ValueError as e :
        print(f"\tError tipo--> ' {e} ':\nPor favor, ingrese un número entero  para poder ingresar al programa.")
print("===PROGRAMA FINALIZADO===")
# ##########################
# #######FILTRO PYTHON######
# ##########################

from Funciones.funciones import *
from Funciones.funcionesJson import *
from Funciones.funcionesMensajes import *

listaRobusta=abrirJSON()
print("Bienvenido al programa")


booleano=True

while (booleano):
    mensajeIni()
    Opcion=int(input("Ingresar un opcion numerica: "))
    if (Opcion==1):
        mensajeCRUD()
        OpcionUsuario=int(input("Ingresar un opcion numerica: "))
        if(OpcionUsuario==1):
            print("=======================================\
                \n     Creacion de ingrediente nuevo      \
                \n=======================================")
            nombre=str(input("Ingrese el nombre del ingrediente: "))
            descripcion=str(input("Ingrese una breve descripcion del ingrediente\n"))
            precio=int(input("Ingrese el precio del ingrediente: "))
            stock=int(input("Ingrese el stock del ingrediente: "))
            diccionarioNuevo={
                "numeroDato": (listaRobusta[len(listaRobusta)-1]["id"])+1,
                "nombre":nombre,
                "descripcion":descripcion,
                "precio":precio,
                "stock":stock
            }
            listaRobusta.append(diccionarioNuevo)
            guardarJSON(listaRobusta)
            print("")
            print(f'Ingrediente {nombre} fue creado exitosamente.')
        elif(OpcionUsuario==2):
            leerDatos(listaRobusta)
        elif(OpcionUsuario==3):
            Individual=int(input("Ingrese el numero del dato que deseas ver: "))
            

    if (Opcion==2):
        print("\
            \n=======================================\
            \n1. Registrar los ingredientes usados\
            \n2. Leer los ingredientes usados\n")
    if(Opcion==3):
        mensajeCRUD()
    if(Opcion==4):
        mensajeCRUD()
    if(Opcion==5):
        mensajeCRUD()
    if(Opcion==6):
        print("Gracias por usar nuestro gestor de almacenamieto.¡Hasta luego!")
        booleano=False
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
                "numeroDato":(listaRobusta[len(listaRobusta)-1]["numeroDato"])+1,
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
            mostrarUno(listaRobusta,Individual)
        elif(OpcionUsuario==4):
            print("=======================================\
                \n     Actualizar de ingrediente nuevo      \
                \n=======================================")
            Individual=int(input("Ingrese el numero del dato que deseas ver: "))
            mostrarUno(listaRobusta,Individual)
            temporal=listaRobusta[Individual-1]
            nombreTEM=str(input("Ingrese el nombre del ingrediente: "))
            descripcionTEM=str(input("Ingrese una breve descripcion del ingrediente\n"))
            precioTEM=int(input("Ingrese el precio del ingrediente: "))
            stockTEM=int(input("Ingrese el stock del ingrediente: "))
            dicActualizar={"numeroDato":(listaRobusta[len(listaRobusta)-1]["numeroDato"]),"nombre":nombreTEM,"descripcion":descripcionTEM,"precio":precioTEM,"stock":stockTEM}
            listaRobusta[Individual-1]=dicActualizar
        guardarJSON(listaRobusta)
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
# ##########################
# #######FILTRO PYTHON######
# ##########################

from Funciones.funciones import *
from Funciones.funcionesJson import *
from Funciones.funcionesMensajes import *

listaRobusta=abrirJSON()
listaRobusta1=abrirJSON1()
print("Bienvenido al programa")

booleano=True

while (booleano):
    listaRobusta=abrirJSON()
    listaRobusta1=abrirJSON1()
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
        elif(OpcionUsuario==5):
                    Individual=int(input("Por favor ingresar el numero de la persona a eliminar:"))
                    mostrarUno(listaRobusta,Individual)
                    confirmar=int(input("¿Estas seguro que lo deseas eliminar?\n1. SI\n2. NO\n"))
                    if (confirmar==1):
                        temporal= listaRobusta.pop(Individual-1)
                        guardarJSON(listaRobusta)
                        print("Dato eliminado!")
                    else:
                        print("Gracias por confirmar!")
        else:
            print("Regresando al menu principal.......")
    if (Opcion==2):
        print("\
            \n=======================================\
            \n1. Registrar los ingredientes usados\
            \n2. Leer los ingredientes usados\n")
    if(Opcion==3):
        mensajeCRUD()
        OpcionUsuario=int(input("Ingresar un opcion numerica: "))
        if(OpcionUsuario==1):
            print("=======================================\
                \n     Creacion de categoria nueva      \
                \n=======================================")
            nombre=str(input("Ingrese el nombre del ingrediente: "))
            descripcion=str(input("Ingrese una breve descripcion del ingrediente\n"))
            diccionarioNuevo1={
                "numeroDato":(listaRobusta1[len(listaRobusta1)-1]["numeroDato"])+1,
                "nombre":nombre,
                "descripcion":descripcion
            }
            listaRobusta1.append(diccionarioNuevo1)
            guardarJSON1(listaRobusta1)
            print("")
            print(f'Categoria {nombre} fue creada exitosamente.')
        elif(OpcionUsuario==2):
            leerDatos1(listaRobusta1)
        elif(OpcionUsuario==3):
            Individual=int(input("Ingrese el numero del dato que deseas ver: "))
            mostrarUno1(listaRobusta1,Individual)
        elif(OpcionUsuario==4):
            print("=======================================\
                \n     Actualizar de ingrediente nuevo      \
                \n=======================================")
            Individual=int(input("Ingrese el numero del dato que deseas ver: "))
            mostrarUno1(listaRobusta1,Individual)
            temporal=listaRobusta1[Individual-1]
            nombreTEM=str(input("Ingrese el nombre del ingrediente: "))
            descripcionTEM=str(input("Ingrese una breve descripcion del ingrediente\n"))
            dicActualizar={"numeroDato":(listaRobusta1[len(listaRobusta1)-1]["numeroDato"]),"nombre":nombreTEM,"descripcion":descripcionTEM}
            listaRobusta1[Individual-1]=dicActualizar
            guardarJSON1(listaRobusta1)
        elif(OpcionUsuario==5):
                    Individual=int(input("Por favor ingresar el numero de la persona a eliminar:"))
                    mostrarUno1(listaRobusta1,Individual)
                    confirmar=int(input("¿Estas seguro que lo deseas eliminar?\n1. SI\n2. NO\n"))
                    if (confirmar==1):
                        temporal= listaRobusta1.pop(Individual-1)
                        guardarJSON1(listaRobusta1)
                        print("Dato eliminado!")
                    else:
                        print("Gracias por confirmar!")
        else:
            print("Regresando al menu principal.......")
    if(Opcion==4):
        mensajeCRUD()
    if(Opcion==5):
        mensajeCRUD()
    if(Opcion==6):
        print("Gracias por usar nuestro gestor de almacenamieto.¡Hasta luego!")
        booleano=False
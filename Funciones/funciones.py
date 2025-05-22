def leerDatos(listaRobusta):
    for i in range(len(listaRobusta)):
            print("=======================================\
                \n       Dato N.",i+1,"      \
                \n=======================================")
            print("Numero del dato:",listaRobusta[i]["numeroDato"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("descripcion:",listaRobusta[i]["descripcion"])
            print("precio",listaRobusta[i]["precio"])
            print("stock",listaRobusta[i]["stock"])
            print("=======================================")

def mostrarUno(listaRobusta,Individual):
    print("=======================================")
    print("       Dato N.",Individual)
    print("=======================================")
    print("Numero del dato:",listaRobusta[Individual-1]["numeroDato"])
    print("Nombre:",listaRobusta[Individual-1]["nombre"])
    print("descripcion:",listaRobusta[Individual-1]["descripcion"])
    print("precio",listaRobusta[Individual-1]["precio"])
    print("stock",listaRobusta[Individual-1]["stock"])
    print("=======================================")

def leerDatos1(listaRobusta1):
    for i in range(len(listaRobusta1)):
            print("=======================================\
                \n       Dato N.",i+1,"      \
                \n=======================================")
            print("Numero del dato:",listaRobusta1[i]["numeroDato"])
            print("Nombre:",listaRobusta1[i]["nombre"])
            print("descripcion:",listaRobusta1[i]["descripcion"])
            print("=======================================")


def mostrarUno1(listaRobusta1,Individual):
    print("=======================================")
    print("       Dato N.",Individual)
    print("=======================================")
    print("Numero del dato:",listaRobusta1[Individual-1]["numeroDato"])
    print("Nombre:",listaRobusta1[Individual-1]["nombre"])
    print("Especialidad:",listaRobusta1[Individual-1]["especialidad"])
    print("=======================================")


def leerDatos2(listaRobusta2):
    for i in range(len(listaRobusta2)):
            print("=======================================\
                \n       Dato N.",i+1,"      \
                \n=======================================")
            print("Numero del dato:",listaRobusta2[i]["numeroDato"])
            print("Nombre:",listaRobusta2[i]["nombre"])
            print("Especialidad:",listaRobusta2[i]["especialidad"])
            print("=======================================")


def mostrarUno2(listaRobusta2,Individual):
    print("=======================================")
    print("       Dato N.",Individual)
    print("=======================================")
    print("Numero del dato:",listaRobusta2[Individual-1]["numeroDato"])
    print("Nombre:",listaRobusta2[Individual-1]["nombre"])
    print("Especialidad:",listaRobusta2[Individual-1]["especialidad"])
    print("=======================================")


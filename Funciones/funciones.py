def leerDatos(listaRobusta):
    for i in range(len(listaRobusta)):
            print("=======================================\
                \n       Dato N.",i+1,"      \
                \n=======================================")
            print("Nombre:",listaRobusta[i]["nombre"])
            print("descripcion:",listaRobusta[i]["descripcion"])
            print("precio",listaRobusta[i]["precio"])
            print("stock",listaRobusta[i]["stock"])
            print("=======================================")

def mostrarUno(listaRobusta,Individual):
    print("=======================================")
    print("       Dato N.",Individual)
    print("=======================================")
    print("Nombre:",listaRobusta[Individual-1]["nombre"])
    print("descripcion:",listaRobusta[Individual-1]["descripcion"])
    print("precio",listaRobusta[Individual-1]["precio"])
    print("stock",listaRobusta[Individual-1]["stock"])
    print("=======================================")
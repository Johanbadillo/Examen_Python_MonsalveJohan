import json

def abrirJSON():
    dicFinal={}
    with open("./Data/data.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./Data/data.json",'w') as outFile:
        json.dump(dic,outFile)



def abrirJSON1():
    dicFinal={}
    with open("./Data/dataCategorias.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON1(dic):
    with open("./Data/dataCategorias.json",'w') as outFile:
        json.dump(dic,outFile)
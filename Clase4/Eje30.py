from pydoc import doc


def imprimir(dic):
    for indice in dic:
        print("key:",indice,"Value:",dic[indice])
def agregarE (dic,cod,nom):
    dic[cod]=[]
    dic[cod].append(nom)
    dic[cod].append([])
def agregarN(dic,cod,nota):
    dic[cod][1]+=[nota]
def prom(lista):
    suma=0
    for item in lista:
        suma+=item
    return suma/len(lista)


dic={}
imprimir(dic)
agregarE(dic,"0001","Anderson")
agregarN(dic,"0001",10)
agregarN(dic,"0001",9)
agregarN(dic,"0001",11)
imprimir(dic)
print()
print(prom(dic["0001"][1]))

lista1=["a","b","c","d","e"]
lista2=["c","e","f","t","g"]
listaTodo=[]
lSol1=[]
lSol2=[]
lAmbas=[]

listaTodo=lista1+lista2
for palabra in lista1:
    if palabra in lista2:
        lAmbas=lAmbas+[palabra]
    else:
        lSol1=lSol1+[palabra]
for palabra in lista2:
    if palabra not in lista1:
        lSol2=lSol2+[palabra]
print(lista1)
print(lista2)
print(listaTodo)
print(lSol1)
print(lSol2)
print(lAmbas)
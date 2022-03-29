from random import randint

def llenarSec(n):
    lista=[]
    for i in range(1,n+1):
        lista+=[i]
    return lista
def llenarAl(n):
    lista=[]
    num=randint(1,n)
    lista+=[num]
    for i in range(n-1):
        while num in lista:
         num=randint(1,n)
        lista+=[num]
    return lista

n=110
listaA=llenarSec(n);
listaB=llenarAl(n);
print(listaA)
print(listaB)

for i in range (len(listaA)):
    print("La persona:", listaA[i]," es pareja  con la:", listaB[i])
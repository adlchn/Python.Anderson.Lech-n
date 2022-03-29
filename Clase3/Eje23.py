K=150
lista=[80,34,80,23,70]
lista1=[]

suma=0
pesoMax=lista[0]
for i in range(len(lista)):
 
    for j in range(i+1,len(lista)):
        suma=lista[i]+lista[j]
        if(suma<=K):
             print("La suma de: ",lista[i]," + ",lista[j]," = ",suma)
             if(suma>pesoMax):
                pesoMax=suma
print("El peso Maximo posible es:",pesoMax)
                      
            

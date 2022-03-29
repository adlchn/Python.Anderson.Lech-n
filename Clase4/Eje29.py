def imprimir(dic):
    for indice in dic:
        print("Producto:",indice,"Precio:",dic[indice])


dic={}
dic["pan"]=.12
dic["queso"]=2
total=0
menu=True
while menu:
    op=int(input("Elija una opcionn\n1.-Agregar producto\2.-Factura\n3.-Salir"))
    if op==1:
        indice=input("Ingrese indice:")
        valor=float(input("Ingrese el valor:"))
        dic[indice]=valor
        print(dic)
    elif op==2:
        
        factura=True
        while factura:
         imprimir(dic)
         op=int(print("Elija una opcionn\n1.-Agregar producto\n2.-Factura\n3.-Salir"))
         opf=int(input())
        if opf==1:
            
           indice=input("Ingrese indice:")
           cantidad=int(input("Ingrese Cantidad:"))
           if dic.get(indice) is None:
                print("Producto no encontrado")
           else:
                total+=float(dic.get(indice))*cantidad
                print("El total es:",total)
        else:
            factura=False
            total=0   
    elif op==3:
        menu =False
    else: 
        print("Ingres opcion valida")
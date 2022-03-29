from random import randint
op=randint(1,3)
num1=randint(1,10)
num2=randint(1,10)
v=True
a=0
while v:
    op=randint(1,3)
    num1=randint(1,10)
    num2=randint(1,10)
    if op==1:
        res=num1*num2
        print(num1,"*",num2,"=")
        rUsuario=int(input("Ingrese respuesta:"))
        if(res==rUsuario):
            print("Correcto")
            a+=1
        else:
            print("Incorrecto, la respuesta corrreta es:",res)
            v=False
    elif op==2:
        res=num1//num2
        print(num1,"/",num2,"=")
        rUsuario=int(input("Ingrese respuesta:"))
        if(res==rUsuario):
            print("Correcto")
            a+=1
        else:
            print("Incorrecto")
            v=False
        
print("Aciertos:",a)
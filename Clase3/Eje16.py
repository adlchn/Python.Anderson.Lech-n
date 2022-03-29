from random import randint



ganadas=0
ganaMaquina=0
while ganadas<3 and ganaMaquina<3:
    opUsuario=int(input("Ingrese una opcion: \n1.-Piedra\n2.-Papel\n3.-Tijera \n"))
    opMaquina=randint(1,3)
    3
    print("La maquina eligio: ",opMaquina)
    print("El usuario eligio: ",opUsuario)
    if(opUsuario==1 and opMaquina==3)or(opUsuario==2 and opMaquina==1) or(opUsuario==3 and opMaquina==2 ):
        print("Gana el usuario")
        ganadas+=1
    elif opMaquina==opUsuario:
        print("Es un empate")
    else:
        print("Gana la maquina")
        ganaMaquina+=1
    print("Ganadas:",ganadas)
    print("Gana la maquina:",ganaMaquina)




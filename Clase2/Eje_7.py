from random  import randint
#randint(x,y) numero aleatorio entero entre "x"y "y"
#random() numero aleatorio entre 0  y 1
#randrange (x,y,p) numero aleatorio entre "x"y "y" con un paso de "p"
#uniform(x,y) numero aleatorio de tipo float entre "x"  y "y"
ZonaUsuario=int(input("En que zona desea disparar?"))
zonaPortero =randint(1,6);
print("La zona cubierta por el portero es:",zonaPortero)
if ZonaUsuario==zonaPortero:
   
     print("No ha sido un gol")
else:
    print("GOOOL...")
altura =5
espacios=altura
caracter= 1

for i in range(altura):
    for j in range(espacios):
     print(" ",end="")
    
    for k in range (caracter):
        print("* ",end="")
    espacios-=1
    caracter+=1
   
    print()
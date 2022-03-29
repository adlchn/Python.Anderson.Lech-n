
def vasos (n,x):
    total=0
    while n>=x:
        reciclado=n//x
        sobra=n%x
        total+=reciclado
        n=reciclado+sobra
        print("N:",n, "Reciclado:",reciclado," sobran:",sobra," Total:",total)
    return total

n=60
x=8 
vasos(n,x)

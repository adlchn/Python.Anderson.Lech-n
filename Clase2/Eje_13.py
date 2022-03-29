frase="aslv mvklvm kv mslv vmsdvm"
letra="b"
cont=0
for carac in frase:
    if carac==letra:
        cont+=1
if cont>0:
    print("La letra: "+letra+" se encontro: "+str(cont)+" veces")
else:
    print("No se encontro la letra:"+letra+" en la frase:"+frase)
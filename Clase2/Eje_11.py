anioInicio=2000
anioFin=3100

r="Los anios bisiestos entre  "+str(anioInicio)+"  y  "+str(anioFin)+" son:"
for i in range(anioInicio,anioFin):
    if (i%4==0 and i%100!=0) or i%400==0:
        r+=str(i)+","
print(r)
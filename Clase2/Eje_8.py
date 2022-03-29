jornada=48
htrabajadas=49
pagoH=2
pagoE=3.5
if htrabajadas<=jornada:
    salario=htrabajadas*pagoH
else:
    salario=(jornada*pagoH)+((htrabajadas-jornada)*pagoE)

print("Su pago Total es:",salario)
# Construir un programa que permita ingresar 20 números enteros 
# y cuente cuantos números negativos fueron ingresados (+1)

print("    Programa para contar la cantidad de números neutros, positivos y negativos enteros   ")

neutros = 0
negativos = 0
positivos = 0
i=0
while (i<5):
    n = int(input(f'Ingresa el número {i+1}: '))
    if(n==0):
        neutros+=1
    elif(n<0):
        negativos+=1
    else:
        positivos+=1
    i+=1

print(f'{neutros} son números neutros, {negativos} son números negativos y {positivos} son números positivos')
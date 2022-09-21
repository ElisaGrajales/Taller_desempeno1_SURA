##2. Leer información de 10 frutas {nombre, color, precio} para preparar un salpicón; 
##   el programa debe permitir mostrar las 10 frutas ingresadas al mismo tiempo+(1)

print("   Frutas del Salpicón   " )

frutas=[]

for i in range(10):
    fruta={}
    fruta['nombre']=input("Ingrese el nombre de la fruta: ")
    fruta['color']=input("Ingrese el color de la fruta: ")
    fruta['precio']=int (input("Ingrese el precio de la fruta: "))
    frutas.append(fruta)
    
print(f'Las frutas para el salpicón son: {frutas}')
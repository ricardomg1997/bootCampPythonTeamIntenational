nombre = input("Ingrese el nombre del estudiante => ")
edad = input("Ingrese la edad del estudiante => ")

estudiante = []
notas = []
estudiante.append(nombre)
estudiante.append(edad)

num = int(input("Ingrese nota 1 => "))
num1 = int(input("Ingrese nota 2 => "))
num2= int(input("Ingrese nota 3 => "))
num3 = int(input("Ingrese nota 4 => "))
num4 = int(input("Ingrese nota 5 => "))

notas.append(num)
notas.append(num1)
notas.append(num2)
notas.append(num3)
notas.append(num4)

prom_notas = sum(notas)/5

estudiante.append(notas)
#print(estudiante)
#print(prom_notas)
if prom_notas >= 3:
    print(f"El estudiante {estudiante[0]} aprobó con un promedio de {prom_notas} y sus notas fueron: {estudiante[-1]}")
else:
    print(f"El estudiante {estudiante[0]} reprobó con un promedio de {prom_notas} y sus notas fueron: {estudiante[-1]}")
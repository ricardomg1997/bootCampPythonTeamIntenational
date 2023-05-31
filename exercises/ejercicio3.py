entrada = { a for a in range(6)}
def estadistica(lista):
    salida ={}
    promedio, value = "promedio",sum(lista)/len(lista)
    salida[promedio] = value
    pares, value = "pares", [x for x in lista if x%2 == 0]
    salida[pares] = value
    impares, value = "impares", [x for x in lista if x%2 == 1]
    salida[impares] = value
    print(salida)

estadistica(entrada)
print(entrada)
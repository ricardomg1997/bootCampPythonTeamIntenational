
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 28]

def find_maximum(lista):
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo
    

print(f"El número máximo de la lista es el: {find_maximum(lista)}")
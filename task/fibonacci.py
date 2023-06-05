#imprimir los 10 primeros terminos de la secuencia fibonacci
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,

def fibonacci(n):
    lista =[1, 1]
    if n < 2:
        print(n)
    elif n == 2:
        print(lista)
    else:
        i=1
        for x in range(1,n-1):
            lista.append(lista[i-1]+lista[i])
            i += 1
    print(lista)
    
fibonacci(10)
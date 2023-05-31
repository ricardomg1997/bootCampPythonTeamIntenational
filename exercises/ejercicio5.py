'''num = 0
def suma(n):
  if n == 0:
    return 0
  return n + suma(n-1)
print(sum(5))



def invertir_cadena(cadena):
    return cadena[::-1]


def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida


print(invertir_cadena("Hola"))
'''

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
    
print(fib(8))
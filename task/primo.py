
#num = int(input("Ingrese un número entero => "))

def ingreso_num():
    num = int(input("Ingrese un número entero => "))
    return es_primo(num)

def es_primo(num):
    if num % 2 == 0:
        result = "El número", num, "es par"
        print("este número no es primo")
        ingreso_num()
    elif num % 3 == 0:
        result = "El número", num, "es impar"
        print("este número no es primo")
        ingreso_num()
    else:
       
        print("El número", num, "es primo")
        ingreso_num()

ingreso_num()

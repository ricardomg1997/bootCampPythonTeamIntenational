num = int(input("Ingrese un número entero => "))
num2 = int(input("Ingrese otro número entero => "))

#funcion para operar dos numeros
def suma(a,b):
  """
    Está función suma dos números
    Esta función recibe dos parámetros, en este caso dos enteros.
        a : (int) toma el primer valor ingresado por el usuario
        b : (int) toma el segundo valor ingresado por el usuario
  """
  return a+b
  

print(f"La suma es: {str(suma(num, num2))}")

import time

inicio = time.time()
lista = [1, 5, 7, 3, 8, 9, 0, 2, 4]

def called_timer(funcion):
    def nueva_funcion(lis):
        print("Se va a llamar")
        c = funcion(lis)
        print("Se ha llamado")
        fin = time.time()
        print(f"---Proceso finalizado.---\n => El tiempo de ejecución ha sido de {round(fin - inicio, 5)} segundos.")
        return c
    return nueva_funcion

@called_timer
def ordenador(lis):
    
    print("Entra en funcion ordenador")
    print(f"(La lista original es: {lis})")
    lis.sort() # Ordena la lista de menor a mayor
    print(f"(La lista ordenada es: {lis})")

ordenador(lista)

# Se va a llamar
# Entra en funcion ordenador
# Resultado función ordenador
# Se ha llamado
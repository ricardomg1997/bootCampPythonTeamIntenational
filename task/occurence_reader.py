
fichero = open('texto.txt')
cadena = fichero.readline() #leo y recupero la cadena de texto

def occurrence_reader(cadena):
    
    lista_palabras = cadena.split() #Divido la cadena en  

    frecuencia = []
    for p in lista_palabras:
        frecuencia.append(lista_palabras.count(p))

    dic = dict(zip(lista_palabras, frecuencia)) #uno las listas y convierto en diccionario
    print(f"Diccionario de ocurrencias\n {str(dic)}")

occurrence_reader(cadena)
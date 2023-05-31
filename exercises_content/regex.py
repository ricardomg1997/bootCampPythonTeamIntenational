import re

def re_match_search(cadena: str):
    if re.match("gato", cadena):
        print("se encontro gato match")
    if re.search("ato", cadena):
        print("se encontro ato con search")

#re_match_search("gato que esta triste y azul")
#\d*\.\d+| por si hace falta
def extraer_numeros(cadena: str):
    """ función para extrar números de una cadena """
    nums = re.findall("(\d+.\d*)", cadena)
    print(nums)

extraer_numeros("1 hola, esto es una prueba 2.3, 13 veremos si se encuentran 357, 457")
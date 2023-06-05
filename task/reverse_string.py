
frase = input("Por favor ingrese la oración a revertir: ")
def reverse_string(frase):
    reverso = ""
    for letra in frase:
        reverso = letra + reverso
    return reverso
    
print(reverse_string(frase))
frase = 'somos'

def palindromo(frase):
    
    lis = []

    for letra in frase:
        lis.append(letra)
    
    fin = len(lis) - 1

    for inicio in range(len(lis)):
        if lis[inicio] == lis[fin]:
            if inicio >= fin:
                print(f"La palabra {frase} es palíndroma")
                return True
                
            inicio += 1
            fin -= 1
        else:
            print(f"La palabra {frase} no es palíndroma")
            return False
       
palindromo(frase)
import unittest

def palindromo(frase):
    
    lis = []

    for letra in frase:
        lis.append(letra)
    
    fin = len(lis) - 1

    for inicio in range(len(lis)):
        if lis[inicio] == lis[fin]:
            if inicio >= fin:
                return True
                
            inicio += 1
            fin -= 1
        else:
            return False
       
class TestPalindrome(unittest.TestCase):
    def test_palindro(self):
        palabra = "somos"
        result = palindromo(palabra)
        self.assertEqual(result, True)

    def test_no_palindro(self):
        palabra = "seremos"
        result = palindromo(palabra)
        self.assertEqual(result, False)


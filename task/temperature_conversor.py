fa_temperature = float(input("Ingrese la temperature en Fahrenheit => "))

def tem_conversor(temp):
    """
        Función para relizar la conversión de temperatura de Fahrenheit a Celsius
        Esta función recibe como parámetro un número.
        temp : float, toma el valor ingresado por el usuario.
        para la conversión tenemos en cuenta qué:
            * 32 grados Fahrenheit son 0 grados Celsius
            * La fórmula para la conversión es: (32F - 32) x 5/9 = 0 °C
    """

    result = float("{0:.4f}".format((temp -32)*5/9 ))
    return result

print(f"La temperatura en grados Celsius aproximadamente es: {str(tem_conversor(fa_temperature))} °C")
print(fa_temperature)
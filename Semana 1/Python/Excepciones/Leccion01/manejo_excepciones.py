from NumerosIgualesException import NumerosIgualesException
# Importamos la clase NumerosIgualesException desde el archivo NumerosIgualesException.py

resultado = None
# Inicializamos la variable "resultado" como "None"

try:
    a = int(input("Digite el primer número: "))
    # Pedimos al usuario que introduzca el primer número
    b = int(input("Digite el segundo número: "))
    # Pedimos al usuario que introduzca el segundo número
    if a == b:
        # Si los números son iguales, lanzamos una excepción personalizada
        raise NumerosIgualesException("Son números iguales")
    resultado =  a / b
    # Realizamos la operación de división y guardamos el resultado en la variable "resultado"
except TypeError as e:
    # Si ocurre un TypeError, imprimimos un mensaje de error
    print(f" TypeError - Ocurrió un error: {type(e)}")
except ZeroDivisionError as e:
    # Si ocurre un ZeroDivisionError, imprimimos un mensaje de error
    print(f"ZeroDivisionError - Ocurrió un error: {type(e)}")
except Exception as e:
    # Si ocurre cualquier otra excepción, imprimimos un mensaje de error genérico
    print(f"Exception - Ocurrió un error: {type(e)}")
else: # Si no se han lanzado excepciones, imprimimos un mensaje de éxito
    print("No se arrojo ninguna excepción")
finally: # Siempre se ejecuta, independientemente de si se han lanzado excepciones o no
    print("Ejecución de este bloque finally")

print(f"El resultado es: {resultado}")
# Imprimimos el resultado de la operación de división, si se ha realizado correctamente
print("seguimos...")
# Indicamos que la ejecución del programa continúa


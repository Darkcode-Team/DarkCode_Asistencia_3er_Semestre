class NumerosIgualesException(Exception):
    # Define una clase llamada "NumerosIgualesException" que extiende de la clase base "Exception"

    def __init__(self, mensaje):
        # El método constructor de la clase acepta un argumento llamado "mensaje"

        self.message = mensaje
        # Inicializa un atributo de instancia llamado "message" con el valor del argumento "mensaje"

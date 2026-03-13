# Clase que representa un vehículo dentro del sistema
class Vehiculo:

    # Constructor de la clase
    # Inicializa los atributos del vehículo
    def __init__(self, placa, marca, propietario):
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

 # Método para acceder a la placa
    def get_placa(self):
        return self.placa

    # Método para acceder a la marca
    def get_marca(self):
        return self.marca

    # Método para acceder al propietario
    def get_propietario(self):
        return self.propietario

    # Método para obtener todos los datos del vehículo
    def obtener_datos(self):
        return self.placa, self.marca, self.propietario
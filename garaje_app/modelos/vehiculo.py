# Clase que representa un vehículo dentro del sistema
class Vehiculo:

    # Constructor de la clase
    # Inicializa los atributos del vehículo
    def __init__(self, placa, marca, propietario):
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

        # Método para obtener los datos del vehículo
    def obtener_datos(self):
        return self.placa, self.marca, self.propietario


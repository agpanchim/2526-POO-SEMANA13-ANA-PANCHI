# Clase que representa un vehículo dentro del sistema
class Vehiculo:

    # Constructor de la clase
    # placa: str -> cadena que identifica al vehículo
    # marca: str -> cadena que indica la marca del vehículo
    # propietario: str -> cadena con el nombre del dueño
    def __init__(self, placa: str, marca: str, propietario: str):
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
# Importamos la clase Vehiculo desde el paquete modelos
from modelos.vehiculo import Vehiculo

# Clase que gestiona las operaciones del garaje
class GarajeServicio:

    # Constructor de la clase
    # Se crea una lista para almacenar los vehículos
    def __init__(self):
        self.vehiculos = []

    # Método para agregar un vehículo al garaje
    def agregar_vehiculo(self, placa, marca, propietario):

        # Se crea un objeto Vehiculo
        vehiculo = Vehiculo(placa, marca, propietario)

        # Se agrega el vehículo a la lista
        self.vehiculos.append(vehiculo)

    # Método para obtener la lista de vehículos registrados
    def listar_vehiculos(self):

        return self.vehiculos
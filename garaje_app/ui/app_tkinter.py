import tkinter as tk
from tkinter import ttk, messagebox
from servicios.garaje_servicio import GarajeServicio


# Clase principal de la interfaz gráfica
class App:

    # Constructor de la interfaz
    def __init__(self):

        # Se crea la ventana principal
        self.root = tk.Tk()
        self.root.title("Sistema Básico de Gestión de Garaje")

        # Instancia del servicio que gestiona los vehículos
        self.servicio = GarajeServicio()

        # Etiquetas del formulario
        tk.Label(self.root, text="Placa").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.root, text="Marca").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.root, text="Propietario").grid(row=2, column=0, padx=5, pady=5)

        # Campos de entrada de texto
        self.txt_placa = tk.Entry(self.root)
        self.txt_marca = tk.Entry(self.root)
        self.txt_propietario = tk.Entry(self.root)

        self.txt_placa.grid(row=0, column=1, padx=5, pady=5)
        self.txt_marca.grid(row=1, column=1, padx=5, pady=5)
        self.txt_propietario.grid(row=2, column=1, padx=5, pady=5)

        # Botón para agregar vehículo
        btn_agregar = tk.Button(
            self.root,
            text="Agregar Vehículo",
            command=self.agregar
        )
        btn_agregar.grid(row=3, column=0, pady=10)

        # Botón para limpiar los campos
        btn_limpiar = tk.Button(
            self.root,
            text="Limpiar",
            command=self.limpiar
        )
        btn_limpiar.grid(row=3, column=1, pady=10)

        # Tabla para mostrar los vehículos registrados
        self.tabla = ttk.Treeview(
            self.root,
            columns=("placa", "marca", "propietario"),
            show="headings"
        )

        # Encabezados de la tabla
        self.tabla.heading("placa", text="Placa")
        self.tabla.heading("marca", text="Marca")
        self.tabla.heading("propietario", text="Propietario")

        # Posición de la tabla
        self.tabla.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Método que se ejecuta al presionar el botón Agregar
    def agregar(self):

        # Obtener datos del formulario
        placa = self.txt_placa.get().strip()
        marca = self.txt_marca.get().strip()
        propietario = self.txt_propietario.get().strip()

        # Validar que los campos no estén vacíos
        if placa == "" or marca == "" or propietario == "":
            messagebox.showwarning(
                "Campos vacíos",
                "Todos los campos son obligatorios"
            )
            return

        # Registrar el vehículo
        self.servicio.agregar_vehiculo(placa, marca, propietario)

        # Actualizar tabla
        self.actualizar_tabla()

        # Limpiar formulario
        self.limpiar()

    # Método para actualizar la tabla de vehículos
    def actualizar_tabla(self):

        # Eliminar registros actuales
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # Insertar vehículos en la tabla
        for vehiculo in self.servicio.listar_vehiculos():

            datos = vehiculo.obtener_datos()

            self.tabla.insert(
                "",
                "end",
                values=datos
            )

    # Método para limpiar los campos del formulario
    def limpiar(self):

        self.txt_placa.delete(0, tk.END)
        self.txt_marca.delete(0, tk.END)
        self.txt_propietario.delete(0, tk.END)

    # Método que ejecuta la aplicación
    def run(self):

        self.root.mainloop()
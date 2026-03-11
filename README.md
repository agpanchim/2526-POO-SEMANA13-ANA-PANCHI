# 2526-POO-SEMANA13-ANA-PANCHI
Aplicación de escritorio con interfaz gráfica utilizando Tkinter, 
aplicando la arquitectura modular vista en clase: modelos, servicios, ui y main.py.  
La aplicación permitirá registrar vehículos que ingresan a un garaje y visualizar 
la información desde una interfaz gráfica.


# Sistema Básico de Gestión de Garaje 

## Descripción
Este proyecto consiste en una aplicación de escritorio desarrollada en **Python** utilizando la librería **Tkinter**.  
El sistema permite registrar vehículos que ingresan a un garaje y visualizar la información en una interfaz gráfica.

La aplicación fue desarrollada aplicando **arquitectura modular**, separando el código en modelos, servicios y la interfaz gráfica.

---

## Funcionalidades

- Registrar vehículos ingresando:
  - Placa
  - Marca
  - Propietario
- Mostrar los vehículos registrados en una tabla.
- Limpiar los campos del formulario.
- Validar que los campos no estén vacíos.

### Descripción de carpetas

**modelos**  
Contiene la clase que representa el objeto Vehiculo.

**servicios**  
Contiene la lógica del sistema, como registrar y listar vehículos.

**ui**  
Contiene la interfaz gráfica desarrollada con Tkinter.

**main.py**  
Archivo principal que inicia la aplicación.
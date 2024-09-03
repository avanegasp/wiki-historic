# Wiki-historic

## Descripción del Proyecto
Este proyecto es una API desarrollada con Flask, un microframework para Python, que ofrece funcionalidad para gestionar perfiles y realizar búsquedas avanzadas en Wikipedia. A continuación se detallan los componentes y características principales:

### Rutas/Endpoints: La API expone varias rutas que permiten realizar operaciones HTTP:

- '/' para verificar el funcionamiento general de la API.
- '/profiles' para obtener una lista de perfiles existentes en la base de datos.
- '/create_profile' para crear un nuevo perfil y realizar una búsqueda en Wikipedia basada en los datos del perfil.

### Métodos HTTP: La API utiliza métodos HTTP estándar:

- GET para obtener datos.
- POST para crear nuevos registros.

- Peticiones a Wikipedia: La API integra la biblioteca requests para realizar peticiones a la API de Wikipedia. Al crear un perfil, se envía una consulta a Wikipedia utilizando los datos del perfil (nombre, país, ciudad y año). Los resultados de la búsqueda en Wikipedia se incluyen en la respuesta de la API, proporcionando a los usuarios información relevante directamente desde Wikipedia.

- Respuestas en JSON: La API devuelve datos en formato JSON, lo que facilita la interoperabilidad con otras aplicaciones web y servicios.

- Interacción con Base de Datos: La API emplea SQLAlchemy y Flask-SQLAlchemy para manejar la base de datos y realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los perfiles. Esto incluye la validación de datos y la gestión de errores.

Este proyecto destaca por su capacidad para crear una API robusta que combina la gestión de perfiles con la integración de datos externos, proporcionando una solución completa para interactuar con la API de Wikipedia y manipular datos de perfil.

# Prueba_Fundamentos_de_programacion_en_Python

Este proyecto lista especies de aves típicas de Chile junto con sus nombres en español e inglés, y sus imágenes correspondientes. Utiliza una API proporcionada por la asociación de Amantes de los pájaros de Chile.

Funcionalidades

Llamado a la API: Se realiza un llamado a la API 'https://aves.ninjas.cl/api/birds' para obtener la información necesaria.

Templates HTML: Se han creado templates HTML para mostrar la información de las aves.

Exportación a HTML: El sitio web se exporta como un archivo HTML que puede ser abierto en el navegador.

Modularización 

El código se ha modularizado en 3 archivos , por un lado el archivo obtener_datos_aves.py para obtener los datos desde las api y retornar desde una funcion en formato JSON, el archivo generador_html.py, que estructura la plantilla del html y el archivo main.py que es la estructura principal del programa y llama los archivos anteriores, estoigue las buenas prácticas de programación para facilitar la legibilidad y la facil manipulacion de estos.
from obtener_datos_aves import obtener_datos
from generador_html import generar_template_html

#obtener datos de las aves llamando a la funcion obtener_datos y guardandolo en la variable datos_aves
datos_aves = obtener_datos()

# generar el string de la plantilla
plantilla_str = generar_template_html(datos_aves)

# genera en un archivo .html creado en la funcion generar_template_html
with open('aves_de_chile.html', 'w') as f:
        f.write(plantilla_str)

print("Archivo HTML generado exitosamente: aves_de_chile.html")

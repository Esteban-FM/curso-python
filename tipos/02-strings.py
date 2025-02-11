nombre_curso = "Ultimate Python"

descripcion_curso = """

Ultimate Python,
este curso contempla los detalles basicos de python.
"""

# print(nombre_curso, descripcion_curso)

print(len(nombre_curso))
# donde "len" es el argumento
#  y "nombre_curso" el valor

print(nombre_curso[0])
# los parentesis "[]" en este caso es para acceder al indice
#  dentro del mismo se coloca el valor del caracter al que queremos acceder

print(nombre_curso[0:8])
# para cortar un string colocamos parentesis de corchete seguido del string
# dentro del mismo colocamos ":" de esta manera [:]
# se coloca el valor del lado izquierdo indicando el indice(de donde comienza)
# y un valor del lado derecho indicando cuantos caracteres hay que recortar

print(nombre_curso[9:])
# al momento en que no se coloque un valor del lado derecho,
# se rellenara hasta el final del string sin restriccion alguna

print(nombre_curso[:8])
# al momento en que no se coloque un valor del lado izquierdo,
# se tomara en cuenta desde el inicio del string hasta la restriccion
# colocada en el valor derecho

print(nombre_curso[:])
# al momento en el que no se coloquen valores, se imprimira el total del
# string desde inicio a fin sin restricciones

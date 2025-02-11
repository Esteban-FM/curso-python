animal = " viEJo PeRRo "
print(animal.upper())
# Metodo es una funsion que se encuentra dentro de un objeto
# .upper() Toma el string que esta dentro  de la variable y lo pasa
# a letras mayusculas

print(animal.lower())
# .lower() Toma el string que esta dentro de la variable y lo pasa
#  a letras minusculas

print(animal.capitalize())
# .capitalize() toma el primer caracter del string mientras no sea un espacio y lo pasa
# a mayuscula, haciendo al resto minusculas

print(animal.strip().capitalize())
# para resolver el uso de capitalize con un texto en el que empieze con espacios
# encadenamos los metodos agregando .strip() antes de utilizar .capitalize() lo que
# borrara los espacios y le permitira dar formato correctamente a .capitalize()

print(animal.title())
# .title()  toma la primera letra de cada palabra que se encuentra
# dentro del string para pasarlo a mayuscula y lo demas a minuscula

print(animal.strip())
# .strip() remueve todo espacio que se encuentre a la izquierda y
# y a la derecha del string
print(animal.rstrip())
# .rstrip() remueve los espacios de la derecha del string
print(animal.lstrip())
# .lstrip() remueve los espacios de la izquierda del string

print(animal.find("eR"))
# .find() buscara una cadena de caracteres que le indiquemos
#  lo que hara es devolvernos el valor inicial o de posicion de la
# cadena de caracteres que indicamos

print(animal.find("ER"))
# Al momento de colocar una cadena de caracteres que no se encuentre
# dentro del string, el valor que nos devolvera sera de "-1"
# porque es un valor no encontrado ya que no existe

print(animal.replace("Pe", "Fie"))
# .replace("", "") remplazara los caracteres que coloquemos dentro de
# las primeras " " por el colocado dentro de las segundas " " antes
# de imprimirlo, en caso de no encontrar la cadena de caracteres que
# cambiaremos no se realizara el cambio

print("PeR" in animal)
#  " " in busca un caracter o una cadena de caracteres y nos devolvera
# un valor booleano dependiendo de si se encuentra o no

print("PeR" not in animal)
#  " " not in busca si no se encuentra un caracter o una cadena de
# caracteres y nos devolvera un valor booleano dependiendo de si
# se no encuentra o si no se encuetra

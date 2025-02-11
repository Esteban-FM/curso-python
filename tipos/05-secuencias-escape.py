
curso = 'Ultimate "Python"'
curso2 = "Ultimate \"Python\""
# al colocar el \ "backslash" le da a entender que no tome el siguiente caracter
# propio del lenguaje, sino que lo utilize como parte del contenido delstring
curso3 = "Ultimate \n \"Python\""
# al colocar el \n "backslash" + n tomara el string que viene o lo que sigue para
# pasarlo a una nueva linea

print(curso)
print(curso2)
print(curso3)

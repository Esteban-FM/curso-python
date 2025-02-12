numero = 2  # integer -> entero
decimal = 1.2  # float
imaginario = 2 + 2j  # 2 + 2i  el "i" es la raiz cuadrada de -1,
# en donde "i" es un valor imaginario

numero = numero + 2
# aqui estamos tomando el valor de numero y lo estamos remplazando por si misma
# como en este caso tiene valor de 2 lo que sucedera es un reemplazo
# numero que es igual a "2" + 2  da igual a 4 dandole un valor final de 4 a la variable numero
print("numero es igual a", numero)

numero_ejemplo = 2
# Otra manera de hacer lo mismo sin tener que reemplazarlo
numero_ejemplo += 2
# la anotacion de += quiere decir que la variable a la izquierda
# se le sumara 2 y luego se le asignara de nuevo a la misma variable
print("numero += es", numero_ejemplo)

print(1 + 3)  # suma
print(1 - 3)  # resta
print(1 * 3)  # multiplicacion
print(1 / 3)  # division
print(1 // 3)  # division sin decimales
print(8 % 3)  # modulo, de la divicion dame el porcentaje sobrante
print(2 ** 3)  # potencia o elevado a

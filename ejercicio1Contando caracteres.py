frase = input("Escribe una frase: ")# input() Le pide al usuario que escriba algo
total_caracteres = len(frase)#len() Cuenta **cuántos caracteres** tiene la frase
espacios = frase.count(" ")#.count() Cuenta **cuántas veces aparece un espacio** (`" "`) en la frase.

print(f"La frase tiene {total_caracteres} caracteres en total.") # print()` y f-string  Muestra en pantalla el total de caracteres.
print(f"La frase tiene {espacios} espacios.")#print()` y f-string Muestra en pantalla cuántos espacios tiene la frase.

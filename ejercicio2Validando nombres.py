nombre = input("Escribe tu nombre completo: ")

if nombre.replace(" ", "").isalpha():
    if nombre.istitle():
        print("El nombre es válido.")
    else:
        print("El nombre debe comenzar con mayúscula.")
else:
    print("El nombre solo debe contener letras.")
cadena = input("ingrese una oracion: ")
invertida = ""

for letra in cadena:
    invertida = letra + invertida
    if (invertida == cadena):
        print ("La palabra es capicua ")    
        print (invertida)
    else: 
        print("La palabra no es capicua")

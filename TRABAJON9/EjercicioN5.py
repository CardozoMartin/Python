#desarrolle un algoritmo para determinar si un año es o no bisiesto;

año = int(input("Ingrese un año : "));

if año % 4 == 0 :
    print("es año bisiesto");
else :
    print("No es bisiesto");
# ingrese 2 numeros enteros identifique cual es el menor e imprimir es menor en caso contrario imprimi es mayor

n1 = int(input("Ingrese el primer numero : "));
n2 = int(input("Ingrese el segundo numero : "));

if n1 > n2 :
    print(n1 , "es mayor que : ", n2);
else:
    print(n2, "es mayor que : " ,n1);
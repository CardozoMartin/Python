# elabore un algoritmo que permita ingresar el numero de partidos ganados, perdidos y empatados por abc, se debe mostrar su puntaje total, teniendo en cuenta que por el  cada partido ganado se obtendra 3 puntos y empatados 1 y perdidos 0 puntos

ganado = int(input("Ingrese lo partidos ganados : "));
perdidos = int(input("ingrese los partidos perdidos : "));
empatados = int(input("Ingrese la cantidad de partidos empatados : "));

totalGanados = ganado * 3;
totalEmpatados = empatados;

totalPartidos = ganado + perdidos + empatados;
puntajeFinal = totalGanados + totalEmpatados;

print("El total de partidos jugandos son : ", totalPartidos);
print("El total del puntaje es : ", puntajeFinal);
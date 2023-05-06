from claseRegistro import Registro

if __name__ == "__main__":
 datos_mensuales = [[None for j in range(24)] for i in range(31)]
with open("datos.csv") as archivo:
    for linea in archivo:
        valores = linea.strip().split(",")
        dia = int(valores[0])
        hora = int(valores[1])
        temperatura = float(valores[2])
        humedad = float(valores[3])
        presion = float(valores[4])
        registro = Registro(temperatura, humedad, presion)
        datos_mensuales[dia-1][hora] = registro

def min_max_por_variable(variable):
    min_valor = float("inf")
    min_dia = None
    min_hora = None
    max_valor = float("-inf")
    max_dia = None
    max_hora = None
    for i in range(31):
        for j in range(24):
            registro = datos_mensuales[i][j]
            if registro is not None:
                valor = getattr(registro, variable)
                if valor < min_valor:
                    min_valor = valor
                    min_dia = i+1
                    min_hora = j
                if valor > max_valor:
                    max_valor = valor
                    max_dia = i+1
                    max_hora = j
    return (min_dia, min_hora, min_valor, max_dia, max_hora, max_valor)

def temperatura_promedio_mensual_por_hora():
    promedios = [0 for i in range(24)]
    conteos = [0 for i in range(24)]
    for i in range(31):
        for j in range(24):
            registro = datos_mensuales[i][j]
            if registro is not None:
                promedios[j] += registro.temperatura
                conteos[j] += 1
    return [promedios[j] / conteos[j] if conteos[j] > 0 else None for j in range(24)]

def valores_por_hora_en_dia(dia):
    valores = []
    for j in range(24):
        registro = datos_mensuales[dia-1][j]
        if registro is not None:
            valores.append((j, registro.temperatura, registro.humedad, registro.presion))
    return valores

while True:
    print("\n Menú:")
    print("1. Mostrar para cada variable el día y hora de menor y mayor valor.")
    print("2. Indicar la temperatura promedio mensual por cada hora.")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Mostrar dia y hora:",min_max_por_variable )
    elif opcion == "2":
        print("La temperatura promedio es:",temperatura_promedio_mensual_por_hora )
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente de nuevo")
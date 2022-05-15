import random

def costoSolucion():
    #Entrega el costo total de los pokevacunatios de la solución
    costo_total = 0
    for i in range(len(costo)):
        costo_total += sol[i]*costo[i]
    return costo_total

def estaCubierta(n):
    #Muestra si la comuna está cubierta por un pokevacunatorio
    if cobertura[n] == 1:
        return True
    else:
        return False

def elegirComuna():
    #Busca la siguiente comuna a construir un pokevacunatorio
    comunas_posibles = [] #auxiliar para guardar la posición de las comunas posibles
    costo_ponderado_comunas = [] #auxiliar para guardar la ponderacion de costo de las comunas posibles
    for i in range(len(costo)):
        ab = 1 #auxiliar, cantidad de comunas que puede cubrir actualmente, parte de 1 porque puede cubrirse a sí misma
        if estaCubierta(i):
            continue
        for j in range(len(costo)):
            #se suma la cantidad de comunas que se puede cubrir en el instante actual para la ponderación
            if estaCubierta(j):
                continue
            ab = ab + matriz[i][j]
        a = costo[i]/ab #se divide el costo de la construcción por la cantidad de comunas que se puede cubrir actualmente

        costo_ponderado_comunas.append(a)
        comunas_posibles.append(i)
    # choices elige aleatoriamente una comuna de comunas_posibles dependiendo del peso en weights
    # dado que el menor costo es la mejor comuna, le damos más peso a la menor comuna usando 1/costo
    # un menor costo dará un número más alto, por ende mayor probabilidad de elección al tener menor costo.
    return random.choices(comunas_posibles, weights=[1/x for x in costo_ponderado_comunas], k=1)[0]

def construirPokeVacunatorio(n):
    #Guardar la comuna en la solución y cubrirla
    sol[n] = 1
    cobertura[n] = 1
    for i in range(len(costo)):
        #Buscar las comunas contiguas a la seleccionada y marcarlas como cubiertas
        if matriz[n][i] == 1:
            cobertura[i] = 1
    

def greedy():
    while (sum(cobertura) != len(costo)):
        #mientras no esté todo cubierto, seguir construyendo 
        construirPokeVacunatorio(elegirComuna())

if __name__ == "__main__":
    #los índices van del 0 al 10 indicando las comunas 1 al 11 del problema
    #conectividad de las comunas de acuerdo al problema. 0 esa comuna no está conectada a la comuna de la fila, 1 si lo está
    #ej: fila 0 (comuna 1 del problema) está conectada a las comunas 2,3,4 por lo tanto [0,1,1,1.....]
    matriz = [[0,1,1,1,0,0,0,0,0,0,0],
              [1,0,0,1,0,0,0,0,0,0,0],
              [1,0,0,1,1,1,0,0,0,0,0],
              [1,1,1,0,1,0,0,0,0,0,0],
              [0,0,1,1,0,1,1,1,1,0,0],
              [0,0,1,0,1,0,0,0,1,0,0],
              [0,0,0,0,1,0,0,1,0,1,1],
              [0,0,0,0,1,0,1,0,1,1,0],
              [0,0,0,0,1,1,0,1,0,1,1],
              [0,0,0,0,0,0,1,1,1,0,1],
              [0,0,0,0,0,0,1,0,1,1,0]]

    #costo de construir un pokevacunatorio en la comuna del índice
    costo = [60,30,60,70,130,50,70,60,50,80,40]

    #semillas utilizadas para generar números aleatorios
    semillas = [18064, 7113, 58232, 71014, 66026, 37769, 3298, 49750, 40300,
                55001, 45703, 24510, 9661, 80395, 14510, 95231, 17445, 61022, 36431, 95647]

    for i in range(1):
        random.seed(semillas[i])
        print("Semilla : " + str(semillas[i]))

        sol = [0,0,0,0,0,0,0,0,0,0,0]
        cobertura = [0,0,0,0,0,0,0,0,0,0,0]
    
        greedy()

        print("Solución : " + str(sol))
        print("Costo total : " + str(costoSolucion()))
        print("--------------------")

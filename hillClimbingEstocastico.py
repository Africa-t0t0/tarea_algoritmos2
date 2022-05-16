import random

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

costo = [60,30,60,70,130,50,70,60,50,80,40]

def factible(sol):
    #ver si una solucion es factible, que tenga cobertura total
    cobertura = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(sol)):
        if sum(cobertura) == len(sol): #si es que la cobertura está en todas las comunas, retornar verdadero
            return True
        if sol[i] == 1: #si hay pokevacunatorio en la comuna i
            cobertura[i] = 1 #cubrise a si misma la comuna
            for j in range(len(sol)): #recorrer las comunas contiguas a la comuna seleccionada
                if sum(cobertura) == len(sol):
                    return True
                if matriz[i][j] == 1:
                    cobertura[j] = 1 #rellenar las comunas contiguas
    return False #si es que no hubo solucion factible, retornar falso

def costoSolucion(sol):
    #Entrega el costo total de los pokevacunatios de la solución
    costo_total = 0
    for i in range(len(costo)):
        costo_total += sol[i]*costo[i]
    return costo_total

def calcularVecinos(sol):
    #Entrega una lista de vecinos con el movimiento 1 -> 0
    #Ej: sol: [1,1,1] vecinos: [0,1,1] [1,0,1] [1,1,0]
    vecinos = []
    for i in range(len(sol)):
        aux = sol.copy()
        aux[i] = 0
        if aux == sol:
            #si no se elimina el vecino igual a la solucion del vecindario se puede entrar en un bucle infinito
            continue
        vecinos.append(aux)
    return vecinos

def hillClimbing():
    #solucion inicial
    solucion = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    vecinos = calcularVecinos(solucion) #crear vecinos
    continuar = True
    while (continuar):
        continuar = False
        aux_vecinos = [] #auxiliar de vecinos factibles
        aux_costos = [] #auxiliar de costos de los vecinos factibles
        continuar = False
        for vecino in vecinos:
            if factible(vecino):
                #si el vecino es una solucion factible guardarlo
                aux_vecinos.append(vecino)
                aux_costos.append(costoSolucion(vecino))
                continuar = True
            else:
                continue
        if aux_vecinos: #si es que hay vecinos factibles
            #elegir la nueva solucion al azar de forma ponderada por costo menor mayor probabilidad
            solucion = random.choices(aux_vecinos, weights=[1/x for x in aux_costos], k=1)[0]
            #y crear el nuevo vecindario
            vecinos = calcularVecinos(solucion)
    
    return solucion, costoSolucion(solucion)

if __name__ == "__main__":
    #semillas utilizadas para generar números aleatorios
    semillas = [18064, 7113, 58232, 71014, 66026, 37769, 3298, 49750, 40300,
                55001, 45703, 24510, 9661, 80395, 14510, 95231, 17445, 61022, 36431, 95647]
    
    for i in range(20):
        random.seed(2)
        print("Semilla {}: ".format(i+1) + str(semillas[i]))
        
        a, b = hillClimbing()
        print("Solución: " + str(a))
        print("Costo total : " + str(b))
        print("--------------------")
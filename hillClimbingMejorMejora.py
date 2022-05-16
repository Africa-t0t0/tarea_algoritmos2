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
        vecinos.append(aux)
    return vecinos

def hillClimbing():
    #partir de una solución
    solucion = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    costo_solucion = costoSolucion(solucion)
    vecinos = calcularVecinos(solucion) #crear los vecinos
    continuar = True
    while (continuar):
        continuar = False
        for vecino in vecinos: #buscar mejor vecino
            if factible(vecino): #si no hay factible, se entrega la ultima solucion guardada
                aux = costoSolucion(vecino)
                if aux < costo_solucion:
                    solucion = vecino
                    costo_solucion = aux
                    continuar = True
                else:
                    continue
            else:
                continue
        vecinos = calcularVecinos(solucion) #crear nuevo vecindario con respecto a la nueva solucion
    
    return solucion, costo_solucion

if __name__ == "__main__":
    a, b = hillClimbing()

    print("Solución: " + str(a))
    print("Costo total : " + str(b))
    print("--------------------")

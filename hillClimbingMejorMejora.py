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
    cobertura = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(sol)):
        if sum(cobertura) == len(sol):
            return True
        if sol[i] == 1:
            cobertura[i] = 1
            for j in range(len(sol)):
                if sum(cobertura) == len(sol):
                    return True
                if matriz[i][j] == 1:
                    cobertura[j] = 1
    return False

def costoSolucion(sol):
    #Entrega el costo total de los pokevacunatios de la solución
    costo_total = 0
    for i in range(len(costo)):
        costo_total += sol[i]*costo[i]
    return costo_total

def calcularVecinos(sol):
    vecinos = []
    for i in range(len(sol)):
        aux = sol.copy()
        aux[i] = 0
        vecinos.append(aux)
    return vecinos

def hillClimbing():
    solucion = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    costo_solucion = costoSolucion(solucion)
    vecinos = calcularVecinos(solucion)
    continuar = True
    while (continuar):
        continuar = False
        for vecino in vecinos:
            if factible(vecino):
                aux = costoSolucion(vecino)
                if aux < costo_solucion:
                    solucion = vecino
                    costo_solucion = aux
                    continuar = True
                else:
                    continue
            else:
                continue
        vecinos = calcularVecinos(solucion)
    
    return solucion, costo_solucion

if __name__ == "__main__":
    a, b = hillClimbing()

    print("Solución: " + str(a))
    print("Costo total : " + str(b))
    print("--------------------")

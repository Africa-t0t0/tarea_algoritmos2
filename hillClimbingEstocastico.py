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
        if aux == sol:
            continue
        vecinos.append(aux)
    return vecinos

def hillClimbing():
    solucion = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    vecinos = calcularVecinos(solucion)
    continuar = True
    while (continuar):
        continuar = False
        aux1 = []
        aux2 = []
        continuar = False
        for vecino in vecinos:
            if factible(vecino):
                aux1.append(vecino)
                aux2.append(costoSolucion(vecino))
                continuar = True
            else:
                continue
        if aux1:
            solucion = random.choices(aux1, weights=[1/x for x in aux2], k=1)[0]
            vecinos = calcularVecinos(solucion)
    
    return solucion, costoSolucion(solucion)

if __name__ == "__main__":
    #semillas utilizadas para generar números aleatorios
    semillas = [18064, 7113, 58232, 71014, 66026, 37769, 3298, 49750, 40300,
                55001, 45703, 24510, 9661, 80395, 14510, 95231, 17445, 61022, 36431, 95647]
    
    for i in range(20):
        random.seed(semillas[i])
        print("Semilla : " + str(semillas[i]))
        
        a, b = hillClimbing()
        print("Solución: " + str(a))
        print("Costo total : " + str(b))
        print("--------------------")

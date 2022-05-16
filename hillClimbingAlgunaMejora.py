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

def hillClimbing():
    solucion = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    costo_solucion = costoSolucion(solucion)
    continuar = True
    while (continuar):
        continuar = False
        for i in range(len(solucion)):
            nueva_solucion = solucion.copy()
            nueva_solucion[i] = 0
            if factible(nueva_solucion):
                aux = costoSolucion(nueva_solucion)
                if aux < costo_solucion:
                    solucion = nueva_solucion
                    costo_solucion = aux
                    continuar = True
                else:
                    continue
            else:
                continue
    return solucion, costo_solucion

if __name__ == "__main__":
    a, b = hillClimbing()

    print("Solución: " + str(a))
    print("Costo total : " + str(b))
    print("--------------------")

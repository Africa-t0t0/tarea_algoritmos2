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

def hillClimbing():
    #partir de una solución
    solucion = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    costo_solucion = costoSolucion(solucion)
    continuar = True
    while (continuar):
        continuar = False
        for i in range(len(solucion)):
            #generar un vecino y ver si es mejor
            nueva_solucion = solucion.copy()
            nueva_solucion[i] = 0
            if factible(nueva_solucion): #si no hay factible, se entrega la ultima solucion guardada
                aux = costoSolucion(nueva_solucion)
                if aux < costo_solucion:
                    #si el vecino es mejor, moverse, de lo contrario seguir buscando
                    solucion = nueva_solucion
                    costo_solucion = aux
                    continuar = True
                    break
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

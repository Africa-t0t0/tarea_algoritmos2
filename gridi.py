from random import randrange

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

sol = [0,0,0,0,0,0,0,0,0,0,0]

cobertura = [0,0,0,0,0,0,0,0,0,0,0]

def Pipo(n):
    if cobertura[n] == 1:
        return True
    else:
        return False

def bestoComuna():
    aux = max(costo)
    aux2 = 0
    aux3 = 0
    for i in range(11):
        ab = 0
        if Pipo(i):
            continue
        for j in range(11):
            if Pipo(j):
                continue
            ab = sum(matriz[i])
            if ab > aux3:
                aux3 = ab
        #print("ITERACION " + str(i))
        #print("ab " + str(ab))
        #print("ab elegido "+str(aux3))
        #print("i actual "+str(aux2))
        a = costo[i]/ab
        #print("costo "+str(a))
        if a < aux:
            aux = a
            aux2 = i
        #print("i elegido "+str(aux2))
        #print("costo elegido "+str(aux))
    return aux2

def construirPokeVacunatorio(n):
    for i in range(11):
        if matriz[n][i] == 1:
            cobertura[i] = 1

def cost():
    cost = 0
    for i in range(0, 11):
        if sol[i] == 1:
            cost += costo[i]
    return cost

def gridi():
    seed = randrange(11)
    print(seed)
    sol[seed] = 1
    cobertura[seed] = 1
    construirPokeVacunatorio(seed)
    while (sum(cobertura) != 11):
        a = bestoComuna()
        sol[a] = 1
        construirPokeVacunatorio(a)
        cobertura[a] = 1

        
for i in range(20):
    sol = [0,0,0,0,0,0,0,0,0,0,0]
    cobertura = [0,0,0,0,0,0,0,0,0,0,0]
    
    gridi()
    print(sol)
    print(cost())
    print("--------------------")

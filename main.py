from xmlrpc.client import MAXINT
from igraph import *

matrix =            [[0,1,1,1,0,0,0,0,0,0,0],
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


def is_active(i):
    if active[i] == 1:
        return True
    return False

def best_choice():
    aux = MAXINT
    for i in range(0, len(weights)):
        if is_active(i):
            continue
        if weights[i] < aux:
            aux = i
    active[aux] = 1
    sol[aux] = 1
    # for i in range(0, len(weights)):
    #     if matrix[aux][i] == 1:
    #         active[i] = 1
    marcar(aux)
    return active

def cost():
    cost = 0
    for i in range(0, len(weights)):
        if sol[i] == 1:
            cost += weights[i]
    return cost

def not_ready():
    for i in range(0, len(weights)):
        if active[i] == 0:
            return True
    return False

def marcar(aux):
    for i in range(0, len(weights)):
        if matrix[aux][i] == 1:
            active[i] = 1

active = [0,0,0,0,0,0,0,0,0,0,0]
weights = [60,30,60,70,130,50,70,60,50,80,40]
sol = [0,0,0,0,0,0,0,0,0,0,0]

def greedy(seed):
    active[seed] = 1
    sol[seed] = 1
    marcar(seed)
    while not_ready():
        best_choice()
    return sol, cost()

            
x, y = greedy(0)
print("solution: ", x)
print("cost: ", y)


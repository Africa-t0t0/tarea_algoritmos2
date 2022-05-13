from xmlrpc.client import MAXINT
from igraph import *
visual_style = {}
out_name = "graph.png"

g = Graph.Adjacency([[0,1,1,1,0,0,0,0,0,0,0],
                     [1,0,0,1,0,0,0,0,0,0,0],
                     [1,0,0,1,1,1,0,0,0,0,0],
                     [1,1,1,0,1,0,0,0,0,0,0],
                     [0,0,1,1,0,1,1,1,1,0,0],
                     [0,0,1,0,1,0,0,0,1,0,0],
                     [0,0,0,0,1,0,0,1,0,1,1],
                     [0,0,0,0,1,0,1,0,1,1,0],
                     [0,0,0,0,1,1,0,1,0,1,1],
                     [0,0,0,0,0,0,1,1,1,0,1],
                     [0,0,0,0,0,0,1,0,1,1,0]])

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

for i in range(len(g.vs)):
    g.vs[i]["id"]= i
    g.vs[i]["label"]= str(i)

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
    for i in range(0, len(weights)):
        if matrix[aux][i] == 1:
            active[i] = 1
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

active = [0,0,0,0,0,0,0,0,0,0,0]
weights = [60,30,60,70,130,50,70,60,50,80,40]
sol = [0,0,0,0,0,0,0,0,0,0,0]

def greedy():
    while not_ready():
        sol = best_choice()
    return sol

            
greedy()
print("solution: ", sol)
print("cost: ", cost())


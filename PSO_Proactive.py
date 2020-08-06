import random
import numpy as np
import time


def fitness(normalizedQoE, normalizedCost):
    return weight * normalizedQoE - (1-weight)*normalizedCost


pathvector = []
edgecapacity = []
budget = []
QualityThreshold =[]
unitResourceCost = []
probability = []
sourceDestPathCount = []
Xij = []
pbest = []
gbest_fitness = -1000000
user = 150
EN = 12
Time = 10
particle = 30
iteration = 100
weight = 0.8
wUpper = 0.9
wLower = 0.4
rho = 0.9
c1 = 0.8
c2 = 0.9
accuracy = 0.85
WW = 0.95

pathvector = [[random.randrange(0, 2, 1) for k in range(0, EN)] for j in range(0, user)]
edgecapacity = [5 for j in range(0, EN)]
budget = [random.randrange(100, 120, 1) for j in range(0, user)]
for i in range(user):
    cnt = 0
    for j in range(EN):
        if pathvector[i][j] == 1:
            cnt += 1
    sourceDestPathCount.append(cnt)

Xij = [[[0 for k in range(0, EN)] for j in range(0, user)] for p in range(particle)]
pbest_position = [[[0 for k in range(0, EN)] for j in range(0, user)] for p in range(particle)]
new_position = [[[0 for k in range(0, EN)] for j in range(0, user)] for p in range(particle)]
gbest_position = [[0 for k in range(0, EN)] for j in range(0, user)]
new_velocity = [[0 for k in range(0, EN)] for j in range(0, user)]
pbest_fitness = [-100000 for p in range(particle)]
velocity_vector = [random.uniform(-1, 1) for p in range(particle)]
print(pbest_fitness)
start = time.time()
for ita in range(iteration):
    if ita <= rho * iteration:
        W = wUpper - ((ita + 1) * (wUpper - wLower))/(rho * iteration)
    else:
        W = wLower
    print(W)
    for p in range(particle):
        normalizedQoE = 0
        normalizeCost = 0
       # print("particle " + str(p+1))

        probability = [[round(random.uniform(0, 1), 1) for k in range(0, EN)] for j in range(0, user)]
        countEdgeNodeCap = [0 for k in range(0, EN)]
        unitResourceCost = [[round(random.uniform(1, 2.5), 1) for k in range(0, EN)] for j in range(0, user)]
        QualityThreshold = [budget[j]/120 for j in range(0, user)]
        #print("Path Nodes")
      #  print(pathvector)
      #  print(budget)
       # print(QualityThreshold)
       # print(unitResourceCost)
       # print(sourceDestPathCount)
      #  print(probability)
        for i in range(user):
            userBudget = 0
            pathQuality = 0
            noPathQuality = 0
            for j in range(EN):

                if (pathvector[i][j] == 1) and userBudget <= budget[i] and countEdgeNodeCap[j] < edgecapacity[j]:
                    Xij[p][i][j] = 1
                    pathQuality += Xij[p][i][j]
                    userBudget += unitResourceCost[i][j] * Time
                    countEdgeNodeCap[j] += 1
            for j in range(EN):
                if probability[i][j] > 0.5 and userBudget <= budget[i] and countEdgeNodeCap[j] < edgecapacity[j]:
                    Xij[p][i][j] = 1
                    noPathQuality += Xij[p][i][j]
                    userBudget += unitResourceCost[i][j] * Time
                    countEdgeNodeCap[j] += 1
            Quality = accuracy * pathQuality + (1 - accuracy) * noPathQuality
            normalizedQoE += Quality / sourceDestPathCount[i]
            normalizeCost += userBudget / budget[i]

        fit = fitness(normalizedQoE, normalizeCost)
      #  print(fit)
        if pbest_fitness[p] < fit:
           # print("particle best position nisse " + str(p+1))
          #  print(Xij[p])
            pbest_fitness[p] = fit
            pbest_position[p] = Xij[p]
        if gbest_fitness < fit:
            gbest_fitness = fit
            gbest_position = Xij[p]


        # print(Quality / sourceDestPathCount[i])
       # print(countEdgeNodeCap
    for p in range(particle):
      #  print("After First Fit")
      #  print(Xij[p])
     #   print(pbest_fitness[p])
       # print("Best Position")
      #  print(pbest_position[p])
        ptemp = 0
        gtemp = 0
        for i in range(user):
            for j in range(EN):
                ptemp = (pbest_position[p][i][j] - Xij[p][i][j])
                gtemp = (gbest_position[i][j] - Xij[p][i][j])
                new_velocity[i][j] = (WW * velocity_vector[p]) + (c1 * random.uniform(0, 1) * ptemp) +\
                       (c2 * random.uniform(0, 1) * gtemp)
                sig = 1/(1+np.exp(-new_velocity[i][j]))
        #print("New Position")
             #   print(sig)
                if sig >= random.uniform(0, 1):
                    new_velocity[i][j] = 1
                else:
                    new_velocity[i][j] = 0

        for i in range(user):
            for j in range(EN):
                new_position[p][i][j] = new_velocity[i][j]

        Xij[p] = new_position[p]
       # print(Xij[p])
    print("Iteration " + str(ita))
    print("==================Global Best================================")
    print(gbest_fitness)
  #  print(gbest_position)
print(pathvector)
end = time.time()
print(end - start)





import random
import numpy as np
import time
import math


def fitness(normalizedQoE, normalizedCost):
    return (weight * normalizedQoE) - ((1-weight)*normalizedCost)


sourceDestPathCount = []
Xij = []
pbest = []
gbest_fitness = -1000000
user = 400
EN = 12
cap = 150
Time = 10
particle = 30
iteration = 50
weight = 0.8
wUpper = 0.9
wLower = 0.4
rho = 0.962
c1 = 0.8
c2 = 0.9
accuracy = 0.25
WW = 0.95
resCost = 1.1
path = EN * 0.4
print(path)
pathvector = []
best = 0
falsepathvector = []
for j in range(user):
    pathvector.append([])
    cnt = 0
    for k in range(EN):
        if cnt < path:
            a = random.randrange(0, 2, 1)
            if a == 1:
                cnt += 1
            pathvector[j].append(a)
        else:
            pathvector[j].append(0)
probability = []
mout = []
for p in range(particle):
    probability.append([])
    for j in range(user):
        probability[p].append([])
        for k in range(EN):
            if pathvector[j][k] == 1:
                probability[p][j].append(round(random.uniform(0.65, 1), 2))
            else:
                probability[p][j].append(round(random.uniform(0, .65), 2))

truecnt = path * accuracy
falsecnt = path - int(truecnt)
print(truecnt)
print(falsecnt)
for j in range(user):
    falsepathvector.append([])
    cnt = 0
    for k in range(EN):
        if cnt < int(truecnt):
            if pathvector[j][k] == 1:
                cnt += 1
                falsepathvector[j].append(1)
            else:
                falsepathvector[j].append(0)
        else:

            falsepathvector[j].append(0)

for j in range(user):
    cntpath = 0
    for k in range(EN):
        if cntpath < int(math.ceil(falsecnt)):
            if falsepathvector[j][k] == 0 and probability[0][j][k] > 0.3 and pathvector[j][k] != 1:
                cntpath += 1
                falsepathvector[j][k] = 1
print(pathvector)
print(falsepathvector)
#pathvector = [[random.randrange(0, 2, 1) for k in range(0, EN)] for j in range(0, user)]
budget = [random.randrange(100, 200, 1) for j in range(0, user)]
totalBudget = 0
for i in range(user):
    totalBudget += budget[i]

Xij = [[[0 for k in range(0, EN)] for j in range(0, user)] for p in range(particle)]
pbest_position = [[[0 for k in range(0, EN)] for j in range(0, user)] for p in range(particle)]
new_position = [[[0 for k in range(0, EN)] for j in range(0, user)] for p in range(particle)]
gbest_position = [[0 for k in range(0, EN)] for j in range(0, user)]
new_velocity = [[0 for k in range(0, EN)] for j in range(0, user)]
pbest_fitness = [-100000 for p in range(particle)]
velocity_vector = [random.uniform(-6, 6) for p in range(particle)]
print(pbest_fitness)
normalizedQoE = 0
normalizeCost = 0
# print("particle " + str(p+1))

#probability = [[[round(random.uniform(0, 1), 1) for k in range(0, EN)] for j in range(0, user)] for p in range(particle)]
for p in range(particle):
    for i in range(user):
        cnt = 0
        ncnt = 0
        for j in range(EN):
            if pathvector[i][j] == 1:
                cnt += 1
            if pathvector[i][j] == 0 and probability[p][i][j] > 0.5:
                ncnt += 1
        sourceDestPathCount.append(cnt)
        mout.append(ncnt)
print(mout)
unitResourceCost = [[[round(random.uniform(0.5, 2), 1) for k in range(0, EN)] for j in range(0, user)] for p in range(particle)]
QualityThreshold = [round(budget[j] / 400, 2) for j in range(0, user)]
edgecapacity = [cap for j in range(0, EN)]
print(QualityThreshold)
FF = [[[0 for k in range(0, EN)] for j in range(0, user)] for p in range(particle)]
for p in range(particle):
    countEdgeNodeCap = [0 for k in range(0, EN)]

    for i in range(user):
        userBudget = 0
        pathQuality = 0
        noPathQuality = 0
        #for j in range(EN):
          #  print(pathvector[i][j])
         #   if (pathvector[i][j] == 1) and userBudget <= budget[i] and countEdgeNodeCap[j] < edgecapacity[j]:
          #      Xij[p][i][j] = 1
           #     pathQuality += Xij[p][i][j]
            #    userBudget += unitResourceCost[p][i][j] * Time
             #   countEdgeNodeCap[j] += 1
        for j in range(EN):
            if probability[p][i][j] > 0.5 and userBudget <= budget[i] and countEdgeNodeCap[j] < edgecapacity[j]:
                Xij[p][i][j] = 1
                noPathQuality += Xij[p][i][j]
                userBudget += unitResourceCost[p][i][j] * Time
                countEdgeNodeCap[j] += 1
        Quality = accuracy * pathQuality + (1 - accuracy) * noPathQuality
        normalizedQoE += Quality / (sourceDestPathCount[i] + 1)
        normalizeCost += userBudget / budget[i]
FF = Xij
fit = fitness(normalizedQoE, normalizeCost)
start = time.time()
#PSO Start

for ita in range(iteration):
    if ita <= rho * iteration:
        W = wUpper - ((ita + 1) * (wUpper - wLower))/(rho * iteration)
    else:
        W = wLower
  #  print(W)
    for p in range(particle):
        ptemp = 0
        gtemp = 0
     #   edgecapacity = [10 for j in range(0, EN)]
        countEdgeNodeCap = [0 for k in range(0, EN)]
        for i in range(user):
            userBudget = 0
            for j in range(EN):
                ptemp = (pbest_position[p][i][j] - Xij[p][i][j])
                gtemp = (gbest_position[i][j] - Xij[p][i][j])
                new_velocity[i][j] = (W * velocity_vector[p]) + (c1 * random.uniform(0, 1) * ptemp) +\
                       (c2 * random.uniform(0, 1) * gtemp)
                sig = 1/(1+np.exp(-new_velocity[i][j]))

                if sig >= random.uniform(0, 1) and userBudget <= budget[i] and countEdgeNodeCap[j] <= edgecapacity[j] \
                        and probability[p][i][j] > 0.5:
                    new_velocity[i][j] = 1
                    countEdgeNodeCap[j] += 1
                    userBudget += resCost * Time
                else:
                    new_velocity[i][j] = 0

        for i in range(user):
            for j in range(EN):
                new_position[p][i][j] = new_velocity[i][j]
        Xij[p] = new_position[p]
        normalizeCost = 0
        normalizedQoE = 0
        for i in range(user):
            pathQuality = 0
            noPathQuality = 0
            userBudget = 0
            for j in range(EN):
                if Xij[p][i][j] == 1 and falsepathvector[i][j] == 1:
                    pathQuality += Xij[p][i][j]
                    userBudget += resCost * Time
                elif Xij[p][i][j] == 1 and falsepathvector[i][j] == 0:
                    noPathQuality += Xij[p][i][j] * probability[p][i][j]
                    userBudget += resCost * Time
            Quality = accuracy * (pathQuality / (sourceDestPathCount[i] + 1)) + \
                      (1 - accuracy) * (noPathQuality / (mout[i] + 1))
            normalizedQoE += Quality
            if Quality < QualityThreshold[i]:
              #  print("Dhukse for particle " + str(p+1) + " and " + str(i+1))
               # print(str(Quality) + " " + str(QualityThreshold[i]))
                for j in range(EN):
                    if userBudget <= budget[i] and countEdgeNodeCap[j] <= edgecapacity[j] and probability[p][i][j] > 0.2\
                            and Xij[p][i][j] == 0:
                        Xij[p][i][j] = 1

                    if Xij[p][i][j] == 1 and falsepathvector[i][j] == 1:
                        pathQuality += Xij[p][i][j]
                        userBudget += resCost * Time
                    elif Xij[p][i][j] == 1 and falsepathvector[i][j] == 0:
                        noPathQuality += Xij[p][i][j] * probability[p][i][j]
                        userBudget += resCost * Time
                    Quality = accuracy * (pathQuality / (sourceDestPathCount[i] + 1)) + \
                              (1 - accuracy) * (noPathQuality / (mout[i] + 1))

                    if Quality >= QualityThreshold[i]:
                        break
                normalizedQoE += Quality
            normalizeCost += userBudget / budget[i]
      #  print(p+1)
      #  print(normalizedQoE)
        fit = fitness(normalizedQoE, normalizeCost)
       # print(normalizedQoE)
        if pbest_fitness[p] < fit:
            pbest_fitness[p] = fit
            pbest_position[p] = Xij[p]
       # print(pbest_fitness)
        if gbest_fitness < fit:
            gbest_fitness = fit
            gbest_position = Xij[p]
            best = p

    print("Iteration " + str(ita))
    print("==================Global Best================================")
    print(gbest_fitness)
print("=================QoE===================")
print(normalizedQoE/user)
print(gbest_position)
print(pathvector)
print(budget)
print(unitResourceCost)
end = time.time()
print(end - start)
maxi = -1
normalizeCost = 0
normalizedQoE = 0
userBudget = 0
reactive = 0
reactiveTotalCnt = 0
normalizeCostFF = 0
normalizedQoEFF = 0
userBudgetFF = 0
reactiveFF = 0
reactiveTotalCntFF = 0
finalQuality = []
for i in range(user):
    pathQuality = 0
    noPathQuality = 0
    pathQualityFF = 0
    noPathQualityFF = 0

    for j in range(EN):
        if Xij[best][i][j] == 1 and pathvector[i][j] == 1:
            pathQuality += 1
            userBudget += resCost * Time
        if Xij[best][i][j] == 1 and pathvector[i][j] == 0:
            noPathQuality += (1 * probability[best][i][j])
            userBudget += resCost * Time
        if Xij[best][i][j] == 0 and (pathvector[i][j] == 1 or probability[best][i][j] >= 0.5):
            reactive += 1
        if pathvector[i][j] == 1 or probability[best][i][j] >= 0.3:
            reactiveTotalCnt += 1

    Quality = accuracy * (pathQuality / (sourceDestPathCount[i]+1)) + (1 - accuracy) * (noPathQuality / (mout[i]+1))
    finalQuality.append(round(Quality, 2))
    print()
    print("User " + str(i) + " Quality " + str(Quality))
    if Quality > maxi:
        maxi = Quality
    normalizedQoE += Quality
print("Qoe " + str(normalizedQoE/user))
print("Cost " + str(userBudget/user))
print(maxi)
print(reactive)
print(reactiveTotalCnt)
print("Reactive Migration Probability")
print(reactive/reactiveTotalCnt * 100)
print(QualityThreshold)
print(finalQuality)
cntQuality = 0
for i in range(user):
    if QualityThreshold[i] > finalQuality[i]:
        cntQuality += 1
print(cntQuality)
print(totalBudget)



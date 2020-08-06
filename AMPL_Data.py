import random
import numpy as np
import math


def printing(arr):
    for i in range(EN):
        file.write(str(i + 1) + " ")
    file.write(":=\n")
    for i in range(user):
        file.write(str(i + 1) + " ")
        for j in range(EN):
            file.write(str(arr[i][j]) + " ")
        if i == user - 1:
            file.write(";")
        file.write("\n")


def printing1d(arr):
    for i in range(user):
        file.write(str(i + 1) + " ")
        file.write(str(arr[i]))
        if i == user - 1:
            file.write(";")
        file.write("\n")


pathvector = []
file = open("ampldata.txt", "w")
user = 500
EN = 30
path = math.ceil(EN * 0.4)
alpha = 0.2
file.write("param edgeNode:= " + str(EN) + ";\n")
file.write("param user:= " + str(user) + ";\n")
file.write("param alpha := " + str(alpha) + ";\n")
file.write("param time := 10; \n param Hmin := 0.2;\n\n")
users = []
for j in range(user):
    users.append(j+1)
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
print(pathvector)
print(np.transpose(pathvector))
print(users)

file.write("param pathnode: ")
printing(pathvector)
file.write("\n")
probability = []
mout = []
for j in range(user):
    probability.append([])
    for k in range(EN):
        if pathvector[j][k] == 1:
            probability[j].append(round(random.uniform(0.65, 1), 2))
        else:
            probability[j].append(round(random.uniform(0, .65), 2))
file.write("param probability: ")
printing(probability)
file.write("\n")
unitResourceCost = [[round(random.uniform(0.5, 2), 1) for k in range(0, EN)] for j in range(0, user)]
file.write("param resourcecost: ")
printing(unitResourceCost)
file.write("\n")
budget = [random.randrange(100, 300, 1) for j in range(0, user)]
file.write("param budget:= ")
printing1d(budget)
file.write("\n")
sourceDestPathCount = []
for i in range(user):
    cnt = 0
    ncnt = 0
    for j in range(EN):
        if pathvector[i][j] == 1:
            cnt += 1
    sourceDestPathCount.append(cnt)
file.write("param pathnodeNumber:= ")
printing1d(sourceDestPathCount)
Qmin = [round(budget[j]/1500, 2) for j in range(0, user)]
file.write("param Qmax:= ")
printing1d(Qmin)
file.write("\n")
capacity = [150 for j in range(0, EN)]
file.write("param edgeCapacity:= ")
for j in range(EN):
    file.write(str(j + 1) + " ")
    file.write(str(capacity[j]))
    if j == EN - 1:
        file.write(";")
    file.write("\n")
file.close()
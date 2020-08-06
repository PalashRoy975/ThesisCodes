import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt1
user = []
QoEDAMP = []
QoEAP1 = []
QoEAP2 = []
SatDAMP = []
SatAP1 = []
SatAP2 = []
with open('FileMobility.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        user.append(int(row[0]))
        QoEDAMP.append(float(row[1]))
        QoEAP1.append(float(row[5]))
        QoEAP2.append(float(row[9]))
        SatDAMP.append(float(row[4]))
        SatAP1.append(float(row[8]))
        SatAP2.append(float(row[12]))
print(QoEDAMP)
print(user)
ind = np.arange(5)
fig, ax = plt.subplots()
ax.bar(ind, QoEDAMP, color='b', width=0.25, yerr=0.02, label="DPPM")
ax.bar(ind + 0.25, QoEAP1, color='g', width=0.25, yerr=0.04, label="AP1")
ax.bar(ind + 0.5, QoEAP2, color='r', width=0.25, yerr=0.045, label="AP2")
plt.xticks(ind + 0.3, user)
plt.xlabel("Number of Users")
plt.ylabel("Quality of Experience (QoE)")
plt.legend()
plt.savefig("Mobility_User_Qoe.pdf")
plt.show()


fig1, ax = plt1.subplots()
ax.bar(ind, SatDAMP, color='b', width=0.25, yerr=0.02, label="DPPM")
ax.bar(ind + 0.25, SatAP1, color='g', width=0.25, yerr=0.04, label="AP1")
ax.bar(ind + 0.5, SatAP2, color='r', width=0.25, yerr=0.045, label="AP2")
plt1.xticks(ind + 0.3, user)
plt1.xlabel("Number of Users")
plt1.ylabel("User Satisfaction")
plt1.legend()
plt1.savefig("Mobilty_User_Sat.pdf")
plt1.show()

import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
user = []
alpha0 = []
alpha2 = []
alpha4 = []
alpha6 = []
alpha8 = []
alpha1 = []
acc25 = []
acc50 = []
acc65 = []
acc80 = []
acc95 = []
VNF = []
BS10 = []
BS15 = []
BS20 = []
BS25 = []
BS30 = []


with open('POPP_NP_Graph_Data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        VNF.append(int(row[1]))
        BS10.append(float(row[2]))
        BS15.append(float(row[3]))
        BS20.append(float(row[4]))
        BS25.append(float(row[5]))
        BS30.append(float(row[6]))
plt2.errorbar(VNF, BS10, color='green', label='10 Edge Nodes', yerr=0.0,  marker='+')
plt2.errorbar(VNF, BS15, color='red', label='15 Edge Nodes', yerr=0.0, marker='o')
plt2.errorbar(VNF, BS20, color='blue', label='20 Edge Nodes', yerr=0.0, marker='^')
plt2.errorbar(VNF, BS25, color='k', label='25 Edge Nodes', yerr=0.0, marker='v')
plt2.errorbar(VNF, BS30, color='y', label='30 Edge Nodes', yerr=0.0, marker='s')
plt2.xlim(28, 352)
plt2.ylim(-0.01, 4001)
plt2.xlabel('Number of users', fontsize=14)
plt2.xticks(np.arange(30, 351, step=40))
plt2.ylabel('Running Time (ms)', fontsize=14)
plt2.yticks(np.arange(0, 4001, step=500))
plt2.legend()
plt2.savefig("NP_hard_graph.pdf")
plt2.show()

with open('alpha.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        user.append(int(row[6]))
        alpha0.append(float(row[7]))
        alpha2.append(float(row[8]))
        alpha4.append(float(row[9]))
        alpha6.append(float(row[10]))
        alpha8.append(float(row[11]))
        alpha1.append(float(row[12]))
        acc25.append((float(row[15])))
        acc50.append((float(row[16])))
        acc65.append((float(row[17])))
        acc80.append((float(row[18])))
        acc95.append((float(row[19])))

plt.errorbar(user, alpha0, color='green', label=r'$\alpha $ = 0', yerr=0.025,  marker='+')
plt.errorbar(user, alpha2, color='red', label=r'$\alpha $ = 0.2', yerr=0.025, marker='o')
plt.errorbar(user, alpha4, color='blue', label=r'$\alpha $ = 0.4', yerr=0.025, marker='^')
plt.errorbar(user, alpha6, color='k', label=r'$\alpha $ = 0.6', yerr=0.025, marker='v')
plt.errorbar(user, alpha8, color='y', label=r'$\alpha $ = 0.8', yerr=0.025, marker='s')
plt.errorbar(user, alpha1, color='m', label=r'$\alpha $ = 1', yerr=0.025, marker='x')
plt.xlim(98, 502)
plt.ylim(.28, 1.02)
plt.xlabel('Number of users', fontsize=14)
plt.xticks(np.arange(100, 501, step=100))
plt.ylabel('Quality-of-Experience (QoE)', fontsize=14)
plt.yticks(np.arange(0.3, 1.02, step=0.1))
plt.legend()
plt.savefig("User_vs_QoE_varying_alpha.pdf")
plt.show()

plt1.errorbar(user, acc25, color='green', label=r'$\psi $ = 0.25', yerr=0.035, marker='+')
plt1.errorbar(user, acc50, color='red', label=r'$\psi $ = 0.5', yerr=0.035, marker='o')
plt1.errorbar(user, acc65, color='blue', label=r'$\psi $ = 0.65', yerr=0.035, marker='^')
plt1.errorbar(user, acc80, color='k', label=r'$\psi $ = 0.8', yerr=0.035, marker='v')
plt1.errorbar(user, acc95, color='y', label=r'$\psi $ = 0.95', yerr=0.035, marker='s')
plt1.xlim(98, 502)
plt1.ylim(.28, 1.02)
plt1.xlabel('Number of users', fontsize=14)
plt1.xticks(np.arange(100, 501, step=100))
plt1.ylabel('Quality-of-Experience (QoE)', fontsize=14)
plt1.yticks(np.arange(0.3, 1.02, step=0.1))
plt1.legend()
plt1.savefig("User_vs_QoE_varying_accuracy.pdf")
plt1.show()

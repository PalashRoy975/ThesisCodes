import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import matplotlib.pyplot as plt5
import matplotlib.pyplot as plt6
import matplotlib.pyplot as plt7
import matplotlib.pyplot as plt8
import matplotlib.pyplot as plt9
import matplotlib.pyplot as plt10
import matplotlib.pyplot as plt11
import numpy as np

user = []
QoePOPP = []
costPOPP = []
probPOPP = []
satPOPP = []
QoeRM = []
costRM = []
probRM = []
satRM = []
QoeNSR = []
costNSR = []
probNSR = []
satNSR = []
EN = []
Cap = []
ENQoePOPP = []
ENCsotPOPP = []
ENProbPOPP = []
ENQoeRM = []
ENCsotRM = []
ENProbRM = []
ENQoeNSR = []
ENCsotNSR = []
ENProbNSR = []
ENSatPOPP = []
ENSatRM = []
ENSatNSR = []
CapQoePOPP = []
CapCsotPOPP = []
CapProbPOPP = []
CapQoeRM = []
CapCsotRM = []
CapProbRM = []
CapQoeNSR= []
CapCsotNSR = []
CapProbNSR = []
CapSatPOPP = []
CapSatRM = []
CapSatNSR = []
with open('file.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        user.append(int(row[2]))
        QoePOPP.append(float(row[4]))
        QoeRM.append(float(row[5]))
        QoeNSR.append(float(row[6]))
        costPOPP.append(float(row[18]))
        costNSR.append(float(row[16]))
        costRM.append(float(row[17]))
        probPOPP.append(float(row[13]))
        probRM.append(float(row[11]))
        probNSR.append(float(row[14]))
        satPOPP.append(float(row[19]))
        satRM.append(float(row[20]))
        satNSR.append(float(row[21]))


with open('fileEN.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        EN.append(int(row[0]))
        ENQoePOPP.append(float(row[3]))
        ENCsotPOPP.append((float(row[16])))
        ENProbPOPP.append((float(row[6])))
        ENQoeRM.append(float(row[7]))
        ENCsotRM.append((float(row[15])))
        ENProbRM.append((float(row[10])))
        ENQoeNSR.append(float(row[11]))
        ENCsotNSR.append((float(row[14])))
        ENProbNSR.append((float(row[13])))
        ENSatPOPP.append(float(row[17]))
        ENSatRM.append(float(row[18]))
        ENSatNSR.append(float(row[19]))

with open('fileCAP.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        Cap.append(int(row[0]))
        CapQoePOPP.append(float(row[1]))
        CapCsotPOPP.append((float(row[13])))
        CapProbPOPP.append((float(row[7])))
        CapSatPOPP.append(float(row[14]))
        CapQoeRM.append(float(row[5]))
        CapCsotRM.append((float(row[12])))
        CapProbRM.append((float(row[4])))
        CapSatRM.append(float(row[15]))
        CapQoeNSR.append(float(row[8]))
        CapCsotNSR.append((float(row[11])))
        CapProbNSR.append((float(row[10])))
        CapSatNSR.append(float(row[16]))


def user_graph():
    plt.errorbar(user, QoePOPP, color='green', yerr=0.025, label='POPP', marker='+')
    plt.errorbar(user, QoeRM, color='red', label='Min-RM', yerr=0.03, marker='o')
    plt.errorbar(user, QoeNSR, color='blue', label='Min-NSR', yerr=0.05, marker='^')
    plt.xlim(98, 502)
    plt.ylim(-.05, 1.05)
    plt.xlabel('Number of users', fontsize=14)
    plt.xticks(np.arange(100, 501, step=100))
    plt.ylabel('Quality-of-Experience (QoE) ', fontsize=14)
    plt.yticks(np.arange(0, 1.1, step=0.2))
    plt.legend()
    plt.savefig("User_vs_QoE.pdf")
    plt.show()


    plt1.errorbar(user, costPOPP, color='green', label='POPP', yerr=0.03, marker='+')
    plt1.errorbar(user, costRM, color='red', label='Min-RM', yerr=0.05, marker='o')
    plt1.errorbar(user, costNSR, color='blue', label='Min-NSR', yerr=0.03, marker='^')
    plt1.xlim(98, 502)
    plt1.ylim(0.18, 0.82)
    plt1.xlabel('Number of users', fontsize=14)
    plt1.xticks(np.arange(100, 501, step=100))
    plt1.ylabel('Normalized Deployment Cost ', fontsize=14)
    plt1.yticks(np.arange(0.2, 0.82, step=0.1))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt1.legend()
    plt1.savefig("User_vs_cost.pdf")
    plt1.show()

    plt2.errorbar(user, probPOPP, color='green', label='POPP', yerr=0.03, marker='+')
    plt2.errorbar(user, probRM, color='red', label='Min-RM', yerr=0.03, marker='o')
    plt2.errorbar(user, probNSR, color='blue', label='Min-NSR', yerr=0.05, marker='^')
    plt2.xlim(98, 502)
    plt2.ylim(-0.02, 0.72)
    plt2.xlabel('Number of users', fontsize=14)
    plt2.xticks(np.arange(100, 501, step=100))
    plt2.ylabel('Reactive Migration Probability ', fontsize=14)
    plt2.yticks(np.arange(0, 0.72, step=0.1))
    plt2.legend()
    plt2.savefig("User_vs_ReactProb.pdf")
    plt2.show()

    plt10.errorbar(user, satPOPP, color='green', label='POPP', yerr=0.025, marker='+')
    plt10.errorbar(user, satRM, color='red', label='Min-RM', yerr=0.05, marker='o')
    plt10.errorbar(user, satNSR, color='blue', label='Min-NSR', yerr=0.05, marker='^')
    plt10.xlim(98, 502)
    plt10.ylim(0.18, .92)
    plt10.xlabel('Number of Users', fontsize=14)
    plt10.xticks(np.arange(100, 501, step=100))
    plt10.ylabel('User Satisfaction ', fontsize=14)
    plt10.yticks(np.arange(0.2, 0.92, step=0.1))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt10.legend()
    plt10.savefig("user_sat.pdf")
    plt10.show()



def Cap_graph():
    plt6.errorbar(Cap, CapQoePOPP, color='green', label='POPP', yerr=0.02, marker='+')
    plt6.errorbar(Cap, CapQoeRM, color='red', label='Min-RM', yerr=0.025, marker='o')
    plt6.errorbar(Cap, CapQoeNSR, color='blue', label='Min-NSR', yerr=0.04,marker='^')
    plt6.xlim(48, 252)
    plt6.ylim(-.05, 1.05)
    plt6.xlabel('Capacity of EN', fontsize=14)
    plt6.xticks(np.arange(50, 251, step=40))
    plt6.ylabel('Quality-of-Experience (QoE)', fontsize=14)
    plt6.yticks(np.arange(0, 1.1, step=0.2))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt6.legend()
    plt6.savefig("Cap_Qoe.pdf")
    plt6.show()


    plt7.errorbar(Cap, CapCsotPOPP, color='green', label='POPP', yerr=0.02, marker='+')
    plt7.errorbar(Cap, CapCsotRM, color='red', label='Min-RM', yerr=0.02, marker='o')
    plt7.errorbar(Cap, CapCsotNSR, color='blue', label='Min-NSR', yerr=0.04, marker='^')
    plt7.xlim(48, 252)
    plt7.ylim(-.02, 0.52)
    plt7.xlabel('Capacity of EN', fontsize=14)
    plt7.xticks(np.arange(50, 251, step=40))
    plt7.ylabel('Normalized Deployment Cost', fontsize=14)
    plt7.yticks(np.arange(0, 0.51, step=0.1))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt7.legend()
    plt7.savefig("Cap_Cost.pdf")
    plt7.show()

    plt8.errorbar(Cap, CapProbPOPP, color='green', label='POPP', yerr=0.02, marker='+')
    plt8.errorbar(Cap, CapProbRM, color='red', label='Min-RM', yerr=0.02, marker='o')
    plt8.errorbar(Cap, CapProbNSR, color='blue', label='Min-NSR', yerr=0.038, marker='^')
    plt8.xlim(48, 252)
    plt8.ylim(.03, 0.57)
    plt8.xlabel('Capacity of EN', fontsize=14)
    plt8.xticks(np.arange(50, 251, step=40))
    plt8.ylabel('Reactive Migration Probability', fontsize=14)
    plt8.yticks(np.arange(0.05, 0.56, step=0.1))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt8.legend()
    plt8.savefig("Cap_prob.pdf")
    plt8.show()

    plt11.errorbar(Cap, CapSatPOPP, color='green', label='POPP', yerr=0.02, marker='+')
    plt11.errorbar(Cap, CapSatRM, color='red', label='Min-RM', yerr=0.035, marker='o')
    plt11.errorbar(Cap, CapSatNSR, color='blue', label='Min-NSR', yerr=0.035, marker='^')
    plt11.xlim(48, 252)
    plt11.ylim(0.38, 0.92)
    plt11.xlabel('Capacity of EN', fontsize=14)
    plt11.xticks(np.arange(50, 251, step=40))
    plt11.ylabel('User Satisfaction ', fontsize=14)
    plt11.yticks(np.arange(0.4, 0.91, step=0.1))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt11.legend()
    plt11.savefig("Cap_sat.pdf")
    plt11.show()

def EN_graph():
    plt3.errorbar(EN, ENQoePOPP, color='green', label='POPP', yerr=0.025, marker='+')
    plt3.errorbar(EN, ENQoeRM, color='red', label='Min-RM', yerr=0.025, marker='o')
    plt3.errorbar(EN, ENQoeNSR, color='blue', label='Min-NSR', yerr=0.045, marker='^')
    plt3.xlim(3, 25)
    plt3.ylim(-.05, 1.05)
    plt3.xlabel('Number of ENs', fontsize=14)
    plt3.xticks(np.arange(4, 25, step=4))
    plt3.ylabel('Quality-of-Experience (QoE) ', fontsize=14)
    plt3.yticks(np.arange(0, 1.1, step=0.2))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt3.legend()
    plt3.savefig("EN_Qoe.pdf")
    plt3.show()

    plt9.errorbar(EN, ENSatPOPP, color='green', label='POPP', yerr=0.02, marker='+')
    plt9.errorbar(EN, ENSatRM, color='red', label='Min-RM', yerr=0.045, marker='o')
    plt9.errorbar(EN, ENSatNSR, color='blue', label='Min-NSR', yerr=0.045, marker='^')
    plt9.xlim(3, 25)
    plt9.ylim(0.28, .92)
    plt9.xlabel('Number of ENs', fontsize=14)
    plt9.xticks(np.arange(4, 25, step=4))
    plt9.ylabel('User Satisfaction ', fontsize=14)
    plt9.yticks(np.arange(0.3, .92, step=0.1))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt9.legend()
    plt9.savefig("EN_Sat.pdf")
    plt9.show()


    plt4.errorbar(EN, ENProbPOPP, color='green', label='POPP', yerr=0.025, marker='+')
    plt4.errorbar(EN, ENProbRM, color='red', label='Min-RM', yerr=0.025, marker='o')
    plt4.errorbar(EN, ENProbNSR, color='blue', label='Min-NSR', yerr=0.04, marker='^')
    plt4.xlim(3, 25)
    plt4.ylim(0.04, 0.56)
    plt4.xlabel('Number of ENs', fontsize=14)
    plt4.xticks(np.arange(4, 25, step=4))
    plt4.ylabel('Reactive Migration Probability ', fontsize=14)
    plt4.yticks(np.arange(0.05, 0.56, step=0.1))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt4.legend()
    plt4.savefig("EN_prob.pdf")
    plt4.show()

    plt5.errorbar(EN, ENCsotPOPP, color='green', label='POPP', yerr=0.025, marker='+')
    plt5.errorbar(EN, ENCsotRM, color='red', label='Min-RM', yerr=0.04, marker='o')
    plt5.errorbar(EN, ENCsotNSR, color='blue', label='Min-NSR', yerr=0.025, marker='^')
    plt5.xlim(3, 25)
    plt5.ylim(0.08, 0.82)
    plt5.xlabel('Number of ENs', fontsize=14)
    plt5.xticks(np.arange(4, 25, step=4))
    plt5.ylabel('Normalized Deployment Cost', fontsize=14)
    plt5.yticks(np.arange(0.1, 0.81, step=0.1))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt5.legend()
    plt5.savefig("EN_Cost.pdf")
    plt5.show()

Cap_graph()
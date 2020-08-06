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

buyer = []
user = []
RatioTIM = []
RatioDTAM = []
RatioProposed = []
QoeTIM = []
QoEDTAM = []
QoeProposed = []
UtilityTIM = []
UtilityDTAM = []
UtilityProposed = []
PaymentTIM = []
PaymentDTAM = []
PaymentProposed = []
worker = []
RatioTIMWorker = []
RatioDTAMWorker = []
RatioProposedWorker = []
QoeTIMWorker = []
QoEDTAMWorker = []
QoeProposedWorker = []
UtilityTIMWorker = []
UtilityDTAMWorker = []
UtilityProposedWorker = []
PaymentTIMWorker = []
PaymentDTAMWorker = []
PaymentProposedWorker = []
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
with open('MS_Thesis_Increasing_buyer.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        buyer.append(int(row[0]))
        RatioTIM.append(float(row[4]))
        RatioDTAM.append(float(row[6]))
        RatioProposed.append(float(row[2]))
        QoeTIM.append(float(row[8]))
        QoEDTAM.append(float(row[9]))
        QoeProposed.append(float(row[7]))
        UtilityTIM.append(float(row[12]))
        UtilityDTAM.append(float(row[11]))
        UtilityProposed.append(float(row[10]))
        PaymentTIM.append(float(row[15]))
        PaymentDTAM.append(float(row[14]))
        PaymentProposed.append(float(row[13]))


with open('MS_increasing_worker.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        worker.append(int(row[0]))
        RatioProposedWorker.append(float(row[2]))
        RatioTIMWorker.append((float(row[6])))
        RatioDTAMWorker.append((float(row[4])))
        QoeTIMWorker.append(float(row[9]))
        QoeProposedWorker.append((float(row[7])))
        QoEDTAMWorker.append((float(row[8])))
        UtilityTIMWorker.append(float(row[12]))
        UtilityDTAMWorker.append((float(row[11])))
        UtilityProposedWorker.append((float(row[10])))
        PaymentTIMWorker.append(float(row[15]))
        PaymentDTAMWorker.append(float(row[14]))
        PaymentProposedWorker.append(float(row[13]))

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
    plt.errorbar(buyer, RatioTIM, color='green', yerr=4, label='TIM', marker='+')
    plt.errorbar(buyer, RatioDTAM, color='red', label='DTAM', yerr=2, marker='o')
    plt.errorbar(buyer, RatioProposed, color='blue', label='FEST', yerr=2, marker='^')
    plt.xlim(9, 61)
    plt.ylim(39, 101)
    plt.xlabel('Number of buyers', fontsize=14)
    plt.xticks(np.arange(10, 61, step=10))
    plt.ylabel('Task Completion Ratio (%)', fontsize=14)
    plt.yticks(np.arange(40, 101, step=10))
    plt.legend()
    plt.savefig("buyer_Ratio.pdf")
    plt.show()

    plt1.errorbar(buyer, QoeTIM, color='green', label='TIM', yerr=0.06, marker='+')
    plt1.errorbar(buyer, QoEDTAM, color='red', label='DTAM', yerr=0.06, marker='o')
    plt1.errorbar(buyer, QoeProposed, color='blue', label='FEST', yerr=0.03, marker='^')
    plt1.xlim(9, 61)
    plt1.ylim(0, 0.81)
    plt1.xlabel('Number of buyers', fontsize=14)
    plt1.xticks(np.arange(10, 61, step=10))
    plt1.ylabel('Average QoE', fontsize=14)
    plt1.yticks(np.arange(0, 0.82, step=0.1))
    plt1.legend()
    plt1.savefig("Buyer_QoE.pdf")
    plt1.show()

    plt2.errorbar(buyer, UtilityTIM, color='green', label='TIM', yerr=0.05, marker='+')
    plt2.errorbar(buyer, UtilityDTAM, color='red', label='DTAM', yerr=0.05, marker='o')
    plt2.errorbar(buyer, UtilityProposed, color='blue', label='FEST', yerr=0.03, marker='^')
    plt2.xlim(9, 61)
    plt2.ylim(0.19, 0.62)
    plt2.xlabel('Number of buyers', fontsize=14)
    plt2.xticks(np.arange(10, 61, step=10))
    plt2.ylabel('Average utility of buyers', fontsize=14)
    plt2.yticks(np.arange(0.2, 0.61, step=0.05))
    plt2.legend()
    plt2.savefig("buyer_vs_Utility.pdf")
    plt2.show()

    plt10.errorbar(buyer, PaymentTIM, color='green', label='TIM', yerr=4, marker='+')
    plt10.errorbar(buyer, PaymentDTAM, color='red', label='DTAM', yerr=4, marker='o')
    plt10.errorbar(buyer, PaymentProposed, color='blue', label='FEST', yerr=2, marker='^')
    plt10.xlim(9, 61)
    plt10.ylim(14, 41)
    plt10.xlabel('Number of buyers', fontsize=14)
    plt10.xticks(np.arange(10, 61, step=10))
    plt10.ylabel('Average payment of workers (unit) ', fontsize=14)
    plt10.yticks(np.arange(15, 41, step=5))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt10.legend()
    plt10.savefig("buyer_payment.pdf")
    plt10.show()


def worker_graph():
    plt6.errorbar(worker, RatioTIMWorker, color='red', label='DTAM', yerr=4, marker='+')
    plt6.errorbar(worker, RatioDTAMWorker, color='green', label='TIM', yerr=2, marker='o')
    plt6.errorbar(worker, RatioProposedWorker, color='blue', label='FEST', yerr=2, marker='^')
    plt6.xlim(9, 61)
    plt6.ylim(19, 101)
    plt6.xlabel('Number of workers', fontsize=14)
    plt6.xticks(np.arange(10, 61, step=10))
    plt6.ylabel('Task Completion Ratio (%)', fontsize=14)
    plt6.yticks(np.arange(20, 101, step=10))
    plt6.legend()
    plt6.savefig("Worker_Ratio.pdf")
    plt6.show()


    plt7.errorbar(worker, QoeTIMWorker, color='green', label='TIM', yerr=0.045, marker='+')
    plt7.errorbar(worker, QoEDTAMWorker, color='red', label='DTAM', yerr=0.045, marker='o')
    plt7.errorbar(worker, QoeProposedWorker, color='blue', label='FEST', yerr=0.03, marker='^')
    plt7.xlim(9, 61)
    plt7.ylim(0.19, 0.61)
    plt7.xlabel('Number of workers', fontsize=14)
    plt7.xticks(np.arange(10, 61, step=10))
    plt7.ylabel('Average QoE ', fontsize=14)
    plt7.yticks(np.arange(0.2, 0.61, step=0.05))
    plt7.legend()
    plt7.savefig("worker_QoE.pdf")
    plt7.show()

    plt8.errorbar(worker, UtilityTIMWorker, color='green', label='TIM', yerr=0.045, marker='+')
    plt8.errorbar(worker, UtilityDTAMWorker, color='red', label='DTAM', yerr=0.045, marker='o')
    plt8.errorbar(worker, UtilityProposedWorker, color='blue', label='FEST', yerr=0.03, marker='^')
    plt8.xlim(9, 61)
    plt8.ylim(.19, 0.56)
    plt8.xlabel('Number of workers', fontsize=14)
    plt8.xticks(np.arange(10, 61, step=10))
    plt8.ylabel('Average Utility of buyers', fontsize=14)
    plt8.yticks(np.arange(0.20, 0.56, step=0.05))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt8.legend()
    plt8.savefig("Worker_utility.pdf")
    plt8.show()

    plt11.errorbar(worker, PaymentTIMWorker, color='green', label='TIM', yerr=4, marker='+')
    plt11.errorbar(worker, PaymentDTAMWorker, color='red', label='DTAM', yerr=4, marker='o')
    plt11.errorbar(worker, PaymentProposedWorker, color='blue', label='FEST', yerr=2, marker='^')
    plt11.xlim(9, 61)
    plt11.ylim(14, 46)
    plt11.xlabel('Number of workers', fontsize=14)
    plt11.xticks(np.arange(10, 61, step=10))
    plt11.ylabel('Average payment of workers (unit) ', fontsize=14)
    plt11.yticks(np.arange(15, 46, step=5))
    #plt.title('Graph Density Vs Execution Time Graph')
    plt11.legend()
    plt11.savefig("worker_payment.pdf")
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


buyer_pair =[]
Ask = []
priceAsk = []
bidAsk = []
for i in range(18):
    buyer_pair.append(i+1)
print(buyer_pair)
with open('output.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        #buyer.append(int(row[0]))
        priceAsk.append(float(row[4]))
        Ask.append(float(row[2]))
        bidAsk.append(float(row[5]))
print(Ask)
print(priceAsk)
print(bidAsk)
bars = np.add(Ask, priceAsk).tolist()

width = 0.4       # the width of the bars: can also be len(x) sequence
sumprice = priceAsk + bidAsk
fig, ax = plt.subplots()
ind = np.arange(15)
p1 = ax.bar(ind+1, Ask, width, color='darkblue', label='Minimum cost of workers')
p2 = ax.bar(ind+1, priceAsk, width, color='dodgerblue', bottom=Ask, label='Winning price/payment')
p3 = ax.bar(ind+1, bidAsk, width, color='lightskyblue', bottom=bars, label='Bid submitted by buyer')

ax.set_xlabel('Winning buyer-worker pairs')
#ax.set_title('Scores by group and gender')
ax.legend()
plt.xticks(ind + 1, buyer_pair)
plt.yticks(np.arange(0, 11, step=2))
plt5.savefig("Rationality.pdf")
plt.show()


def utility_graph():
    bid = []
    utility = []
    lossUtility = []
    workerUtility = []
    workerlossUtility = []
    with open('truthfulnessData.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            bid.append(float(row[0]))
            utility.append(float(row[1]))
            lossUtility.append(float(row[2]))
            workerUtility.append(float(row[3]))
            workerlossUtility.append(float(row[4]))
    plt2.errorbar(bid, utility, color='darkblue', yerr=0.0, marker='o')
    plt2.xlim(2.9, 10.1)
    plt2.ylim(-0.05, 0.51)
    plt2.xlabel('Submitted bid', fontsize=14)
    plt2.xticks(np.arange(3, 10.5, step=1))
    plt2.ylabel('Utility of buyer', fontsize=14)
    plt2.yticks(np.arange(0, 0.51, step=0.05))
    #plt2.legend()
    plt2.savefig("buyer_vs_Utility_truthful.pdf")
    plt2.show()

    plt3.errorbar(bid, lossUtility, color='darkblue', yerr=0.0, marker='o')
    plt3.xlim(2.9, 10.1)
    plt3.ylim(-0.71, 0.06)
    plt3.xlabel('Submitted bid', fontsize=14)
    plt3.xticks(np.arange(3, 10.5, step=1))
    plt3.ylabel('Utility of buyer', fontsize=14)
    plt3.yticks(np.arange(-0.7, 0.06, step=0.1))
    #pl32.legend()
    plt3.savefig("buyer_vs_Utility_truthful_loss.pdf")
    plt3.show()

    plt4.errorbar(bid, workerUtility, color='darkblue', yerr=0.0, marker='o')
    plt4.xlim(2.9, 10.1)
    plt4.ylim(-0.02, 0.31)
    plt4.xlabel('Worker Ask', fontsize=14)
    plt4.xticks(np.arange(3, 10.5, step=1))
    plt4.ylabel('Utility of worker', fontsize=14)
    plt4.yticks(np.arange(0, 0.31, step=0.05))
    #pl32.legend()
    plt4.savefig("worker_vs_Utility_truthful.pdf")
    plt4.show()

    plt5.errorbar(bid, workerlossUtility, color='darkblue', yerr=0.0, marker='o')
    plt5.xlim(2.9, 10.1)
    plt5.ylim(-0.21, 0.02)
    plt5.xlabel('Worker Ask', fontsize=14)
    plt5.xticks(np.arange(3, 10.5, step=1))
    plt5.ylabel('Utility of worker', fontsize=14)
    plt5.yticks(np.arange(-0.20, 0.01, step=0.05))
    #pl32.legend()
    plt5.savefig("worker_vs_Utility_truthful_loss.pdf")
    plt5.show()


def reputation_graph():
    time = []
    repu = []
    repuBaseline = []
    repuTSL = []
    detectMWSL = []
    detectTSL = []
    threshold = []
    with open('reputation.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            time.append(float(row[5]))
            repu.append(float(row[2]))
            repuBaseline.append(float(row[3]))
            repuTSL.append(float(row[4]))

    with open('Detection.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            detectTSL.append(float(row[2]))
            detectMWSL.append(float(row[1]))
            threshold.append(float(row[0]))
    plt2.errorbar(time, repu, color='darkblue', yerr=0.0, label='MWSL scheme', marker='o')
    plt2.errorbar(time, repuTSL, color='g', yerr=0.0, label='TSL scheme', marker='^')
    plt2.errorbar(time, repuBaseline, color='r', yerr=0.0, label='Reputation Threshold 0.5', marker='+')
    plt2.xlim(5, 61)
    plt2.ylim(-.01, 1.01)
    plt2.xlabel('Time (s)', fontsize=14)
    plt2.xticks(np.arange(6, 61, step=6))
    plt2.ylabel('Reputation of workers', fontsize=14)
    plt2.yticks(np.arange(0, 1.01, step=0.1))
    plt2.legend()
    plt2.savefig("Time_Reputation.pdf")
    plt2.show()


    ind = np.arange(9)
    fig, ax = plt.subplots()
    ax.bar(ind, detectTSL, color='g', width=0.25, yerr=0.00, label="TSL Scheme")
    ax.bar(ind + 0.25, detectMWSL, color='b', width=0.25, yerr=0.00, label="MWSL scheme")
    plt.xticks(ind + 0.3, threshold)
    plt.xlabel("Reputation Threshold")
    plt.ylabel("Successful Detection Rate")
    plt.legend()
    plt.savefig("detect.pdf")
    plt.show()
#user_graph()
#worker_graph()
#utility_graph()
reputation_graph()
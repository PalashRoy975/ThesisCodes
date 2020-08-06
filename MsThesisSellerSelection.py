from collections import defaultdict
import random
import numpy as np

buyer = 10
seller = 15
price = defaultdict(list)
pair = defaultdict(list)
res_time = defaultdict(list)
r_i = []
t_i = []
for i in range(buyer):
    r_i.append(random.randrange(3, 10, 1))
    t_i.append(random.randrange(500, 1500, 10))
r_i_store = r_i.copy()
t_i_store = t_i.copy()
bidList = []
trueCost = []
worker_ask = []


def worker_part():
    file4 = open("buyersellerReputation.txt", 'w')
    d = defaultdict(list)
    exTime = defaultdict(list)
    cost = defaultdict(list)
    bidDict = defaultdict(list)
    for s in range(seller):
        r_i = r_i_store.copy()
        t_i = t_i_store.copy()
        print("###################### Seller " + str(s+1) + "############################")
        ask_j = random.randint(3, 8)
        worker_ask.append(ask_j)
        print(ask_j)
        R_j = random.randint(20, 40)
        T_j = random.randrange(1000, 4000, 10)
        C_w = []
        B_w = []
        B_j = []
        T_w = []
        n_max = int(random.uniform(4, 10))
        print(n_max)
        c_ij = []
        v = []
        execution_time_ij = []
        priority = []
        maxxxx = 0
        for i in range(buyer):
            k = random.randrange(0, ask_j+3, 1)
            if k > maxxxx:
                maxxxx = k
            c_ij.append(k)
            priority.append(random.uniform(0, 1))
        for x in t_i:
            execution_time_ij.append(random.randrange(1, x, 1))
        temp_cij = c_ij.copy()
        print(temp_cij)
        bidList.append(temp_cij)
        for val in range(len(c_ij)):
            bidDict[val+1].append(c_ij[val])
        for i in range(len(r_i)):
            if c_ij[i] >= ask_j and r_i[i] <= R_j and t_i[i] <= T_j:
                B_j.append(i+1)
            else:
                B_j.append(-1)
                c_ij[i] = -1
                r_i[i] = -1
                t_i[i] = -1
        print("=================Eligible Buyer List================")
        print(B_j)
        print("=================Eligible Buyer Bid List================")
        print(c_ij)
        print("=================Eligible Buyer Resource List================")
        print(r_i)
        print("=================Eligible Buyer Time List================")
        print(t_i)
        priority_factor_i = [(c_ij[i] * priority[i]) / execution_time_ij[i] for i in range(len(execution_time_ij))]
        print("=================Priority Factor================")
        print(priority_factor_i)
        R = 0
        n_j = 0
        myDict = dict()
        sorted_priFactor = dict()
        for val in range(len(r_i)):
            myDict[val] = priority_factor_i[val]
        print(myDict)
        sortedR_i = []
        sortedExecution_i = []
        sortedC_ij = []
        sortedB_j = []
        sorted_temp_cij = []
        sorted_least_time_buyer = []
        sorted_pri = sorted(myDict, key=myDict.get, reverse=True)   #print key in decending order of value
        print("=================Decending order dictionary================")
        print(sorted_pri)
        for r in sorted_pri:
            sorted_priFactor[r] = priority_factor_i[r]
            sortedR_i.append(r_i[r])
            sortedExecution_i.append(execution_time_ij[r])
            sortedC_ij.append(c_ij[r])
            sortedB_j.append(B_j[r])
            sorted_temp_cij.append(temp_cij[r])
            sorted_least_time_buyer.append(t_i[r])
        print(sorted_priFactor)
        print(sortedC_ij)
        print(sortedExecution_i)
        for i in range(len(B_j)):
            if  0 <= sortedR_i[i] <= (R_j - R) and n_j < n_max:
                R = R + sortedR_i[i]
                n_j += 1
                T_w.append(sortedExecution_i[i])
                C_w.append(sortedC_ij[i])
                B_w.append(sortedB_j[i])
            else:
                break
        print("====================Extra Resource=========================")
        print(R_j - R)
        print("====================Final Winning Bid List=========================")
        print(C_w)
        print("====================Final Winning buyer List========================")
        print(B_w)
        print("====================sorted initial bid========================")
        print(sorted_temp_cij)
        print("====================Final Time of Winning buyer List========================")
        print(T_w)
        winning_list_len = len(C_w)
        for i in range(len(B_w)):
            d[B_w[i]].append(s+1)
            exTime[B_w[i]].append(T_w[i])
        print(d)
        C_w_len = len(C_w)
        if C_w_len > 0:
            minimum = min(C_w)
            print("Minimum Value " + str(minimum))
            minimum_bar = sorted_temp_cij[winning_list_len]
            print("alternate Minimum Value " + str(minimum_bar))
            next_min_list = [x for x in sorted_temp_cij if minimum_bar >= x > ask_j]
            print(T_w)
            print(sorted_least_time_buyer)
        else:
            print("Minimum nai")
        for x in range(len(C_w)):
            if minimum <= minimum_bar:
                price_j = minimum + ((C_w[x]-minimum) * (T_w[x] / sorted_least_time_buyer[x]))
            elif minimum > minimum_bar > ask_j:
                price_j = minimum_bar + ((C_w[x] - minimum_bar) * (T_w[x] / sorted_least_time_buyer[x]))
            else:
                price_j = ask_j + ((C_w[x] - ask_j) * (T_w[x] / sorted_least_time_buyer[x]))
            print(price_j)
            cost[B_w[x]].append(round(price_j, 2))
       # print("Price for seller " + str(price_j))
    print(bidDict)
    d_items = d.items()
    sorted_d = sorted(d_items)
    print("===================Buyer Seller pair in auction stage===============")
    print(sorted_d)
    pair = sorted_d.copy()
    exTime_items = exTime.items()
    sorted_exTime = sorted(exTime_items)
    print("===================Time required for Buyer Seller pair in auction stage===============")
    print(sorted_exTime)
    res_time = sorted_exTime.copy()
    cost_item = cost.items()
    sorted_cost = sorted(cost_item)
    print("===================Cost for Buyer Seller pair in auction stage===============")
    print(sorted_cost)
    price = sorted_cost.copy()
    file = open("cost.csv", "w")
    winning_buyer_list = []
    seller_list = []
    cost_list = []
    time_list = []
    for r in sorted_d:
        winning_buyer_list.append(r[0])
        seller_list.append(r[1])
    for r in sorted_cost:
        cost_list.append(r[1])
    for r in sorted_exTime:
        time_list.append(r[1])
    print(winning_buyer_list)
    print(seller_list)
    print(cost_list)
    print(time_list)
    cnt = 0
    file = open("buyersellerCost.txt", 'w')
    file1 = open("buyersellerTime.txt", 'w')
    file2 = open("buyersellerConnection.txt", 'w')
    file3 = open("buyersellerBidList.txt", 'w')
    bid_cnt = 1
    for i in bidDict.values():
        file3.write("==============================")
        file3.write(str(bid_cnt) + "\n")
        for j in range(len(i)):
            file3.write(str(j+1) + " " + str(i[j]) + "\n")
        bid_cnt += 1

    for r in range(buyer):
        buy = ''
        s = r+1
        if s in winning_buyer_list:
            for j in range(seller):
                if j+1 in seller_list[cnt]:
                    buy += str(j + 1) + " "
            for k in cost_list[cnt]:
                buy += str(k) + " "
            for k in time_list[cnt]:
                buy += str(k) + " "

            cnt += 1
        else:
            buy += str(s)
        temp = buy.split()
        tempLength = len(temp)/3
        print(r+1)
        seller_cnt = 0
        sellerNew = []
        cost = []
        time =[]
        for i in range(int(tempLength)):
            sellerNew.append(int(temp[i]))
            cost.append(temp[i+int(tempLength)])
            time.append(temp[i+2*int(tempLength)])
        file.write("==============================")
        file.write(str(r+1) + "\n")
        file1.write("==============================")
        file1.write(str(r + 1) + "\n")
        file2.write("==============================")
        file2.write(str(r + 1) + "\n")
        file4.write("==============================")
        file4.write(str(r + 1) + "\n")
        rep = []
        for k in range(seller):
            rep.append(random.uniform(0, 1))
            if k+1 in sellerNew:
                print("Seller " + str(k+1) + " Cost " + cost[seller_cnt] + " Time " + time[seller_cnt])
                file.write(str(k+1) + " " + cost[seller_cnt] + " \n")
                file1.write(str(k + 1) + " " + time[seller_cnt] + " \n")
                file2.write(str(k + 1) + " " + str(1) + "\n ")

                file4.write(str(k + 1) + " " + str(round(rep[k], 2)) + "\n ")
                seller_cnt += 1
            else:
                print("Seller " + str(k + 1) + " Cost " + str(0) + " Time " + str(0))
                file.write(str(k + 1) + " " + str(0) + "\n ")
                file1.write(str(k + 1) + " " + str(0) + "\n ")
                file2.write(str(k + 1) + " " + str(0) + "\n ")
                file4.write(str(k + 1) + " " + str(0) + "\n ")
    file.close()
    file1.close()
    file2.close()
    file3.close()
    print(len(winning_buyer_list))
    return pair, price, res_time, bidList


worker_list, worker_price, worker_time, bids= worker_part()       #Call Worker part
print(worker_list)
print(worker_price)
print(worker_time)
worker_bid = np.array(bids).T

repu = [[round(random.uniform(0, 1), 2) for i in range(seller)] for j in range(buyer)]
print(np.array(repu))
maxBidList = [max(i) for i in worker_bid]

index = 0
total_utility_QoE = 0
total_utility = 0
Qoe_list = []
Qoe_buyer = 0
Utility_worker = 0
utility_buyer = 0
trueCost = []
for i in range(len(maxBidList)):
    v = maxBidList[i]
    k = random.randrange(v-4, 11, 1)
    trueCost.append(k)

main_pair = []
Quality = []
Quality_get = []
Q_max = 0.1
Q_min = 0
Worker_price = []
actual_price = []
for b in range(buyer):
    U_c = []
    U_t = []
    U_q = []
    U_ij = []
    kappa = round(random.uniform(0.4, 1), 2)
    omega = round(random.uniform(0, 0.5), 2)
    #kappa = 0.3
    #omega = 0.5
    maxi = 0
    success_utility = 0
    worker = 0
    QoE = 0
    pair = []
    for i in worker_list:
        w = i[0]
        if b + 1 == w:
            print(w)
            cnt = 0
            for j in i[1]:
                bid = worker_price[index][1][cnt]
                time = worker_time[index][1][cnt]
                cnt += 1

                utility_cost = round(((trueCost[index] - bid)) / (trueCost[index]), 2)
                utility_time = round((1 - time/t_i[w-1]), 2)
                utility_qoe = round((kappa * utility_time + (1 - kappa) * repu[w-1][j-1]), 2)
                final_utility = round((omega * utility_cost + (1 - omega) * utility_qoe), 2)
                if final_utility > maxi:
                    Q = round(random.uniform(0, 0.7), 2)
                    Q_com = min(0, Q - 0.2)
                    Q_get = round(random.uniform(Q, Q), 2)
                    Q_work = round((Q_com - Q_get), 2)
                    task_completion = random.randrange(200, t_i[w - 1] + 200, 50)
                    worker = j
                    maxi = final_utility
                    success_utility = final_utility
                    QoE = utility_time
                    Qoe_buyer = round((1 - task_completion / t_i[w - 1]), 2)
                    price = bid
                    price1 = bid
                    price_real = bid * r_i[w-1]
                    reward = (trueCost[index] - price) * r_i[w-1] * np.exp((Q_work - Q_max) * 2)
                    penalty = np.exp((Q_min - Q_work) * 2)
                    if Q_work <= Q_max and task_completion <= t_i[w-1]:
                        price = (price * r_i[w-1]) + reward
                    elif Q_work > Q_max:
                        price = penalty * price

                    a = worker_ask[j-1]
                    Utility_W = (price - a) / price
                    bidd = worker_bid[w-1][j-1]

                U_q.append(utility_qoe)
                U_c.append(utility_cost)
                U_t.append(utility_time)
                U_ij.append(final_utility)
                if Qoe_buyer < 0:
                    Qoe_buyer = 0
            Worker_price.append(round(price, 2))
            actual_price.append(round(price_real, 2))
            Quality.append(Q_work)
            Quality_get.append(Q_get)
            pair.append(bidd)
            pair.append(price1)
            pair.append(a)
            Qoe_list.append(Qoe_buyer)
            index += 1
            total_utility_QoE += Qoe_buyer
            total_utility += success_utility
            Utility_worker += Utility_W
            utility_buyer += utility_cost
            main_pair.append(pair)

    print(U_q)
    print(U_ij)
    print("Worker " + str(worker) + " Utility " + str(success_utility))

print(total_utility_QoE, index)
print("===============QoE===================")
print(total_utility_QoE/index)
print(total_utility/index)
print(Qoe_list)
print(worker_ask)

print(Utility_worker/index)
print(utility_buyer/index)
print(utility_buyer/index - Utility_worker/index)
#print(np.array(main_pair))
print(Quality)
print(Quality_get)
print(Worker_price)
print(actual_price)
given_price = sum(Worker_price)/len(worker_price)
print(given_price)
print(sum(actual_price)/len(actual_price))
#print(main_pair)
#a = np.asarray(main_pair)
#print(a)
#np.savetxt('rationality.csv', a, delimiter=",")
print("True Cost")
print(trueCost)
print(worker_bid)
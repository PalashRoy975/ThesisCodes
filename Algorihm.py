import re

bs=4#base stations
v=4 #vnf
d=3 #datacenters
vnf=v+3
vnfSize=200000
executionTime=2.3
thresholdTime=100
relocationCost=0.5
taunot=0
alpha=0.3

a1=1
b=0.2
ant=5
gama=0.3
max_iteration=3
gamag=0.4
previous = [[[0 for k in range(0, d + 1)] for j in range(0, v + 1)] for i in range(0, bs + 1)]
exist = [[[0 for k in range(0, d + 1)] for j in range(0, v + 1)] for i in range(0, bs + 1)]
dc2dc= [0 for k in range(0,d+1)]
dc2bs= [0 for k in range(0,bs+1)]
comTime=[[[0 for k in range(0, d + 1)] for j in range(0, v + 1)] for i in range(0, bs + 1)]
initialAssignment=[[0 for k in range(0,v+1)] for i in range(0,bs+1)]
capacity=[8 for k in range(0,d+1)]
currentVnf= [0 for k in range(0,d+1)]
RateDc=[0 for k in range(0,d+1)]
relocationTime= [[[0 for k in range(0, d + 1)] for j in range(0, v + 1)] for i in range(0, bs + 1)]
Y = [[[0 for k in range(0, d + 1)] for j in range(0, v + 1)] for i in range(0, bs + 1)]
serviceCost= [0 for k in range(0,d+1)]
nita = [[[0 for k in range(0, d + 1)] for j in range(0, v + 1)] for i in range(0, bs + 1)]
bin = [[[0 for k in range(0, d + 1)] for j in range(0, v + 1)] for i in range(0, bs + 1)]
tau = [[[0 for k in range(0, d + 1)] for j in range(0, v + 1)] for i in range(0, bs + 1)]
used = [[[0 for k in range(0, d + 1)] for j in range(0, v + 1)] for i in range(0, bs + 1)]
candidateDC=[]
antSolution=[[[0 for k in range(0, v + 1)] for j in range(0, bs + 1)] for i in range(0, ant)]

file1 = open("text2.txt","r+")
a = file1.readlines()
for i in range(0,len(a)):
    str = a[i]
    if(a[i]=='\n') :
        continue
    mat2 = [int(s) for s in str.split() if s.isdigit()]
    for p in range(1, bs+1):  # 4 bs
        #print("aaaaaaa")
        #print(len(mat2))
        for k in range(1,d+1):
             previous[p][mat2[0]][k] = mat2[k]


#print(previous)

file1 = open("text3.txt","r+")
a = file1.readlines()
for i in range(0,len(a)):
    str = a[i]
    if(a[i]=='\n') :
        continue
    mat3 = [int(s) for s in str.split() if s.isdigit()]
    for p in range(1, bs+1):  # 4 bs
        #print("aaaaaaa")
        #print(len(mat2))
        for k in range(1,d+1):
             exist[p][mat3[0]][k] = mat3[k]

#print(exist)
file1 = open("dc2dc.txt","r+")
a = file1.readlines()
for i in range(0,len(a)):
    str = a[i]
    # if(a[i]=='\n') :
    #     continue
    mat4 = re.findall(r"[-+]?\d*\.\d+|\d+", str)
    #print(mat4)
    index= int(mat4[0])
    dis = float(mat4[1])
    dc2dc[index]=dis

#print(dc2dc)
file1 = open("dc2bs.txt","r+")
a = file1.readlines()
for i in range(0,len(a)):
    str = a[i]
    # if(a[i]=='\n') :
    #     continue
    mat5 = re.findall(r"[-+]?\d*\.\d+|\d+", str)
    #print(mat5)
    index= int(mat5[0])
    dis = float(mat5[1])
    dc2bs[index]=dis

#print(dc2bs)
file1 = open("DCrate.txt","r+")
a = file1.readlines()
for i in range(0,len(a)):
    str = a[i]
    # if(a[i]=='\n') :
    #     continue
    mat5 = re.findall(r"[-+]?\d*\.\d+|\d+", str)
    #print(mat5)
    index= int(mat5[0])
    dis = float(mat5[1])
    RateDc[index]=dis
#print(RateDc)

file1 = open("serviceCost.txt","r+")
a = file1.readlines()
for i in range(0,len(a)):
    str = a[i]
    # if(a[i]=='\n') :
    #     continue
    mat5 = re.findall(r"[-+]?\d*\.\d+|\d+", str)
    #print(mat5)
    index= int(mat5[0])
    dis = float(mat5[1])
    serviceCost[index]=dis
#print(serviceCost)



for i in range(1,bs+1):
    for j in range(1,v+1):
        for k in range(1,d+1):
            if previous[i][j][k]==1 or exist[i][j][k]==1:
                relocationTime[i][j][k]= 0;
            else:
                relocationTime[i][j][k] = vnfSize / RateDc[k]

#print(relocationTime)
#Getting communication time for all the VNFs
for i in range(1,bs+1):
    for j in range(1,v+1):
        for k in range(1,d+1):
           comTime[i][j][k]=dc2bs[i]+dc2dc[k]

#print(comTime)

for i in range(1,bs+1):
    for j in range(1,v+1):
        for k in range(1,d+1):
           Y[i][j][k]=comTime[i][j][k]+relocationTime[i][j][k]+executionTime



#print(Y)

##########################Initial Assignment####################
for j in range (1,bs+1):
    for f in range(1,v+1):
        for k in range(1,d+1):
            if (currentVnf[k]<capacity[k] and Y[j][f][k]<thresholdTime):
                initialAssignment[j][f]=k;
                bin[j][f][k]=1
                currentVnf[k]+=1
                break;

print(initialAssignment)

#########defining nita###############
for j in range (1,bs+1):
    for f in range(1,v+1):
        for k in range(1,d+1):
            x=alpha*relocationTime[j][f][k]*relocationCost
            x+=(1-alpha)*comTime[j][f][k]*serviceCost[k]
            nita[j][f][k]=1/x;

#print("nita........")
#print(nita)

##########defining tau not##################
for j in range (1,bs+1):
    for f in range(1,v+1):
        for k in range(1,d+1):
            x=1/(relocationTime[j][f][k]+comTime[j][f][k])
            x=x*bin[j][f][k]
            taunot+=x

#print("taunot   ",taunot)

########initializing tau##################
for j in range (1,bs+1):
    for f in range(1,v+1):
        for k in range(1,d+1):
            tau[j][f][k]= taunot


def build_candidates():
    candidateDC.clear()
    for k in range(1,d+1):
        if(currentVnf[k]<capacity[k]):
            candidateDC.append(k)



def dcSelection(j,f):
    bestDC=0
    print("for (bs,vnf) -> (",j,",",f,") , candidate DCs --- ",candidateDC)
    print("")
    maxnita_tau=0

    for k in candidateDC:
        temp = pow(tau[j][f][k],a1) * pow(nita[j][f][k],b)
        print("for dc ",k,",","temp = ",temp," tau = ",tau[j][f][k]," nita  = ",nita[j][f][k])
        if(temp> maxnita_tau):
            bestDC=k
            maxnita_tau=temp
    #print("suitable dc for (bs,vnf) -> (",j,",",f,")  is  --",bestDC)
    print("");
    return bestDC

#########clearing currentvnf######
def clearCurrentVnf():
    for k in range(1,d+1):
        currentVnf[k]=0

def globalUpdate(n):
    for j in range(1,bs+1):
        for f in range(1,v+1):
            for k in range(1,d+1):
                if(antSolution[n][j][f]==k):
                    tau[j][f][k]=(1-gamag)*tau[j][f][k]+gamag*tau[j][f][k]
                else:
                    tau[j][f][k] = (1 - gamag) * tau[j][f][k]



def printTau():
    for j in range(1, bs + 1):
        for f in range(1, v + 1):

            for k in range(1, d + 1):
                print("(bs,vnf,dc)------------", j, f,k,"tau----------",tau[j][f][k])


def calculateRelocation():
    rel=0
    for j in range(1,bs+1):
        for f in range(1,v+1):
            k=initialAssignment[j][f]
            if(previous[j][f][k]==0 and exist[j][f][k]==0):
                rel=rel+1
    return rel

def antColony():
    maxcost = 99999999999
    for itr in range(0,max_iteration):
        print("*********** iteration ",itr,"*****************")
        for n in range(0,ant):
            print("*********** ant ", n,"**************")
            clearCurrentVnf()
            for j in range(1,bs+1):
                for f in range(1,v+1):
                    build_candidates()
                    k=dcSelection(j,f)
                    currentVnf[k]+=1
                    #initialAssignment[j][f]=k
                    antSolution[n][j][f]=k
            for j in range(1,bs+1):
                for f in range(1,v+1):
                    k=initialAssignment[j][f]
                    if(used[j][f][k]==0):
                        tau[j][f][k] =  gama * taunot
                        used[j][f][k]=1
                    else:
                        tau[j][f][k] = (1 - gama) * tau[j][f][k] +gama*taunot
            print("For ant ",n)
            print("Solution set for ant ",n, " ",antSolution[n])
            #print(initialAssignment)
            print("Tao values for ant ",n,"after local update")
            printTau()
            temp=calculateCost(n)
            #print(" ant ",n,"  cost   ",temp)
            if(temp<maxcost):
                maxcost=temp
                bestant=n
        print("best ant --------------- ",bestant)
        globalUpdate(bestant)
        for p in range(1,bs+1):
            for q in range(1,v+1):
                initialAssignment[p][q]=antSolution[bestant][p][q]
        print("after global update of iteration ",itr)
        printTau()


def calculateCost(n):
    sum = 0
    for j in range(1, bs + 1):
        for f in range(1, v + 1):
            k = antSolution[n][j][f]
            sum += alpha * relocationTime[j][f][k] * relocationCost + (1 - alpha) * comTime[j][f][k] * serviceCost[k]
    return sum
sum=0
for j in range(1,bs+1):
    for f in range(1,v+1):
        k=initialAssignment[j][f]
        sum+=alpha*relocationTime[j][f][k]*relocationCost+(1-alpha)*comTime[j][f][k]*serviceCost[k]

print("Totat Cost in initial Assignment --- ",sum)
antColony()
#print(initialAssignment)
sum=0
for j in range(1,bs+1):
    for f in range(1,v+1):
        k=initialAssignment[j][f]
        sum+=alpha*relocationTime[j][f][k]*relocationCost+(1-alpha)*comTime[j][f][k]*serviceCost[k]


print("Totat Cost after running ant algorithm  --- ",sum)
print(initialAssignment)
print(calculateRelocation())
S=[[-1,0,0],[-1,0,1],[-1,1,0],[-1,1,1]]
W=[0,0,0]
d=[-1,-1,-1,1]
dM=[]
Miss=[]
def findMisclassify():
    for i in range(len(S)):
        result=0
        for j in range(len(S[i])):
            result += d[i]*S[i][j]*W[j]    
        if result <= 0:
                Miss.append(S[i]);
                dM.append(d[i])

findMisclassify()
while(len(Miss) > 0):
    for i in range(len(Miss)):
        for j in range(len(Miss[i])):
            W[j]+= 0.5*dM[i]*Miss[i][j]  
    Miss =[]
    dM=[]
    findMisclassify()
print W

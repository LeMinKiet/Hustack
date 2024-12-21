n=int(input())
import random
def Select_col(arrays,mode):
    node=max(arrays)
    index=[]
    if mode:
        for i in range(len(arrays)):
            if arrays[i]==node:
                index.append(i)
        return random.choice(index)
    return random.randint(0, len(arrays)-1)
def initial_solution(n):
    init=[0 for i in range(n)]
    full=[0 for i in range(n)]
    ins=0
    for i in range(n):
        if full[ins]!=0:
            ins+=1
        ins=ins%n
        init[i]=ins
        full[ins]=1
        ins+=2
        ins=ins%n
    left=[init[i]+i for i in range(n)]
    right=[init[i]-i for i in range(n)]
    counterLeft=dict()
    counterRight=dict()
    for i in range(n):
        counterLeft[left[i]]=0
        counterRight[right[i]]=0
    for i in range(n):
        counterLeft[left[i]]+=1
        counterRight[right[i]]+=1
    for i in range(n):
        full[i]=counterLeft[left[i]]+counterRight[right[i]]-2
    return full, init
def local_search_queen(n):
    selects, queen=initial_solution(n)
    collison=sum(selects)/2
    Check=dict()
    Check[str(queen)]=0
    QueenT=[[] for i in range((n*(n-1)//2)+1)]
    FullT=[[] for i in range((n*(n-1)//2)+1)]
    mode=True
    count=0
    while collison !=0:
        count+=1
        y=Select_col(selects,mode)
        ins=0
        for i in range(n):
            queen[y]=i
            try:
                #exist
                if Check[str(queen)]==0:
                    a=0
            except:
                col, full= caculate(n, queen)
                Check[str(queen)]=0
                show=queen[:]
                know=full[:]
                QueenT[col].append(show)
                FullT[col].append(know)
        #complete adding
        while ins<len(QueenT):
             if len(QueenT[ins])!=0:
                 queen=QueenT[ins][0]
                 selects=FullT[ins][0]
                 QueenT[ins].pop(0)
                 FullT[ins].pop(0)
                 mode=True
                 break
             ins+=1
             mode=False
        collison=ins
    return queen  
        
def caculate(n,queen):
    init=queen
    full=[0 for i in range(n)]
    left=[init[i]+i for i in range(n)]
    right=[init[i]-i for i in range(n)]
    counterLeft=dict()
    counterQueen=dict()
    counterRight=dict()
    for i in range(n):
        counterLeft[left[i]]=0
        counterRight[right[i]]=0
        counterQueen[init[i]]=0
    for i in range(n):
        counterLeft[left[i]]+=1
        counterRight[right[i]]+=1
        counterQueen[init[i]]+=1
    for i in range(n):
        full[i]=counterQueen[init[i]]+counterLeft[left[i]]+counterRight[right[i]]-3
    return sum(full)//2, full
print(' '.join(list(map(str,local_search_queen(n)))) )           
        
     
    
    

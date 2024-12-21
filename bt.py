import math
n = int(input())
valueOf=list(map(int,input().split()))
violates=0
command=input();
queue=[]
def AllDifferent(listvalue):
    count=0
    for i in range(len(listvalue)-1):
        for j in range(i+1,len(listvalue)):
            if listvalue[i] == listvalue[j]:
                count+=1
    return count
def isEqual(listvalue,x,y):
    return abs(listvalue[x-1]-listvalue[y-1])
def LessThanEqual(listvalue,x,y):
    return max(0,listvalue[x-1]-listvalue[y-1])
def update(listvalue,x,y):
    listvalue[x-1]=y
    return
while command != "#":
    listWord=command.split()
    if listWord[0]=="post":
        if listWord[1]=="AllDifferent":
            violates+=AllDifferent(valueOf)
            queue.append(command)
        if listWord[1]=="IsEqual":    
            x=int(listWord[2])
            y=int(listWord[3])
            violates+=isEqual(valueOf,x,y)
            queue.append(command)
        if listWord[1]=="LessThanEqual":
            x=int(listWord[2])
            y=int(listWord[3])
            violates+=LessThanEqual(valueOf,x,y)
            queue.append(command)
    if listWord[0]=="violations":
        print(violates)
    if listWord[0]=="update":
        x=int(listWord[1])
        y=int(listWord[2])
        update(valueOf,x,y)
        violates=0
        for i in range(len(queue)):
            incommand=queue[i]
            inlistWord=incommand.split()
            if inlistWord[1]=="AllDifferent":
                violates+=AllDifferent(valueOf)
            if inlistWord[1]=="IsEqual":    
                x=int(inlistWord[2])
                y=int(inlistWord[3])
                violates+=isEqual(valueOf,x,y)
            if inlistWord[1]=="LessThanEqual":
                x=int(inlistWord[2])
                y=int(inlistWord[3])
                violates+=LessThanEqual(valueOf,x,y)
    command=input()
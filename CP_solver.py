from ortools.linear_solver import pywraplp
class SimplexSolver():
    def __init__(self,filepath: str):
        self.filepath=filepath
    def takeInput(self):
        self.n, self.m=list(map(int,input().split()))
        self.objective=list(map(int,input().split()))
        self.constraint=[list(map(int,input().split())) for i in range(self.m)]
        self.rightHand=list(map(int,input().split()))
    def takeInputbyFilepath(self):
        with open(self.filepath,"r") as f:
            lines=f.readlines()
            self.n, self.m=list(map(int,lines[0].split()))
            self.objective=list(map(int,lines[1].split()))
            self.constraint=[list(map(int,lines[i].split())) for i in range(2,self.m+2)]
            self.rightHand=list(map(int,lines[self.m+2].split()))
    def print(self):
        self.takeInputbyFilepath()
        print(self.n,self.objective,self.constraint,self.rightHand)
        return 0
    def solverByOrtools(self):
        self.takeInputbyFilepath()
        model=pywraplp.Solver.CreateSolver("GLOP")
        if not model:
            return
        x=[model.NumVar(0,model.infinity(),"x["+str(i)+"]") for i in range(self.n)]
        for i in range(self.m):
            model.Add(sum(list(map(lambda k: self.constraint[i][k]*x[k],range(self.n))))<=self.rightHand[i])
        model.Maximize(sum(list(map(lambda h:self.objective[h]+x[h],range(self.n)))))
        status=model.Solve()
        if status == pywraplp.Solver.OPTIMAL:
            print(self.n)
            for i in range(self.n):
                print(f"{x[i].solution_value():0.1f}",end=" ")
        else:
            print("UNBOUNDED")
        return 0
    #Iteration
    def solverByLocalSearch(self):
        self.takeInputbyFilepath()
        solution=[0 for i in range(self.n)]
        basis=[[1 if i==j else 0 for i in range(self.m)] for j in range(self.m)]
        obj=list(map(lambda x:self.constraint[x]+basis[x]+[self.rightHand[x]],range(self.m)))
        objecti=self.objective+[0 for i in range(self.m)]
        if (max(objecti)<=0):
            print("UNBOUNDED")
            return
        while (max(objecti)>0):
            indexX=objecti.index(max(objecti))
            E=list(map(lambda x: obj[x][-1]/obj[x][indexX] if obj[x][indexX] !=0 and obj[x][-1]/obj[x][indexX]>=0 else float("inf"),range(self.m)))
            if(min(E)==float("inf")):
                print("UNBOUNDED")
                return
            indexY=E.index(min(E))
            divisor=obj[indexY][indexX]
            for i in range(len(obj[0])):
                obj[indexY][i]/=divisor
            for i in range(self.m):
                if (i!=indexY):
                    obj[i]=list(map(lambda x: obj[i][x]-obj[i][indexX]*obj[indexY][x],range(len(obj[0]))))
            objecti=list(map(lambda x: objecti[x]-objecti[indexX]*obj[indexY][x],range(len(objecti))))
        for i in range(self.m):
            for j in range(self.n):
                if(obj[i][j]==1):
                    solution[j]=obj[i][-1]
        print(" ".join(list(map(str,solution))))
           


                


cp=SimplexSolver("test.txt")
cp.solverByLocalSearch()

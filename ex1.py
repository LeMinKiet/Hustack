from ortools.sat.python import cp_model
class Solver():
    def __init__(self,filepath):
        self.filepath=filepath
    def takeInput(self):
        self.nbWareshouse,self.nbMarket=list(map(int,input().split()))
        self.Warehouse=list(map(int,input().split()))
        self.Market=list(map(int,input().split()))
        self.distance=[list(map(int,input().split())) for i in range(3,self.nbWareshouse+3)]
    def takeInputByFilepath(self):
        with open(self.filepath,"r") as f:
            lines=f.readlines()
            self.nbWareshouse,self.nbMarket=list(map(int,lines[0].split()))
            self.Warehouse=list(map(int,lines[1].split()))
            self.Market=list(map(int,lines[2].split()))
            self.distance=[list(map(int,lines[i].split())) for i in range(3,self.nbWareshouse+3)]
    def solve(self):
        model=cp_model.CpModel()

        goods=[[model.NewIntVar(0,1,"goods["+str(i)+"]["+str(j)+"]") for j in range(self.nbMarket)] for i in range(self.nbWareshouse)]
        deliver=[[model.NewIntVar(0,max(self.Warehouse),"deliver["+str(i)+"]["+str(j)+"]") for j in range(self.nbMarket)] for i in range(self.nbWareshouse)]
        for i in range(self.nbWareshouse):
            model.Add(sum(list(map(lambda x: deliver[i][x],range(self.nbMarket))))<=self.Warehouse[i])
        for j in range(self.nbMarket):
            model.Add(sum(list(map(lambda x: deliver[x][j],range(self.nbWareshouse))))>=self.Market[j])
        for i in range(self.nbWareshouse):
            for j in range(self.nbMarket):
                b=model.NewBoolVar("")
                model.Add(deliver[i][j]!=0).OnlyEnforceIf(b)
                model.Add(deliver[i][j]==0).OnlyEnforceIf(b.Not())
                model.Add(goods[i][j]==1).OnlyEnforceIf(b)
                model.Add(goods[i][j]==0).OnlyEnforceIf(b.Not())
        
        objective=sum([sum(list(map(lambda y: goods[x][y]*self.distance[x][y],range(self.nbMarket)))) for x in range(self.nbWareshouse)])
        model.Minimize(objective)

        solver=cp_model.CpSolver()
        status=solver.Solve(model)
        if status==cp_model.OPTIMAL or status==cp_model.FEASIBLE:
            print(solver.Value(objective))
            for i in range(self.nbWareshouse):
                for j in range(self.nbMarket):
                    print(str(i+1)+" "+str(j+1)+" "+str("%.1f" % solver.Value(deliver[i][j])))
        else:
            print("No")


cp=Solver("test.txt")
cp.takeInput()
cp.solve()

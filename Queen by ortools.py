from ortools.sat.python import cp_model
class SolverQueen():
    def __init__(self):
        pass
    def takeInput(self):
        self.n=int(input())
    def solveByOrtools(self):
        self.takeInput()
        model=cp_model.CpModel()
        chess= [[model.new_int_var(0,1,"chess["+str(i)+"]["+str(j)+"]") for j in range(self.n)] for i in range(self.n)]
        for k in range(self.n):
            model.add(sum(chess[k])==1)
            model.add(sum(list(map(lambda x: chess[x][k],range(self.n))))==1)
        for i in range(self.n):
            for j in range(self.n):
                b=model.new_bool_var("")
                model.add(chess[i][j]==1).only_enforce_if(b)
                model.add(chess[i][j]==0).only_enforce_if(b.Not())
                for k in range(self.n):
                    if(k!=0):
                        if(i+k<self.n and j+k<self.n):
                            model.add(chess[i+k][j+k]==0).only_enforce_if(b)
                        if(i+k<self.n and j-k>=0):
                            model.add(chess[i+k][j-k]==0).only_enforce_if(b)
                        if(i-k>=0 and j-k>=0):
                            model.add(chess[i-k][j-k]==0).only_enforce_if(b)
                        if(i-k>=0 and j+k<self.n):
                            model.add(chess[i-k][j+k]==0).only_enforce_if(b)
        solver=cp_model.CpSolver()
        status=solver.solve(model)
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            for i in range(self.n):
                for j in range(self.n):
                    if(j==self.n-1):
                        print(solver.Value(chess[i][j]))
                    else:
                        print(solver.Value(chess[i][j]),end=" ")

cp=SolverQueen()
cp.solveByOrtools()        
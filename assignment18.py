#!/usr/bin/env python
import numpy as np

from PyTrilinos import Epetra
from PyTrilinos import AztecOO

class OneDimLaplace(object):

    def __init__(self, comm, number_of_elements=10):

        self.comm = comm
        self.rank = comm.MyPID()
        self.size = comm.NumProc()

        # if self.rank == 0:
            # number_of_entries_per_row = np.ones(number_of_elements,  dtype=np.int32) * 3
            # number_of_entries_per_row[0] = 2
            # number_of_entries_per_row[-1] = 2
        # else:
            # number_of_entries_per_row = np.array([0],  dtype=np.int32)
        
        unbalanced_map = Epetra.Map(number_of_elements, 0, self.comm)

        self.A = Epetra.CrsMatrix(Epetra.Copy, unbalanced_map, 3) 
        for gid in unbalanced_map.MyGlobalElements():
            if gid in (0,number_of_elements-1): 
                self.A.InsertGlobalValues(gid,[1],[gid])
            else: 
                self.A.InsertGlobalValues(gid,[-1,2,-1],[gid-1,gid,gid+1])

        self.A.FillComplete()
        self.x = Epetra.Vector(unbalanced_map) 
        self.b = Epetra.Vector(unbalanced_map) #Boundary conditions
        if self.rank == 0:
            self.b[0] = -1
        if self.rank == self.size-1:
            self.b[-1] = 1

    def solve(self):

        linear_problem = Epetra.LinearProblem(self.A, self.x, self.b) 
        solver = AztecOO.AztecOO(linear_problem) 
        solver.Iterate(10000,1.e-5)  

    def get_solution(self):
        return self.x



if __name__ == "__main__":

    from PyTrilinos import Epetra

    comm = Epetra.PyComm()

    solver = OneDimLaplace(comm)
    solver.solve()

    print(solver.get_solution())

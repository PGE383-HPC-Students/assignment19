#!/usr/bin/env python
import numpy as np

from PyTrilinos import Epetra
from PyTrilinos import AztecOO
from PyTrilinos import Teuchos
from PyTrilinos import Isorropia

class OneDimLaplace(object):

    def __init__(self, comm, number_of_elements=10):

        self.comm = comm
        self.rank = comm.MyPID()
        self.size = comm.NumProc()

        if self.rank == 0:
            number_of_rows = number_of_elements
        else:
            number_of_rows = 0
        
        unbalanced_map = Epetra.Map(-1, number_of_rows, 0, self.comm)

        self.A = Epetra.CrsMatrix(Epetra.Copy, unbalanced_map, 3) 
        self.x = Epetra.Vector(unbalanced_map) 
        self.b = Epetra.Vector(unbalanced_map) 

        for gid in unbalanced_map.MyGlobalElements():
            if gid == 0: 
                self.A.InsertGlobalValues(gid,[1],[gid])
                self.b[0] = -1
            elif gid == (number_of_elements - 1): 
                self.A.InsertGlobalValues(gid,[1],[gid])
                self.b[-1] = 1
            else: 
                self.A.InsertGlobalValues(gid,[-1,2,-1],[gid-1,gid,gid+1])

        self.A.FillComplete()

    def load_balance(self):

        return

    def solve(self):

        return 

    def get_solution(self):
        return self.x




if __name__ == "__main__":

    from PyTrilinos import Epetra

    comm = Epetra.PyComm()

    solver = OneDimLaplace(comm)
    solver.load_balance()
    solver.solve()

    print(solver.get_solution())

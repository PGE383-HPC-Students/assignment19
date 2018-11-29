#!/usr/bin/env python
import os
import unittest
import numpy as np
from PyTrilinos import Epetra

from assignment19 import OneDimLaplace

class TestOneDimLaplace(unittest.TestCase):

    def setUp(self):

        comm = Epetra.PyComm()
        self.solver = OneDimLaplace(comm)

    def test_load_balance(self):

        self.solver.load_balance()
        if self.solver.size == 2:
            if self.solver.rank == 0:
                np.testing.assert_allclose(self.solver.b, np.array([-1., 0., 0., 0., 0.]), atol=0.1)
            if self.solver.rank == 1:
                np.testing.assert_allclose(self.solver.b, np.array([0., 0., 0., 0., 1.]), atol=0.1)
        if self.solver.size == 3:
            if self.solver.rank == 0:
                np.testing.assert_allclose(self.solver.b, np.array([0., 0., 0., 0.]), atol=0.1)
            if self.solver.rank == 1:
                np.testing.assert_allclose(self.solver.b, np.array([-1., 0., 0.]), atol=0.1)
            if self.solver.rank == 2:
                np.testing.assert_allclose(self.solver.b, np.array([0., 0., 1.]), atol=0.1)

    def test_solve(self):

        self.solver.load_balance()
        self.solver.solve()
        if self.solver.size == 1:
            np.testing.assert_allclose(self.solver.x, np.array([-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111, 0.11111111,  0.33333333,  0.55555556, 0.77777778, 1.]), atol=0.001)
        if self.solver.size == 2:
            if self.solver.rank == 0:
                np.testing.assert_allclose(self.solver.x, np.array([-1., -0.77777778, -0.55555556,  0.11111111,  0.33333333]), atol=0.001)
            if self.solver.rank == 1:
                np.testing.assert_allclose(self.solver.x, np.array([-0.33333333, -0.11111111, 0.55555556, 0.77777778, 1.]), atol=0.001)
        if self.solver.size == 3:
            if self.solver.rank == 0:
                np.testing.assert_allclose(self.solver.x, np.array([-0.33333333, -0.11111111, 0.11111111, 0.33333333]), atol=0.001)
            if self.solver.rank == 1:
                np.testing.assert_allclose(self.solver.x, np.array([-1., -0.77777778, -0.55555556]), atol=0.001)
            if self.solver.rank == 2:
                np.testing.assert_allclose(self.solver.x, np.array([0.55555556, 0.77777778, 1.]), atol=0.001)
                


            



if __name__ == '__main__':
    unittest.main()

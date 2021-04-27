#!/usr/bin/env python

# Copyright 2020-2021 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
    exit()

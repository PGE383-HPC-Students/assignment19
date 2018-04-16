# Homework Assignment 18

[![Build Status](https://travis-ci.com/PGE383-HPC/assignment18.svg?token=SnMGq692xXXqxzyE6QSj&branch=master)](https://travis-ci.com/PGE383-HPC/assignment18)

In this assignment the objective is to solve the one-dimensional Laplace equation using AztecOO, i.e.

![equation](http://latex.codecogs.com/gif.latex?-%5Cfrac%7B%5Cpartial%5E2%20u%7D%7B%5Cpartial%20x%5E2%7D%20%3D%200)

with boundary conditions ![equation](http://latex.codecogs.com/gif.latex?u%280%29%20%3D%20-1)


Your code should be parallel consistent, i.e. it should produce the exact same answer independent of the number of processors you specify.

## Testing

If you would like to check to see if your solution is correct, run the following commands at the Terminal command line:

```bash
mpiexec -np 2 python test.py
mpiexec -np 4 python test.py
```

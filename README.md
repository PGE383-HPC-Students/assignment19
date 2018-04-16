# Homework Assignment 18

[![Build Status](https://travis-ci.com/PGE383-HPC/assignment18.svg?token=SnMGq692xXXqxzyE6QSj&branch=master)](https://travis-ci.com/PGE383-HPC/assignment18)

In this assignment the objective is to solve the one-dimensional steady-state pressure diffusivity equation using AztecOO, i.e.

![equation](http://latex.codecogs.com/gif.latex?-%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%20x%7D%5Cleft%28%5Cfrac%20k%20%5Cmu%20%5Cfrac%7B%5Cpartial%20p%7D%7B%5Cpartial%20x%7D%5Cright%29%20%3D%200)


Your code should be parallel consistent, i.e. it should produce the exact same answer independent of the number of processors you specify.

## Testing

If you would like to check to see if your solution is correct, run the following commands at the Terminal command line:

```bash
mpiexec -np 2 python test.py
mpiexec -np 4 python test.py
```

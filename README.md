# Homework Assignment 19

In this assignment the objective is to solve the one-dimensional Laplace equation using AztecOO, i.e.

![equation](http://latex.codecogs.com/gif.latex?-%5Cfrac%7B%5Cpartial%5E2%20u%7D%7B%5Cpartial%20x%5E2%7D%20%3D%200)

with boundary conditions ![equation](http://latex.codecogs.com/gif.latex?u%280%29%20%3D%20-1) and ![equation](http://latex.codecogs.com/gif.latex?u%28L%29%20%3D%201).  If we use a finite difference discretization of this equation with ![equation](http://latex.codecogs.com/gif.latex?%5CDelta%20x%20%3D%201) we get a discrete equation for any node ![equation](http://latex.codecogs.com/gif.latex?i) 

![equation](http://latex.codecogs.com/gif.latex?-u%28x_i%20-%201%29%20&plus;%202%20u%28x_i%29%20-%20u%28x_i%20&plus;%201%29%20%3D%200)

I've used this discretization and the boundary conditions to create a linear system of equations ![equation](http://latex.codecogs.com/gif.latex?%5Cmathbf%7BA%7D%20%5Cmathbf%7Bx%20%3D%20b%7D) during the construction of the `OneDimLaplace` object.  

However, the linear system is completely on one processor.  Your assignment is the use `Isorropia` from Trilinos to load-balance the problem.  Use the default settings and call the load balancer on the matrix ![equation](http://latex.codecogs.com/gif.latex?%5Cmathbf%7BA%7D), then use the results to load balance the rest of the required data structures before calling `AztecOO` to solve the linear system of equations.

My advice is the implement the `solve()` method first and make sure your code works as expected on a single processor.  Then you can perform the load balancing by implementing the method `load_balance()`

Your code should be parallel consistent, i.e. it should produce the exact same answer independent of the number of processors you specify.

## Testing

If you would like to check to see if your solution is correct, run the following commands at the Terminal command line:

```bash
mpiexec -np 1 python test.py
mpiexec -np 2 python test.py
mpiexec -np 3 python test.py
```

# PTF Tutorials

This repository contains a set of tutorials for the ORKG-PTF.

The files are not in any particular order. The tutorials are done directly in the interactive sessions without prior preparations so expect some mistakes and typos.

![meme](meme.png)

## Table of Content

Here is a list of tutorials we are doing:
- [8 Queens Problem using Genetic Algorithm](#8-queens-problem-using-genetic-algorithm)
- [Builder and Fluid Builder Patterns](#builder-and-fluid-builder-patterns)


### 8 Queens Problem using Genetic Algorithm
The 8 queens problem is a classic problem in which we have to place 8 queens on a chess board such that no queen is attacking any other queen. This means that no two queens can be in the same row, column or diagonal.

The genetic algorithm is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover and selection.

The script: [queens.py](queens.py) contains the implementation of the genetic algorithm for the 8 queens problem. The script is well commented and should be easy to follow.

Which can be run with a simple `python queens.py`.

### Builder and Fluid Builder Patterns
The builder pattern is a creational design pattern that lets us construct complex objects step by step. The pattern allows us to produce different types and representations of an object using the same construction code.

The fluid builder pattern is a variation of the builder pattern that allows us to chain the calls to the builder methods in no particular order. This is done by returning the builder object itself from every method call.

The script: [fluid.py](builder/fluid.py) contains the implementation of the fluid builder pattern. The script is well commented and should be easy to follow. You can run it with a simple `python builder/fluid.py`.

The script: [order.py](builder/order.py) contains the implementation of the builder pattern to highlight the order. This implementation is not up to par because it should use interfaces to enforce the order. The script is well commented and should be easy to follow. You can run it with a simple `python builder/order.py`.

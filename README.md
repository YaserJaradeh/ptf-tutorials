# PTF Tutorials

This repository contains a set of tutorials for the ORKG-PTF.

The files are not in any particular order. The tutorials are done directly in the interactive sessions without prior preparations so expect some mistakes and typos.

![meme](meme.png)

## Table of Content

Here is a list of tutorials we are doing:
- [8 Queens Problem using Genetic Algorithm](#8-queens-problem-using-genetic-algorithm)
- [Builder and Fluid Builder Patterns](#builder-and-fluid-builder-patterns)
- [Decorator Functions](#decorator-functions)
- [Recursion Overview](#recursion-overview)
- [Code Modularization](#code-modularization)


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

A proper implementation for calling the builder methods in order is shown in the script: [proper.py](builder/proper.py). The script is well commented and should be easy to follow. You can run it with a simple `python builder/proper.py`.

### Decorator Functions
Decorator functions are a way to add functionality to an existing function without changing the function itself. This is done by wrapping the function with another function that adds the functionality.
This is a python specific feature that has an intersection with the decorator design pattern.

The script: [decorator.py](decorator.py) contains the implementation of the decorator functions. The script is well commented and should be easy to follow. You can run it with a simple `python decorator.py`.
Note that you need the `undecorated` package installed to run this one

### Recursion Overview
Recursion is a programming technique in which a function calls itself directly or indirectly. This is a very powerful technique that can be used to solve many problems. However, it is not always the best solution and can be very inefficient.
Recursion relies on an understanding of the call stack and how it works. A stack is a LIFO (Last In First Out) data structure. The call stack is a stack that keeps track of the function calls. When a function is called, it is pushed to the top of the stack. When a function returns, it is popped from the top of the stack. This means that the last function to be called is the first to return.

The script: [recursion.py](recursion.py) contains an overview of recursion types and sample examples. The script is well commented and should be easy to follow. You can run it with a simple `python recursion.py`.

### Code Modularization
Code modularization is a generic term that refers to the process of breaking a program into multiple files/components. This is done to make the code more readable and maintainable. It also allows for code reuse and easier collaboration.

In the `modular` folder, you will find two folders `before` and `after` to show different modularization techniques applied on various code snippets to demonstrate the benefits of modularization.
Here is a list of the main concepts covered:
- [func.py](modular/before/func.py): Working with different functions
- [flow.py](modular/before/flow.py): Working with control flow
- [helpers.py](modular/before/helper.py): Working with helper functions
- [clazz.py](modular/before/clazz.py): Working with classes
- [vars.py](modular/before/vars.py): Working with variables
- [pipeline.py](modular/before/pipeline.py): Working with pipelines
- [procedural.py](modular/before/procedural.py): Working with procedural generation

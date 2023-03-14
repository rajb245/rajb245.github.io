---
title: 1D Function Approximation
date: 2023-03-13 13:54
Category: ML notes
---
# 1D Function Approximation
## Abstract
Computer logic circuits can do arithmetic (+-*/) operations floating-point numbers; those are the core functions of the floating-point units of CPUs. This is a set of notes
that explores how such basic operations can be composed to effectively calculate other functions that cannot exactly be expressed as a composition of those operations (e.g., trigonometric, logarithmic, "special" functions, etc.). The idea is to approximate the desired function as a composition of arithmetic operations in such a way that the approximation error matches the underlying precision of the representation. For example, if I can approximate `sin(x)` as a polynomial to about 16 digits of precision for any `FP64` value in `[0,2*pi)`, then that polynomial effectively _is_ `sin(x)` in `FP64` on that domain (and periodic extension can be used for all other `FP64` values).

By learning the mechanics of this approximation process, you can control the precision of the approximation and explore trade-offs in computational complexity vs. precision.
The notes use a simple test case of `f(x)=log(x+1)`, and a more realistic case of the [Gaussian error linear unit (GELU) function](https://arxiv.org/pdf/1606.08415.pdf) that is used in neural networks.
It looks at both polynomial and rational function approximations, with both single-point derivative matching (Taylor and Padé methods) and domain-error-minimization approaches (interpolation and minimax).
All of that is explored while exploiting function structure, symmetries, asymptotics, and domain-decomposition / domain-mapping strategies.

## Files
|1D Function Approximation (Release).pdf|
| :------------------------------------------------------------------------------: |
|[:fontawesome-solid-file-pdf: Download](1D Function Approximation (Release).pdf)|
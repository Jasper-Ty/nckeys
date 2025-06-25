# nckeys

This package explores expansions of Cauchy kernels under various quotients of
the free associative algebra.

## Introduction

The main operational perspective in use here is that a Cauchy kernel encodes a 
[*pairing*](https://en.wikipedia.org/wiki/Pairing) between the **k**-modules 
**k**\[**x**\] and **k**\[**y**\], given by the expansion in 
**k**\[**x**\] ⊗ **k**\[**y**\] of the Cauchy kernel (an element of 
**k**\[**x**,**y**\]).

Cauchy identities, then, are a statement that these pairings can be diagonalized
by changing bases on the left and the right. The basic orthogonality relation
between the monomial and complete homogeneous symmetric functions is a statement
of this form.

The Cauchy identity for Schur functions says that one can use the *same* basis
on the left and right to diagonalize the classical Cauchy kernel.
Moreover, this is proven as a purely combinatorial statement, done over positive 
integers, so it holds in full generality over any commutative ring.
In contrast, the Cauchy identity for the the power sum symmetric functions also 
says that the power sum basis diagonalizes the Cauchy kernel, but not over the 
integers.

In general, by
[Sylvester's law of inertia](https://en.wikipedia.org/wiki/Sylvester%27s_law_of_inertia), 
if one has a symmetric kernel, one is always able to diagonalize in the real and
complex numbers by congruence (= with the same basis on the left and right).


## `main.py`


## Requirements

- Python
    - I believe you need least 3.8 for the features I'm using. 
    I'm running 3.10.12 on my machine


## Tutorial


## Some conventions

- There are two main quantities: `n` and `deg`. `n` will always relate to a 
number of generators, and `deg` will always relate to some notion of size.
    - For polynomial rings, `n` is the number of generators, and `deg` is the
    degree of a homogeneous component.
    - For compositions, `n` is the number of parts, and `deg` is the sum of 
    parts. Note that the degree `deg` homogeneous component of a polynomial ring
    in `n` variables is the free **k**-module with generators the compositions 
    of `deg` with `n` parts.
    - For free associative algebras, `n` is the number of generators, and `deg` 
    is the degree of a homogeneous component.
    - For words, `n` is the size of the alphabet, and `deg` is the length of
    the word. Note that the degree `deg` homogeneous component of a free 
    associative algebra is the free **k**-module with generators the words of
    length `deg` in the alphabet 1..`n`.
- Vectors are viewed as row vectors.
    - As a consequence, composition of linear maps goes left to right.
    - Then, operators indexed by reduced words are applied by reading the
    word left to right.
- Indexing of variables starts at zero, of course.
- A shape is a list of coordinates on the grid.


## Tests

Nearly all functions are tested with `deg=0..3` and `n=0..3`. 

To run the tests, install `unittest` with `pip install unittest`, and run all
tests with `python -m unittest -v`.

This package saves intermediate results in a folder called `DATA_DIR`, which is,
by default, `./data`.


## To-do

- Bijectivizations allowing zero
- Optimize integer matrix code
- Refactor `cache.py`

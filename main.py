import os

from nckeys.composition import Compositions
from nckeys.shape import *
from nckeys.ideals import words_to_compositions, plactic_quotient, rk_quotient
from nckeys.bases import monomial_to_atom, monomial_to_key
from nckeys.bijectivization import Bijectivization
from nckeys.tableau import tableau_word
from nckeys.matrix import Matrix
from nckeys.word import partitions


n = 3
deg = 3
shape_id = "stairs"
expansion = "h"
symm = True
x_ideal = "comm"
x_basis = "key"
u_ideal = "r0"
u_basis = None



# - Shapes ---------------------------------------------------------------------
shapes = {
    "rect": rectangle(n),
    "stairs": stairs(n)
}
# ------------------------------------------------------------------------------

shape = shapes[shape_id]
(m, n) = size(shape)
max_deg = len(shape)

transitions = {
    "mon": Matrix.identity(Compositions(deg, n)),
    "key": monomial_to_key(deg, n),
    "atom": monomial_to_atom(deg, n),
}

ideals = {
    "comm": words_to_compositions(deg, n),
    "plac": plactic_quotient(deg, n),
    "r0": rk_quotient(deg, n, 0),
    "r1": rk_quotient(deg, n, 1),
    "r2": rk_quotient(deg, n, 2),
    "r3": rk_quotient(deg, n, 3),
    "r4": rk_quotient(deg, n, 4),
    "r5": rk_quotient(deg, n, 5),
}

kernel = biword_matrix(shape, deg, expansion)
kernel._name = f"{shape_id}_{expansion}_biwords"

output = kernel
if x_ideal is not None:
    output = ideals[x_ideal].transpose() * output
if x_basis is not None:
    output = transitions[x_basis].transpose() * output
if u_ideal is not None:
    output = output * ideals[u_ideal]
if u_basis is not None:
    output = output * transitions[u_basis]


# Then
filename = f"./results/{shape_id}-{expansion}-{deg}_x-{x_ideal}-{x_basis}_u-{u_ideal}-{u_basis}.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    # Print out shape
    f.write(" ".join([" ", *(str(i) for i in range(n))]) + "\n")
    for i in range(m):
        f.write(" ".join([str(i), *("*" if (i,j) in shape else " " for j in range(n))])+ "\n")

    f.write(f"X (rows) mod relations '{x_ideal}'")
    if x_basis is not None:
        f.write(f" in basis '{x_ideal}'\n")
    else:
        f.write(f"\n")
    f.write(f"U (cols) mod relations '{u_ideal}'")
    if u_basis is not None:
        f.write(f" in basis '{u_ideal}'\n")
    else:
        f.write(f"\n")
    f.write(f"Expanded in degree {deg}\n")
    f.write(str(output))
    f.write(f"\n\nbiword matrix for kernel {shape_id}({expansion})\n")
    f.write(str(kernel))
    f.write(f"\n\nquotient map for X (rows) mod '{x_ideal}'\n")
    f.write(str(ideals[x_ideal].transpose()))
    f.write(f"\n\ntransition map for X (rows) '{x_basis}' \n")
    f.write(str(transitions[x_basis].transpose()))
    f.write(f"\n\nquotient map for U (cols) mod '{u_ideal}' \n")
    f.write(str(ideals[u_ideal]))
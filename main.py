import os
from functools import partial


exit()

from nckeys.composition import Compositions
from nckeys.shape import *
from nckeys.ideals import words_to_compositions, plactic_quotient, rk_quotient, no_repeat
from nckeys.bases import monomial_to_atom, monomial_to_key, key_to_monomial
from nckeys.bijectivization import Bijectivization
from nckeys.tableau import tableau_word
from nckeys.matrix import Matrix
from nckeys.word import partitions


N = 5
expansion = "h"
dagger = True
x_ideal = "comm"
x_basis = "atom"
u_ideal = "r3"
u_basis = None

OUT_DIR="./results"

transitions = {
    "key": monomial_to_key,
    "atom": monomial_to_atom,
}

ideals = {
    "comm": words_to_compositions,
    "plac": plactic_quotient,
    "r0": partial(rk_quotient, k=0),
    "r1": partial(rk_quotient, k=1),
    "r2": partial(rk_quotient, k=2),
    "r3": partial(rk_quotient, k=3),
    "r4": partial(rk_quotient, k=4),
    "r5": partial(rk_quotient, k=5),
}


for root_ideal in root_ideals(N):
    shape = diagram(root_ideal)
    if len(shape) == 0:
        continue
    shape_name = ''.join(str(i) for i in root_ideal)
    m, n = size(shape)
    max_deg = min(len(shape),4)

    for deg in range(1, max_deg+1):
        if deg != 3:
            continue
        filename = f"{OUT_DIR}/{shape_name}-{expansion}{'†' if dagger else ''}/x-{x_ideal}-{x_basis}_u-{u_ideal}-{u_basis}/{deg}.txt"
        print(f"Computing {filename}...", end='')
        kernel = biword_matrix(shape, deg, expansion, dagger)
        kernel._name = f"{shape_name}_{expansion}_biwords"
        
        try:
            output = kernel
            if x_ideal is not None:
                output = ideals[x_ideal](deg, m).transpose() * output
            if x_basis is not None:
                output = transitions[x_basis](deg, m).transpose() * output
            if u_ideal is not None:
                output = output * ideals[u_ideal](deg, n)
            if u_basis is not None:
                output = output * transitions[u_basis](deg, n)
        except Exception as e:
            print(e)
    
        if output.is_nonnegative():
            print("+ve")
        else:
            print()

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(" ".join([" ", *(str(i) for i in range(n))]) + "\n")
            for i in range(m):
                f.write(" ".join([str(i), *("*" if (i,j) in shape else " " for j in range(n))])+ "\n")

            f.write(f"X (rows) mod relations '{x_ideal}'")
            if x_basis is not None:
                f.write(f" in basis '{x_basis}'\n")
            else:
                f.write(f"\n")
            f.write(f"U (cols) mod relations '{u_ideal}'")
            if u_basis is not None:
                f.write(f" in basis '{u_ideal}'\n")
            else:
                f.write(f"\n")
            f.write(f"Expanded in degree {deg}\n")
            f.write(str(output))
            
            if x_ideal is not None:
                f.write(f"\n\nquotient map for X (rows) mod '{x_ideal}'\n")
                f.write(str(ideals[x_ideal](deg, n).transpose()))
            if x_basis is not None:
                f.write(f"\n\ntransition map for X (rows) '{x_basis}' \n")
                f.write(str(transitions[x_basis](deg, n).transpose()))
            if u_ideal is not None:
                f.write(f"\n\nquotient map for U (cols) mod '{u_ideal}' \n")
                f.write(str(ideals[u_ideal](deg, n)))

            f.write(f"\n\nbiword matrix for kernel {shape_name}({expansion})\n")
            f.write(str(kernel))




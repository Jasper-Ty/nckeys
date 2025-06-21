from nckeys.operators import demazure

deg = 2
n = 2

print(demazure(0,1,0, deg=3, n=3))

# Computing key polynomial matrix:

# First, don't care about redundant calculations, first step.

from nckeys.lib import compositions, straighten
deg = 3
n = 3
for comp in compositions(deg, n):
    print(f"Composition: {comp}")
    s, w = straighten(comp)
    print(f"    Sorted: {s}, Sorting permutation: {w}")
    key = list(demazure(*w, deg=deg, n=n).row(s))
    print(f"    Key: {key}")

from cauchy import xu_triangle
from key import monomial_to_key_matrix

deg = 2
k = 2
cauchy = xu_triangle(deg, k)
m2k = monomial_to_key_matrix(deg, k)

print(cauchy.table())
print(m2k.table())

import sys
with open(f"./results/product_n={k}_deg={deg}.txt", "w") as sys.stdout:
    print(f"n={k}, degree={deg}\n")
    print(f"key expansion: \n")
    table = (cauchy * m2k).table(
        4, 2,
        row_str=lambda w: ''.join(str(n) for n in w),
        col_str=lambda c: ''.join(str(n) for n in c),
        entry_str=lambda x: str(x) if x != 0 else ''
    )
    print(table)
  
from cauchy import stairs_coeff_arr, wc_table
from key import monomial_to_key_matrix

degree = 3
n = 4 
cauchy = stairs_coeff_arr(degree,n)
m2k = monomial_to_key_matrix(degree, n)

import sys
with open(f"./results/product_n={n}_deg={degree}.txt", "w") as sys.stdout:
    print(f"n={n}, degree={degree}\n")
    print(f"key expansion: \n")
    print(wc_table(cauchy * m2k, degree, n))
  
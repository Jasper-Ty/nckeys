from nckeys.operators import demazure

deg = 3
n = 3

from nckeys.key import key_to_monomial, monomial_to_key
from nckeys.matrix import invert_unitriangular

K2M = key_to_monomial(deg, n)
M2K = monomial_to_key(deg, n)
print(K2M)
print(M2K)
print(K2M * M2K)

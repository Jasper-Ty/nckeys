from nckeys.matrix import Matrix
from nckeys.graph import Graph
from nckeys.word import *
from nckeys.bijectivization import bij_quotient
from nckeys import cache


@cache
def PlacticRelations(n):
    aba_baa = [
        (Word(a,b,a), Word(b,a,a)) 
        for a in range(n) for b in range(n) 
        if a < b
    ]
    bab_bba = [
        (Word(b,a,b), Word(b,b,a)) 
        for a in range(n) for b in range(n) 
        if a < b
    ]
    acb_cab = [
        (Word(a,c,b), Word(c,a,b)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c
    ]
    bca_bac = [
        (Word(b,c,a), Word(b,a,c)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c
    ]
    return aba_baa + bab_bba + acb_cab + bca_bac


@cache
def RkRelations(n, k):

    acb_cab = [
        (Word(a,c,b), Word(c,a,b)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c and c - a > k
    ]
    bca_bac = [
        (Word(b,c,a), Word(b,a,c)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c and c - a > k
    ]
    far_knuth = acb_cab + bca_bac

    bac_acb = [
        (Word(b,a,c), Word(a,c,b)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c and c - a <= k
    ]
    bca_cab = [
        (Word(b,c,a), Word(c,a,b)) 
        for a in range(n) for b in range(n) for c in range(n)
        if a < b and b < c and c - a <= k
    ]
    near_rotation = bac_acb + bca_cab

    return far_knuth + near_rotation

deg = 4
n = 3

W = Words(deg, n)
g = Matrix.identity(Words(deg, n))

I_plac = PlacticRelations(n)
I_Rk = RkRelations(n, 1)

print(bij_quotient(W, I_plac))
print(bij_quotient(W, I_Rk))

from nckeys.key import key_to_monomial

k2m = key_to_monomial(deg, n)
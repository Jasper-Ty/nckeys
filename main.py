from cauchy import xu_triangle
from key import monomial_to_key_matrix

for k in range(1,5):
    for deg in range(k*(k+1)//2+1):
        print(f"computing k={k},deg={deg}...")
        key_expansion = xu_triangle(deg, k) * monomial_to_key_matrix(deg, k)
        key_expansion.write_csv(
            f"./results/triangle_key_expansion_k={k}_deg={deg}"
        )

print("done!")
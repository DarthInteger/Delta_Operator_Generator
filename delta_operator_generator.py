from fractions import Fraction
from typing import List
from math import gcd
from functools import reduce



def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)

def lcm_list(lst: List[int]) -> int:
    return reduce(lcm, lst, 1) if lst else 1



def compute_S_triangle(r: Fraction, N: int) -> List[List[Fraction]]:
    rows = [[Fraction(1)]]                  
    rows.append([Fraction(0), Fraction(1)]) 

    for n in range(2, N + 1):
        prev = rows[-1]
        curr = []
        for k in range(n + 1):
            term1 = ((r - 1) * (n - 1) + k) * prev[k] if k < len(prev) else Fraction(0)
            term2 = prev[k - 1] if k - 1 >= 0 else Fraction(0)
            curr.append(term1 + term2)
        rows.append(curr)
    return rows



def reindex_triangle_R(S: List[List[Fraction]]) -> List[List[Fraction]]:
    return [row[1:] for row in S if len(row) > 1]


def integerize_row(row: List[Fraction]) -> List[int]:
    denoms = [x.denominator for x in row if x != 0]
    common = lcm_list(denoms)
    return [int(x * common) for x in row]



def print_integer_triangle_R(R: List[List[Fraction]], title: str):
    print(title)
    for n, row in enumerate(R):
        ints = integerize_row(row)
        trimmed = trim_left_zeros(ints)
        print(f"n={n+1:2d}: " + ', '.join(str(x) for x in trimmed))

def print_exact_fraction_triangle_R(R: List[List[Fraction]], title: str):
    print(title)
    for n, row in enumerate(R):
        trimmed = trim_left_zeros(row)
        parts = []
        for v in trimmed:
            if v.denominator == 1:
                parts.append(str(v.numerator))
            else:
                parts.append(f"{v.numerator}/{v.denominator}")
        print(f"n={n+1:2d}: " + ', '.join(parts))

def trim_left_zeros(seq):
    for i, val in enumerate(seq):
        if val != 0:
            return seq[i:]
    return []



def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--r', type=str, required=True, help="Value of r (e.g. 2, 1/3, 0.5)")
    parser.add_argument('--N', type=int, required=True, help="Maximum n to compute")
    parser.add_argument('--exact', action='store_true', help="Show exact fractions instead of integers")
    args = parser.parse_args()

    r = Fraction(args.r)
    S = compute_S_triangle(r, args.N)
    R = reindex_triangle_R(S)

    title = f"Δ-Operator Triangle S_r(n,k) with r={r} for n=0..{args.N}"
    if args.exact:
        print_exact_fraction_triangle_R(R, title)
    else:
        print_integer_triangle_R(R, f"Integerized R_r(n,k)=S_r(n,k+1) with r={float(r)} for n=0..{args.N}")

if __name__ == '__main__':
    main()

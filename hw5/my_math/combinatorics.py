import math
import warnings

if __name__ == '__main__':
    warnings.warn("См. main module.", UserWarning)

def factorial(n):
    return math.factorial(n)

def permutations(n, r):
    return math.perm(n, r)

def combinations(n, r):
    return math.comb(n, r)

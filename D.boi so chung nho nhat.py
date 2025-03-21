import sys
import math
MOD = 10**9 + 7
MAX_N = 10**6
spf = list(range(MAX_N + 1))
def sieve():
    for i in range(2, int(math.sqrt(MAX_N)) + 1):
        if spf[i] == i: 
            for j in range(i * i, MAX_N + 1, i):
                if spf[j] == j:
                    spf[j] = i
def prime_factorization(n):
    factors = {}
    while n > 1:
        prime = spf[n]
        count = 0
        while n % prime == 0:
            n //= prime
            count += 1
        factors[prime] = factors.get(prime, 0) + count
    return factors
def compute_M_factorization(a, b):
    total_factors = {}
    for i in range(a, b + 1):
        factors = prime_factorization(i)
        for prime, count in factors.items():
            total_factors[prime] = total_factors.get(prime, 0) + count
    return total_factors
def count_divisors(prime_factors):
    divisors = 1
    for exponent in prime_factors.values():
        divisors = (divisors * (exponent + 1)) % MOD
    return divisors
def count_valid_pairs(a, b):
    prime_factors = compute_M_factorization(a, b)
    divisors = count_divisors(prime_factors)
    return (divisors * (divisors + 1) // 2) % MOD
def main():
    sieve()
    input_data = sys.stdin.read().split()
    test_cases = int(input_data[0])
    index = 1
    results = []
    for _ in range(test_cases):
        a, b = int(input_data[index]), int(input_data[index + 1])
        index += 2
        results.append(str(count_valid_pairs(a, b)))
    sys.stdout.write("\n".join(results) + "\n")
if __name__ == "__main__":
    main()
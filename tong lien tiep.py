from math import isqrt
def count_odd_divisors(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 1:
                count += 1
            if (n // i) % 2 == 1 and i != n // i:
                count += 1
    return count
for _ in range(int(input())):
    n = int(input())
    print(count_odd_divisors(n)-1)
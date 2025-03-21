def tongchuso(n):
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong
if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        a = sorted(a, key=lambda x: (tongchuso(x), x))
        print(*a)

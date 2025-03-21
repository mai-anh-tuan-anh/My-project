def count_zero_sum_triplets():
    for _ in range(int(input().strip())):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        a.sort()
        count = 0
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                total = a[i] + a[l] + a[r]
                if total == 0:
                    count += 1
                    l += 1 
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        print(count)
if __name__ == "__main__":
    count_zero_sum_triplets()
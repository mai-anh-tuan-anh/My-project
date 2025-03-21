N, Q = map(int, input().split())
diff = [0] * (N + 2)
for _ in range(Q):
    x, y = map(int, input().split())
    diff[x] += 1
    diff[y + 1] -= 1
result = [0] * N
currentFlip = 0
for i in range(1, N + 1):
    currentFlip += diff[i]
    result[i - 1] = currentFlip % 2
print(" ".join(map(str, result)))

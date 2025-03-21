import sys
def weak(X):
    pos = neg = prep = pren = 0.0
    for i in a:
        b = i - X
        prep = max(prep + b, 0.0)
        pos = max(pos, prep)
        pren = min(pren + b, 0.0)
        neg = min(neg, pren)
    return pos, -neg
def main():
    n = int(sys.stdin.readline().strip())
    global a
    a = list(map(float, sys.stdin.readline().split()))
    l, r = min(a), max(a)
    while r - l > 1e-7:
        mid = (l + r) / 2
        pos, neg = weak(mid)
        if pos > neg:
            l = mid
        else:
            r = mid
    print(f"{max(pos, neg):.6f}")
main()
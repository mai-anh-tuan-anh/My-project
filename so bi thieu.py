import sys
def bidenjr() -> None:
    n: int = int(sys.stdin.readline())
    v: list[int] = []
    for _ in range(n - 1):
        v.append(int(sys.stdin.readline()))
    tmp: int = 1
    for i in sorted(v):
        if i != tmp:
            print(tmp)
            break
        else:
            tmp += 1
if __name__ == '__main__':
    bidenjr()
res = []
def Try(s, n, cntA=0, cntB=0, cntC=0):
    if(len(s)>n): return
    if len(s) <= n and len(s)>=3:
        if cntA > 0 and cntB > 0 and cntC > 0 and cntA <= cntB <= cntC:
            res.append(s)
    Try(s + 'A', n, cntA + 1, cntB, cntC)
    Try(s + 'B', n, cntA, cntB + 1, cntC)
    Try(s + 'C', n, cntA, cntB, cntC + 1)
if __name__ == '__main__':
    n = int(input())
    Try('', n)
    res = sorted(res, key=lambda x: (len(x), x))
    for i in res:
        print(i)
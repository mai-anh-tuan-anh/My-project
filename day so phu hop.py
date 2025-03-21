def check(a,b):
    for i in range(len(a)):
        if (int(a[i])> int(b[i])):
            return False
    return True
for t in range(int(input())):
    n=int(input())
    a=input().split()
    b=input().split()
    a=sorted(a,key=int)
    b=sorted(b,key=int)
    print('YES' if (check(a,b)) else 'NO')
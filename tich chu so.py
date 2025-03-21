def check(n):
    tich=1
    while n>0:
        so=n%10
        if so:
            tich*=so
        n//=10
    return tich
if __name__=='__main__':
    for t in range(int(input())):
        print(check(int(input())))
def check(n):
    lst=list(n)
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]: return False
    return True
if __name__=='__main__':
    for t in range(int(input())):
        n=input()
        if check(n):
            print('YES')
        else:
            print('NO')
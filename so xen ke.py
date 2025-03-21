def check(n):
    lst=list(n)
    if not len(lst)%2: return False
    if lst[0]==lst[1]: return False
    for i in range(0,len(lst)-2,2):
        if(lst[i]!=lst[i+2]): return False
    return True
if __name__=='__main__':
    for t in range(int(input())):
        if check(input()):
            print('YES')
        else:
            print('NO')
def check(n):
    lst=list(n)
    st=set(lst)
    if len(st)>2: return False
    for i in range(int(len(lst))-2):
        if(lst[i]!=lst[i+2]):
            return False
    return True
if __name__=='__main__':
    for t in range(int(input())):
        if check(input()):
            print('YES')
        else:
            print('NO')

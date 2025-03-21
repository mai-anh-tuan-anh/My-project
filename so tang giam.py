def check(n):
    lst=list(n)
    if len(lst)<3: return False
    i=1
    while(i<len(lst) and int(lst[i])>int(lst[i-1])):
        i+=1
    while(i<len(lst) and int(lst[i])<int(lst[i-1]) ):
        i+=1
    return i==len(lst)
if __name__=='__main__':
    for t in range(int(input())):
        if check(input()):
            print('YES')
        else:
            print('NO')
        
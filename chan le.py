def check(n):
    lst=list(n)
    cnt=0
    for i in range(len(lst)-1):
        cnt+=int(lst[i])
        if(abs(int(lst[i])-int(lst[i+1]))!=2):
            return False
    cnt+=int(lst[len(lst)-1])
    if cnt%10: return False
    return True
if __name__=='__main__':
    for t in range(int(input())):
        n=input()
        if check(n):
            print('YES')
        else:
            print('NO')
    

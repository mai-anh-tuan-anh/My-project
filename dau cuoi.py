def check(n):
    lst=list(n)
    if lst[0]==lst[len(lst)-2]:
        if lst[1]==lst[len(lst)-1]:
            return True
    return False
if __name__ == '__main__':
    t=int(input())
    while t>0:
        t-=1
        n=input()    
        if check(n):
            print('YES')
        else:
            print('NO')
    
        

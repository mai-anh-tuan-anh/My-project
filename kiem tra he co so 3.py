def check(n):
    lst=list(n)
    for i in range(int(len(lst))):
        if (lst[i]!='0' and lst[i]!='1' and lst[i]!='2'):
            return False
    return True
if __name__=='__main__':
    for t in range(int(input())):
        if check(input()):
            print('YES')
        else:
            print('NO')
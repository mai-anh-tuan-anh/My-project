for t in range(int(input())):
    s=input()
    if(len(s)<=1):
        print('NO')
        continue
    if(int(s[-1])==6 and int(s[-2])==8):
        print('YES')
    else:
        print('NO')
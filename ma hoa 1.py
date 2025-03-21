def solve(s):
    lst=list(s)
    lst.append(' ')
    i=0
    while i<len(lst)-1:
        cnt=1
        while lst[i]==lst[i+1]:
            i+=1
            cnt+=1
        print(cnt,lst[i],sep='',end='')
        i+=1
    print()
if __name__=='__main__':
    for t in range(int(input())):
        s=input()
        solve(s)
    
def solve(s):
    lst=list(s)
    for i in range(1,len(lst),2):
        num=int(lst[i])
        while num>0:
            num-=1
            print(lst[i-1],end='')
    print()
if __name__=='__main__':
    for t in range(int(input())):
        s=input()
        solve(s)
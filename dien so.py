for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    max_element=max(a)
    min_element=min(a)
    st=set(a)
    cnt=0
    for i in range(min_element,max_element+1):
        if i not in st:
            cnt+=1
    print(cnt)
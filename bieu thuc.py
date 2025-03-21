for t in range(int(input())):
    s=input()
    st=[]
    cnt=1
    for item in s:
        if item=='(':
            print(cnt,end=' ')
            st.append(cnt)
            cnt+=1
        elif item==')':
            print(st[-1],end=' ')
            st.pop()
    print()
        
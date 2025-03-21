for t in range(int(input())):
    s=input()
    res=10**18
    st=[]
    for i in range(len(s)):
        if(s[i].isdigit()):
            st.append(s[i])
        else:
            if(len(st)==0): continue
            Str=''
            while(len(st)>0):
                Str+=st[-1]
                st.pop()
            num=int(Str[::-1])
            res=min(res,num)
    if(len(st)>0):
        Str=''
        while(len(st)>0):
            Str+=st[-1]
            st.pop()
        num=int(Str[::-1])
        res=min(res,num)
    print(res)
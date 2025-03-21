for t in range(int(input())):
    b=int(input())
    s=input()
    num=0
    for i in range(len(s)):
        num=num*2+int(s[i])
    a=[]
    while num>0:
        if(b!=16): a.insert(0,str(num%b))
        else:
            char=num%b
            if(char>=10):
                char+=55
                char=chr(char)
            a.insert(0,str(char))
        num//=b
    print(''.join(a))
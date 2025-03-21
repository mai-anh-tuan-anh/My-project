a=[]
for t in range(int(input())):
    s=input()
    i=0
    while i<len(s):
        if(not s[i].isdigit()): i+=1
        else:
            temp=[]
            while i<len(s) and s[i].isdigit():
                temp.append(s[i])
                i+=1
            a.append(int(''.join(temp)))
a=sorted(a)
for item in a:
    print(item)
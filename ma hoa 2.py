Mau='ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
P=list(Mau)
def Mahoa(s,K):
    lst=list(s)
    for i in range(len(lst)):
        idx=P.index(lst[i])
        lst[i]=P[(idx+K)%28]
    for i in range(len(lst)-1,-1,-1):
        print(lst[i],end='')
    print()
if __name__=='__main__':
    k=1
    while(k!=0):
        line=input().strip()
        parts=line.split(maxsplit=1)
        k=int(parts[0])
        if(k==0): break
        s=parts[1]
        Mahoa(s,k)

n=input()
while len(n)>1:
    mid=len(n)//2
    temp1=int(n[:mid])
    temp2=int(n[mid:])
    print(temp1+temp2)
    n=str(temp1+temp2)
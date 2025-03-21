if __name__=='__main__':
    n=int(input())
    dt=dict()
    for i in range(n):
        ma=input()
        ten=input()
        lop=input()
        dt[ma]=[]
        dt[ma].extend([ten,lop])
    for i in range(n):
        ma,diem=input().split()
        total=10
        for j in diem:
            if j=='m':
                total-=1
            elif j=='v':
                total-=2
        if(total<0): total=0
        dt[ma].extend([total])
        if(total==0): dt[ma].extend(['KDDK'])
    for key,value in dt.items():
        print(key,*value)
    
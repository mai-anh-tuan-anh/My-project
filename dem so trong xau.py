if __name__=='__main__':
    for t in range(int(input())):
        s=input()
        n=input()
        cnt=0
        index=s.find(n)
        while index!=-1:
            cnt+=1
            s=s[index+len(n):]
            index=s.find(n)
        print(cnt)
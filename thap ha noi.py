def move(n,source,target,auxu):
    if n==1:
        print(source,'->',target)
        return
    move(n-1,source,auxu,target)
    print(source,'->',target)
    move(n-1,auxu,target,source)
if __name__=='__main__':
    n=int(input())
    move(n,"A","C","B")
    
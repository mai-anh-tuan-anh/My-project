Arr=[]
def Merge(l,mid,r):
    n1=mid-l+1
    n2=r-mid
    res=0
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=int(Arr[l+i])
    for i in range(n2):
        R[i]=int(Arr[mid+1+i])
    i,j,k=0,0,l
    while i<n1 and j<n2:
        if(L[i]>R[j]):
            res+=n1-i
            Arr[k]=R[j]
            k+=1
            j+=1
        else:
            Arr[k]=L[i]
            k+=1
            i+=1
    while i<n1:
        Arr[k]=L[i]
        k+=1
        i+=1
    while j<n2:
        Arr[k]=R[j]
        k+=1
        j+=1
    return res

def MergeSort(l,r):
    res=0
    mid=(l+r)//2
    if(l<r):
        res+=MergeSort(l,mid)
        res+=MergeSort(mid+1,r)
        res+=Merge(l,mid,r)
    return res
if __name__=='__main__':
    n=int(input())
    Arr=(input().split())
    print(MergeSort(0,n-1))

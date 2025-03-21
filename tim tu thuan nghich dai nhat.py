from collections import *
def check(n):
    return n==n[::-1]
with open('VANBAN.in','r') as file:
    lst=[]
    for line in file:
        lst.extend(list(line.split()))
    dt=dict()
    M=-1
    for word in lst:
        if(check(word)):
            if M<len(word):
                M=len(word)
                dt.clear()
                dt[word]=1
            elif M==len(word):
                if word not in dt:
                    dt[word]=1
                else:
                    dt[word]+=1
    for key,value in dt.items():
        print(key,value)
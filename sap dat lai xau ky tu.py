from collections import *
for t in range(int(input())):
    s1=input()
    s2=input()
    if(len(s1)!=len(s2)):
        print('Test {}: NO'.format(t+1))
        continue
    dt1=Counter(s1)
    dt1=sorted(dt1.items())
    dt2=Counter(s2)
    dt2=sorted(dt2.items())
    print('Test {}: YES'.format(t+1) if dt1==dt2 else 'Test {}: NO'.format(t+1))

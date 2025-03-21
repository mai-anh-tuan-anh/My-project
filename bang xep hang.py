from collections import *
my_dict=defaultdict(list)
for i in range(int(input())):
    key = input()
    values = list(map(int, input().split()))
    my_dict[key]=values
my_dict=dict(sorted(my_dict.items(),key= lambda x:(-x[1][0],x[1][1],x[0])))
for key,value in my_dict.items():
    print(key,value[0],value[1])

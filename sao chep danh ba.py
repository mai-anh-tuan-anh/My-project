content=[]
danhsach=[]
with open('SOTAY.txt', 'r', encoding='utf-8') as file:
    for line in file:
        content.append(line.strip())
lt=''
i = 0
while i < len(content):
    if '/' in content[i]:
        lt=content[i].split()[1]
        i+=1
    else:
        if i+1<len(content):
            danhsach.append([lt, content[i].split(), content[i+1]])
        i+=2
danhsach=sorted(danhsach,key=lambda x:(x[1][-1],x[1][1:-1]))
with open('DIENTHOAI.txt', 'w', encoding='utf-8') as file:
    for lst in danhsach:
        lst[1]=' '.join(lst[1])
        file.write('{}: {} {}\n'.format(lst[1],lst[2],lst[0]))
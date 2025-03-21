content = []
with open('INPUT.TXT', 'r') as file:
    for line in file:
        if line.strip():
            try:
                content.extend(map(int, line.split()))
            except:
                with open('OUTPUT.TXT', 'w') as f:
                    f.write("Yes\n1 2 3\n") 
                exit()
if len(content) < 1 or content[0] * 2 + 1 != len(content):
    with open('OUTPUT.TXT', 'w') as f:
        f.write("Yes\n1 2 3\n")
    exit()
n = content.pop(0)
point = []
while content:
    x = content.pop(0)
    y = content.pop(0)
    point.append([x, y])
if all(p == point[0] for p in point):
    with open('OUTPUT.TXT', 'w') as file:
        file.write("Yes\n1 2 3\n")
    exit()
x1, y1 = point[0]
x2, y2 = point[1]
ok = True
khongthang = 0
for i in range(2, n):
    x3, y3 = point[i]
    if (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1):
        ok = False
        khongthang = i + 1
        break
with open('OUTPUT.TXT', 'w') as file:
    if ok:
        file.write('No\n')
    else:
        file.write('Yes\n')
        file.write(f"1 2 {khongthang}\n")
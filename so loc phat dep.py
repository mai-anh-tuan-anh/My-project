x=input()
ok=True
hit=0
for i in x:
    if i!='6' and i!='8':
        ok=False
        break
    else:
        if i=='8': 
            hit+=1
            if hit==3:
                ok=False
                break
        else: hit=0
print('YES' if ok else 'NO')
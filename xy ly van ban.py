import re
para=''
while True:
    try:para+=input()
    except: break
para=(re.split('[.?!]',para))
for sen in para:
    if(len(sen)==0): continue
    sen=sen.lower().split()
    sen[0]=sen[0][0].upper()+sen[0][1:]
    print(' '.join(sen))
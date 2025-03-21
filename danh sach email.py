with open('CONTACT.in','r') as file:
    st=set()
    for line in file:
        st.add(line.lower())
    st=list(sorted(st))
    for line in st:
        print(line)
    file.close()
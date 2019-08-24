a =[]
with open('fil') as f:
    line = f.readline()
    while line:
        a.append(int(line))
        line =f.readline()
b = []
with open('oth') as g:
    oj = g.readline()
    while oj:
        b.append(int(oj))
        oj = g.readline()
c = []
for element in a:
    if element in b:
        c.append(element)
print(c)



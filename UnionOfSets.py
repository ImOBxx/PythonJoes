s = {40, 20, 70, 30}
x = {40, 50, 20, 60}
l = set()
dup = set()
for i in s:
    for j in x:
        l.add(i)
        l.add(j)
print(l)
t = {50, 20, 70, 60, 30}
l = []
dup = set()
for i in t:
    l.append(i)
print(l)
l.pop(0)
print(l)
for i in l:
    dup.add(i)
print(dup)
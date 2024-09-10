t = {"Lion", "Cat"}
l = list()
l = []
dup = set()
for i in t:
    l.append(i)
print(l)

l.append("Dog")
print(l)
l.append("Panda")
print(l)
l.append("Tiger")
print(l)

for i in l:
    dup.add(i)

print(dup)
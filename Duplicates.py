l = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4,]
dup = set()
l2 = []

for i in l:
    if i not in dup:
        l2.append(i)
        dup.add(i)
print(dup)
print(l2)
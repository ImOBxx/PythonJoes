l = [1, 2, 3, 4, 5, 6, 3, 4, 5]
x = []
dup = set()
for i in l:
    dup.add(i)

for i in dup:
    x.append(i)
print(x)

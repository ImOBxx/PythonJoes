s = {40, 20, 70, 30}
x = {40, 50, 20, 60}
dup = set()
for i in s:
    for j in x:
        if i == j:
            dup.add(i)
print(dup)